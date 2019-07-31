"""
This file is automatically generated.
Do not modify.
"""

from typing import List, Dict, Any, Optional

NoneType = type(None)  
_omit = None  # type: NoneType
_omit = object()  # type: ignore

class Gateway(object):
    def __init__(self,
                 type=_omit,  # type: Optional[str]
                 sslCertificateRef=_omit,  # type: Optional[str]
                 port=_omit,  # type: Optional[int]
                 securePort=_omit,  # type: Optional[int]
                 instances=_omit,  # type: Optional[int]
                 annotations=_omit,  # type: Optional[Any]
                 placement=_omit,  # type: Optional[Any]
                 resources=_omit,  # type: Optional[Any]
                 ):
        self.type = type
        self.sslCertificateRef = sslCertificateRef
        self.port = port
        self.securePort = securePort
        self.instances = instances
        self.annotations = annotations
        self.placement = placement
        self.resources = resources

    @property
    def type(self):
        # type: () -> Optional[str]
        if self._type is _omit:
            raise AttributeError('type not found')
        return self._type
    
    @type.setter
    def type(self, new_val):
        # type: (Optional[str]) -> None
        self._type = new_val
    
    @property
    def sslCertificateRef(self):
        # type: () -> Optional[str]
        if self._sslCertificateRef is _omit:
            raise AttributeError('sslCertificateRef not found')
        return self._sslCertificateRef
    
    @sslCertificateRef.setter
    def sslCertificateRef(self, new_val):
        # type: (Optional[str]) -> None
        self._sslCertificateRef = new_val
    
    @property
    def port(self):
        # type: () -> Optional[int]
        if self._port is _omit:
            raise AttributeError('port not found')
        return self._port
    
    @port.setter
    def port(self, new_val):
        # type: (Optional[int]) -> None
        self._port = new_val
    
    @property
    def securePort(self):
        # type: () -> Optional[int]
        if self._securePort is _omit:
            raise AttributeError('securePort not found')
        return self._securePort
    
    @securePort.setter
    def securePort(self, new_val):
        # type: (Optional[int]) -> None
        self._securePort = new_val
    
    @property
    def instances(self):
        # type: () -> Optional[int]
        if self._instances is _omit:
            raise AttributeError('instances not found')
        return self._instances
    
    @instances.setter
    def instances(self, new_val):
        # type: (Optional[int]) -> None
        self._instances = new_val
    
    @property
    def annotations(self):
        # type: () -> Optional[Any]
        if self._annotations is _omit:
            raise AttributeError('annotations not found')
        return self._annotations
    
    @annotations.setter
    def annotations(self, new_val):
        # type: (Optional[Any]) -> None
        self._annotations = new_val
    
    @property
    def placement(self):
        # type: () -> Optional[Any]
        if self._placement is _omit:
            raise AttributeError('placement not found')
        return self._placement
    
    @placement.setter
    def placement(self, new_val):
        # type: (Optional[Any]) -> None
        self._placement = new_val
    
    @property
    def resources(self):
        # type: () -> Optional[Any]
        if self._resources is _omit:
            raise AttributeError('resources not found')
        return self._resources
    
    @resources.setter
    def resources(self, new_val):
        # type: (Optional[Any]) -> None
        self._resources = new_val

    def to_json(self):
        res = {
            'type': self._type,
            'sslCertificateRef': self._sslCertificateRef,
            'port': self._port,
            'securePort': self._securePort,
            'instances': self._instances,
            'annotations': self._annotations,
            'placement': self._placement,
            'resources': self._resources,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Gateway]
        return cls(
            type=data.get('type', _omit),
            sslCertificateRef=data.get('sslCertificateRef', _omit),
            port=data.get('port', _omit),
            securePort=data.get('securePort', _omit),
            instances=data.get('instances', _omit),
            annotations=data.get('annotations', _omit),
            placement=data.get('placement', _omit),
            resources=data.get('resources', _omit),
        )


class Replicated(object):
    def __init__(self,
                 size=_omit,  # type: Optional[int]
                 ):
        self.size = size

    @property
    def size(self):
        # type: () -> Optional[int]
        if self._size is _omit:
            raise AttributeError('size not found')
        return self._size
    
    @size.setter
    def size(self, new_val):
        # type: (Optional[int]) -> None
        self._size = new_val

    def to_json(self):
        res = {
            'size': self._size,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Replicated]
        return cls(
            size=data.get('size', _omit),
        )


class ErasureCoded(object):
    def __init__(self,
                 dataChunks=_omit,  # type: Optional[int]
                 codingChunks=_omit,  # type: Optional[int]
                 ):
        self.dataChunks = dataChunks
        self.codingChunks = codingChunks

    @property
    def dataChunks(self):
        # type: () -> Optional[int]
        if self._dataChunks is _omit:
            raise AttributeError('dataChunks not found')
        return self._dataChunks
    
    @dataChunks.setter
    def dataChunks(self, new_val):
        # type: (Optional[int]) -> None
        self._dataChunks = new_val
    
    @property
    def codingChunks(self):
        # type: () -> Optional[int]
        if self._codingChunks is _omit:
            raise AttributeError('codingChunks not found')
        return self._codingChunks
    
    @codingChunks.setter
    def codingChunks(self, new_val):
        # type: (Optional[int]) -> None
        self._codingChunks = new_val

    def to_json(self):
        res = {
            'dataChunks': self._dataChunks,
            'codingChunks': self._codingChunks,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[ErasureCoded]
        return cls(
            dataChunks=data.get('dataChunks', _omit),
            codingChunks=data.get('codingChunks', _omit),
        )


class MetadataPool(object):
    def __init__(self,
                 failureDomain=_omit,  # type: Optional[str]
                 replicated=_omit,  # type: Optional[Replicated]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 ):
        self.failureDomain = failureDomain
        self.replicated = replicated
        self.erasureCoded = erasureCoded

    @property
    def failureDomain(self):
        # type: () -> Optional[str]
        if self._failureDomain is _omit:
            raise AttributeError('failureDomain not found')
        return self._failureDomain
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def replicated(self):
        # type: () -> Optional[Replicated]
        if self._replicated is _omit:
            raise AttributeError('replicated not found')
        return self._replicated
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> Optional[ErasureCoded]
        if self._erasureCoded is _omit:
            raise AttributeError('erasureCoded not found')
        return self._erasureCoded
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val

    def to_json(self):
        res = {
            'failureDomain': self._failureDomain,
            'replicated': self.replicated.to_json() if self._replicated not in [None, _omit] else self._replicated,
            'erasureCoded': self.erasureCoded.to_json() if self._erasureCoded not in [None, _omit] else self._erasureCoded,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[MetadataPool]
        return cls(
            failureDomain=data.get('failureDomain', _omit),
            replicated=Replicated.from_json(data['replicated']) if 'replicated' in data else _omit,
            erasureCoded=ErasureCoded.from_json(data['erasureCoded']) if 'erasureCoded' in data else _omit,
        )


class DataPool(object):
    def __init__(self,
                 failureDomain=_omit,  # type: Optional[str]
                 replicated=_omit,  # type: Optional[Replicated]
                 erasureCoded=_omit,  # type: Optional[ErasureCoded]
                 ):
        self.failureDomain = failureDomain
        self.replicated = replicated
        self.erasureCoded = erasureCoded

    @property
    def failureDomain(self):
        # type: () -> Optional[str]
        if self._failureDomain is _omit:
            raise AttributeError('failureDomain not found')
        return self._failureDomain
    
    @failureDomain.setter
    def failureDomain(self, new_val):
        # type: (Optional[str]) -> None
        self._failureDomain = new_val
    
    @property
    def replicated(self):
        # type: () -> Optional[Replicated]
        if self._replicated is _omit:
            raise AttributeError('replicated not found')
        return self._replicated
    
    @replicated.setter
    def replicated(self, new_val):
        # type: (Optional[Replicated]) -> None
        self._replicated = new_val
    
    @property
    def erasureCoded(self):
        # type: () -> Optional[ErasureCoded]
        if self._erasureCoded is _omit:
            raise AttributeError('erasureCoded not found')
        return self._erasureCoded
    
    @erasureCoded.setter
    def erasureCoded(self, new_val):
        # type: (Optional[ErasureCoded]) -> None
        self._erasureCoded = new_val

    def to_json(self):
        res = {
            'failureDomain': self._failureDomain,
            'replicated': self.replicated.to_json() if self._replicated not in [None, _omit] else self._replicated,
            'erasureCoded': self.erasureCoded.to_json() if self._erasureCoded not in [None, _omit] else self._erasureCoded,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[DataPool]
        return cls(
            failureDomain=data.get('failureDomain', _omit),
            replicated=Replicated.from_json(data['replicated']) if 'replicated' in data else _omit,
            erasureCoded=ErasureCoded.from_json(data['erasureCoded']) if 'erasureCoded' in data else _omit,
        )


class Spec(object):
    def __init__(self,
                 gateway=_omit,  # type: Optional[Gateway]
                 metadataPool=_omit,  # type: Optional[MetadataPool]
                 dataPool=_omit,  # type: Optional[DataPool]
                 ):
        self.gateway = gateway
        self.metadataPool = metadataPool
        self.dataPool = dataPool

    @property
    def gateway(self):
        # type: () -> Optional[Gateway]
        if self._gateway is _omit:
            raise AttributeError('gateway not found')
        return self._gateway
    
    @gateway.setter
    def gateway(self, new_val):
        # type: (Optional[Gateway]) -> None
        self._gateway = new_val
    
    @property
    def metadataPool(self):
        # type: () -> Optional[MetadataPool]
        if self._metadataPool is _omit:
            raise AttributeError('metadataPool not found')
        return self._metadataPool
    
    @metadataPool.setter
    def metadataPool(self, new_val):
        # type: (Optional[MetadataPool]) -> None
        self._metadataPool = new_val
    
    @property
    def dataPool(self):
        # type: () -> Optional[DataPool]
        if self._dataPool is _omit:
            raise AttributeError('dataPool not found')
        return self._dataPool
    
    @dataPool.setter
    def dataPool(self, new_val):
        # type: (Optional[DataPool]) -> None
        self._dataPool = new_val

    def to_json(self):
        res = {
            'gateway': self.gateway.to_json() if self._gateway not in [None, _omit] else self._gateway,
            'metadataPool': self.metadataPool.to_json() if self._metadataPool not in [None, _omit] else self._metadataPool,
            'dataPool': self.dataPool.to_json() if self._dataPool not in [None, _omit] else self._dataPool,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> Optional[Spec]
        return cls(
            gateway=Gateway.from_json(data['gateway']) if 'gateway' in data else _omit,
            metadataPool=MetadataPool.from_json(data['metadataPool']) if 'metadataPool' in data else _omit,
            dataPool=DataPool.from_json(data['dataPool']) if 'dataPool' in data else _omit,
        )


class CephObjectStore(object):
    def __init__(self,
                 apiVersion,  # type: str
                 kind,  # type: str
                 metadata,  # type: Any
                 spec=_omit,  # type: Optional[Spec]
                 ):
        self.apiVersion = apiVersion
        self.kind = kind
        self.metadata = metadata
        self.spec = spec

    @property
    def apiVersion(self):
        # type: () -> str
        if self._apiVersion is _omit:
            raise AttributeError('apiVersion not found')
        return self._apiVersion
    
    @apiVersion.setter
    def apiVersion(self, new_val):
        # type: (str) -> None
        self._apiVersion = new_val
    
    @property
    def kind(self):
        # type: () -> str
        if self._kind is _omit:
            raise AttributeError('kind not found')
        return self._kind
    
    @kind.setter
    def kind(self, new_val):
        # type: (str) -> None
        self._kind = new_val
    
    @property
    def metadata(self):
        # type: () -> Any
        if self._metadata is _omit:
            raise AttributeError('metadata not found')
        return self._metadata
    
    @metadata.setter
    def metadata(self, new_val):
        # type: (Any) -> None
        self._metadata = new_val
    
    @property
    def spec(self):
        # type: () -> Optional[Spec]
        if self._spec is _omit:
            raise AttributeError('spec not found')
        return self._spec
    
    @spec.setter
    def spec(self, new_val):
        # type: (Optional[Spec]) -> None
        self._spec = new_val

    def to_json(self):
        res = {
            'apiVersion': self._apiVersion,
            'kind': self._kind,
            'metadata': self._metadata,
            'spec': self.spec.to_json() if self._spec not in [None, _omit] else self._spec,
        }
        return {k: v for k, v in res.items() if v is not _omit}

    @classmethod
    def from_json(cls, data):
        # type: (dict) -> CephObjectStore
        return cls(
            apiVersion=data['apiVersion'],
            kind=data['kind'],
            metadata=data['metadata'],
            spec=Spec.from_json(data['spec']) if 'spec' in data else _omit,
        )
