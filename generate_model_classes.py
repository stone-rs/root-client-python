"""
Generate Python files containing data Python models classes for
all properties of the all CRDs in the file

**Note**: generate_model_classes.py is independent of Rook or Ceph. It can be used for all
  CRDs.

For example:
  python3 -m venv venv
  pip install -r requirements.txt
  python generate_model_classes.py <crds.yaml> <output-folder>
  python setup.py develop

Usage:
  generate_model_classes.py <crds.yaml> <output-folder>
"""
import os
from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import List, Union, Iterator, Optional, Dict, TypeVar, Callable

import yaml
try:
    from dataclasses import dataclass
except ImportError:
    from attr import dataclass  # type: ignore

T = TypeVar('T')
K = TypeVar('K')

header = '''"""
This file is automatically generated.
Do not modify.
"""

try:
    from typing import Any, Optional, Union, List
except ImportError:
    pass

from .._helper import _omit, CrdObject, CrdObjectList, CrdClass

'''

@dataclass  # type: ignore
class CRDBase(ABC):
    name: str
    nullable: bool
    required: bool

    @property
    def py_name(self):
        return self.name

    @property
    @abstractmethod
    def py_type(self):
        ...

    @abstractmethod
    def flatten(self) -> Iterator[Union['CRDClass', 'CRDList', 'CRDAttribute']]:
        ...

    @abstractmethod
    def toplevel(self) -> str:
        ...

    def py_property(self):
        return f"""
@property
def {self.py_name}(self):
    # type: () -> {self.py_property_return_type}
    return self._property_impl('{self.py_name}')

@{self.py_name}.setter
def {self.py_name}(self, new_val):
    # type: ({self.py_param_type}) -> None
    self._{self.py_name} = new_val
    """.strip()

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}=_omit,  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required

    @property
    def py_param_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable or not self.required) else self.py_type

    @property
    def py_property_return_type(self):
        return f'Optional[{self.py_type}]' if (self.nullable) else self.py_type

@dataclass
class CRDAttribute(CRDBase):
    type: str
    default_value: str='_omit'

    @property
    def py_param(self):
        if not self.has_default:
            return f'{self.py_name},  # type: {self.py_param_type}'
        return f'{self.py_name}={self.default_value},  # type: {self.py_param_type}'

    @property
    def has_default(self):
        return not self.required or self.default_value != '_omit'

    @property
    def py_type(self):
        return {
            'integer': 'int',
            'boolean': 'bool',
            'string': 'str',
            'object': 'Any',
            'number': 'float',
            'x-kubernetes-int-or-string': 'Union[int, str]',
        }[self.type]

    def flatten(self) -> Iterator[Union['CRDClass', 'CRDList', 'CRDAttribute']]:
        yield from ()

    def toplevel(self):
        return ''

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.toplevel() == other.toplevel()

    def __hash__(self):
        return hash(self.toplevel())


@dataclass
class CRDList(CRDBase):
    items: 'CRDClass'

    @property
    def py_name(self):
        return self.name

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:] + 'List'

    @property
    def py_param_type(self):
        inner = f'Union[List[{self.items.py_type}], CrdObjectList]'
        return f'Optional[{inner}]' if (self.nullable or not self.required) else inner

    @property
    def py_property_return_type(self):
        inner = f'Union[List[{self.items.py_type}], CrdObjectList]'
        return f'Optional[{inner}]' if (self.nullable) else inner

    def flatten(self) -> Iterator[Union['CRDClass', 'CRDList', 'CRDAttribute']]:
        yield from self.items.flatten()
        yield self

    def toplevel(self):
        py_type = self.items.py_type
        if py_type == 'Any':
            py_type = 'None'

        return f"""
class {self.py_type}(CrdObjectList):
{indent('_items_type = ' + py_type)}
""".strip()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.toplevel() == other.toplevel()

    def __hash__(self):
        return hash(self.toplevel())


@dataclass
class CRDClass(CRDBase):
    attrs: List[Union[CRDAttribute, 'CRDClass']]
    base_class: str = 'CrdObject'

    def toplevel(self) -> str:
        ps = '\n\n'.join(a.py_property() for a in self.attrs)
        return f"""class {self.py_type}({self.base_class}):
{indent(self.py_properties())}        

{indent(self.py_init())}

{indent(ps)}
""".strip()

    @property
    def sub_classes(self) -> List["CRDClass"]:
        return [a for a in self.attrs if isinstance(a, CRDClass)]

    @property
    def py_type(self):
        return self.name[0].upper() + self.name[1:]

    def py_properties(self):
        def a_to_tuple(a):
            return ', '.join((f"'{a.name}'",
                       f"'{a.py_name}'",
                       a.py_type.replace('Any', 'object'),
                       str(a.required),
                       str(a.nullable)))

        attrlist = ',\n'.join([f'({a_to_tuple(a)})' for a in self.attrs])
        return f"""_properties = [\n{indent(attrlist)}\n]"""

    def flatten(self) -> Iterator[Union['CRDClass', 'CRDList', 'CRDAttribute']]:
        for sub_cls in self.attrs:
            yield from sub_cls.flatten()
        yield self

    def py_init(self):
        sorted_attrs = sorted(self.attrs, key=lambda a: a.has_default)
        params = '\n'.join(a.py_param for a in sorted_attrs)
        params_set = '\n'.join(f'{a.py_name}={a.py_name},' for a in sorted_attrs)
        return f"""
def __init__(self,
{indent(params, indent=4+9)}
             ):
    super({self.py_type}, self).__init__(
{indent(params_set, indent=8)}
    )
""".strip()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.toplevel() == other.toplevel()

    def __hash__(self):
        return hash(self.toplevel())


def indent(s, indent=4):
    return '\n'.join(' '*indent + l for l in s.splitlines())


def handle_property(elem_name, elem: dict, required: bool):
    nullable = elem.get('nullable', False)
    if 'properties' in elem:
        ps = elem['properties']
        required_elems = elem.get('required', [])
        sub_props = [handle_property(k, v, k in required_elems) for k, v in ps.items()]
        return CRDClass(elem_name, nullable, required, sub_props)
    elif 'items' in elem:
        item = handle_property(elem_name + 'Item', elem['items'], False)
        return CRDList(elem_name, nullable, required, item)
    elif 'type' in elem:
        return CRDAttribute(elem_name, nullable, required, elem['type'])
    elif elem == {}:
        return CRDAttribute(elem_name, nullable, required, 'object')
    elif 'x-kubernetes-int-or-string' in elem:
        return CRDAttribute(elem_name, nullable, required, 'x-kubernetes-int-or-string')

    assert False, str((elem_name, elem))

def spec_get_schema(c_dict: Dict) -> Dict:
    try:
        return c_dict['spec']['validation']['openAPIV3Schema']
    except (KeyError, TypeError):
        pass
    versions = c_dict['spec']['versions']
    if len(versions) != 1:
        raise RuntimeError(f'todo: {[v["name"] for v in versions]}')
    return c_dict['spec']['versions'][0]["schema"]['openAPIV3Schema']

def handle_crd(c_dict: dict) -> Optional[CRDClass]:
    try:
        name = c_dict['spec']['names']['kind']
        s = spec_get_schema(c_dict)
    except (KeyError, TypeError):
        return None
    s['required'] = ['spec']
    c = handle_property(name, s, True)
    if 'apiVersion' not in [a.name for a in c.attrs]:
        c.attrs.append(CRDAttribute('apiVersion', False, True, 'string'))
    if 'metadata' not in [a.name for a in c.attrs]:
        c.attrs.append(CRDAttribute('metadata', False, True, 'object'))
    if 'status' not in [a.name for a in c.attrs]:
        c.attrs.append(CRDAttribute('status', False, False, 'object'))
    return CRDClass(c.name, False, True, c.attrs, base_class='CrdClass')


def local(yaml_filename):
    with open(yaml_filename) as f:
        yamls = yaml.safe_load_all(f.read())
        for y in yamls:
            try:
                yield y
            except AttributeError:
                pass


def remove_duplicates_by(items: List[T], key: Callable[[T], K], unify: Callable[[T, T], T]) -> List[T]:
    res: OrderedDict[K, T] = OrderedDict()
    for i in items:
        k = key(i)
        if k in res:
            res[k] = unify(res[k], i)
        else:
            res[k] = i
    return list(res.values())


def remove_duplicates(items: List[T]) -> List[T]:
    return list(OrderedDict.fromkeys(items).keys())


def unify_classes(left: CRDBase, right: CRDBase) -> CRDBase:
    assert left.py_type == right.py_type
    assert type(left) == type(right), (type(left), type(right), left.py_type, right.toplevel())
    if isinstance(left, CRDClass) and isinstance(right, CRDClass):
        assert left.base_class == right.base_class
        return CRDClass(
            name=left.name,
            nullable=left.nullable or right.nullable,
            required=False,
            attrs=remove_duplicates(right.attrs + left.attrs),
            base_class=left.base_class
        )
    else:
        return left


def get_toplevels(crd: CRDBase) -> List[str]:
    elems: List[CRDBase] = remove_duplicates(list(crd.flatten()))
    res = remove_duplicates_by(elems, lambda c: c.py_type, unify_classes)
    return [e.toplevel() for e in res]


def main(yaml_filename, outfolder):
    for crd in local(yaml_filename):
        valid_crd = handle_crd(crd)
        if valid_crd is not None:
            try:
                os.mkdir(outfolder)
            except FileExistsError:
                pass
            open(f'{outfolder}/__init__.py', 'w').close()

            with open(f'{outfolder}/{valid_crd.name.lower()}.py', 'w') as f:
                f.write(header)
                classes = get_toplevels(valid_crd)
                f.write('\n\n\n'.join(classes))
                f.write('\n')


if __name__ == '__main__':
    from docopt import docopt
    args = docopt(__doc__)
    yaml_filename = '/dev/stdin' if args["<crds.yaml>"] == '-' else args["<crds.yaml>"]
    main(yaml_filename, args["<output-folder>"])