import re
from dataclasses import dataclass
from typing import Iterable


def split(s):
    for x, y in re.findall(r"(\d*)(\D*)", s):
        yield "", int(x or "0")
        yield y, 0


def natural_keys(c):
    return tuple(split(c))


def human_sorted(iterable: Iterable):
    return sorted(iterable, key=natural_keys)


@dataclass(frozen=True)
class PrefixInfo:
    id: int
    prefix: str
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""


@dataclass(frozen=True)
class VLANInfo:
    id: int
    vid: int = None
    name: str = ""
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""


@dataclass(frozen=True)
class IPAddressInfo:
    id: int
    address: str
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""

    def __hash__(self):
        return hash((self.id, self.address))

    def __eq__(self, other):
        return self.id == other.id and self.address == other.address


@dataclass(frozen=True)
class VirtualMachineInfo:
    id: int
    name: str
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""


@dataclass(frozen=True)
class VMInterfaceInfo:
    id: int
    name: str
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""


@dataclass(frozen=True)
class VMDiskInfo:
    id: int
    name: str
    tenant_id: int = None
    tenant_name: str = ""
    tenant_permissions: str = ""
    tenant_permissions_ro: str = ""
