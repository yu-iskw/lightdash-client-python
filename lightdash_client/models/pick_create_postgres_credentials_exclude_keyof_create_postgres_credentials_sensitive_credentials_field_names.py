from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.warehouse_types_postgres import WarehouseTypesPOSTGRES
from ..models.week_day import WeekDay
from ..types import UNSET
from ..types import Unset

T = TypeVar(
    "T", bound="PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames"
)


@attr.s(auto_attribs=True)
class PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesPOSTGRES):
        schema (str):
        host (str):
        port (float):
        dbname (str):
        role (Union[Unset, str]):
        threads (Union[Unset, float]):
        start_of_week (Union[Unset, None, WeekDay]):
        use_ssh_tunnel (Union[Unset, bool]):
        ssh_tunnel_host (Union[Unset, str]):
        ssh_tunnel_port (Union[Unset, float]):
        ssh_tunnel_user (Union[Unset, str]):
        ssh_tunnel_public_key (Union[Unset, str]):
        keepalives_idle (Union[Unset, float]):
        sslmode (Union[Unset, str]):
        search_path (Union[Unset, str]):
    """

    type: WarehouseTypesPOSTGRES
    schema: str
    host: str
    port: float
    dbname: str
    role: Union[Unset, str] = UNSET
    threads: Union[Unset, float] = UNSET
    start_of_week: Union[Unset, None, WeekDay] = UNSET
    use_ssh_tunnel: Union[Unset, bool] = UNSET
    ssh_tunnel_host: Union[Unset, str] = UNSET
    ssh_tunnel_port: Union[Unset, float] = UNSET
    ssh_tunnel_user: Union[Unset, str] = UNSET
    ssh_tunnel_public_key: Union[Unset, str] = UNSET
    keepalives_idle: Union[Unset, float] = UNSET
    sslmode: Union[Unset, str] = UNSET
    search_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        schema = self.schema
        host = self.host
        port = self.port
        dbname = self.dbname
        role = self.role
        threads = self.threads
        start_of_week: Union[Unset, None, int] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.value if self.start_of_week else None

        use_ssh_tunnel = self.use_ssh_tunnel
        ssh_tunnel_host = self.ssh_tunnel_host
        ssh_tunnel_port = self.ssh_tunnel_port
        ssh_tunnel_user = self.ssh_tunnel_user
        ssh_tunnel_public_key = self.ssh_tunnel_public_key
        keepalives_idle = self.keepalives_idle
        sslmode = self.sslmode
        search_path = self.search_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "schema": schema,
                "host": host,
                "port": port,
                "dbname": dbname,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if threads is not UNSET:
            field_dict["threads"] = threads
        if start_of_week is not UNSET:
            field_dict["startOfWeek"] = start_of_week
        if use_ssh_tunnel is not UNSET:
            field_dict["useSshTunnel"] = use_ssh_tunnel
        if ssh_tunnel_host is not UNSET:
            field_dict["sshTunnelHost"] = ssh_tunnel_host
        if ssh_tunnel_port is not UNSET:
            field_dict["sshTunnelPort"] = ssh_tunnel_port
        if ssh_tunnel_user is not UNSET:
            field_dict["sshTunnelUser"] = ssh_tunnel_user
        if ssh_tunnel_public_key is not UNSET:
            field_dict["sshTunnelPublicKey"] = ssh_tunnel_public_key
        if keepalives_idle is not UNSET:
            field_dict["keepalivesIdle"] = keepalives_idle
        if sslmode is not UNSET:
            field_dict["sslmode"] = sslmode
        if search_path is not UNSET:
            field_dict["searchPath"] = search_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesPOSTGRES(d.pop("type"))

        schema = d.pop("schema")

        host = d.pop("host")

        port = d.pop("port")

        dbname = d.pop("dbname")

        role = d.pop("role", UNSET)

        threads = d.pop("threads", UNSET)

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, WeekDay]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = WeekDay(_start_of_week)

        use_ssh_tunnel = d.pop("useSshTunnel", UNSET)

        ssh_tunnel_host = d.pop("sshTunnelHost", UNSET)

        ssh_tunnel_port = d.pop("sshTunnelPort", UNSET)

        ssh_tunnel_user = d.pop("sshTunnelUser", UNSET)

        ssh_tunnel_public_key = d.pop("sshTunnelPublicKey", UNSET)

        keepalives_idle = d.pop("keepalivesIdle", UNSET)

        sslmode = d.pop("sslmode", UNSET)

        search_path = d.pop("searchPath", UNSET)

        pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names = (
            cls(
                type=type,
                schema=schema,
                host=host,
                port=port,
                dbname=dbname,
                role=role,
                threads=threads,
                start_of_week=start_of_week,
                use_ssh_tunnel=use_ssh_tunnel,
                ssh_tunnel_host=ssh_tunnel_host,
                ssh_tunnel_port=ssh_tunnel_port,
                ssh_tunnel_user=ssh_tunnel_user,
                ssh_tunnel_public_key=ssh_tunnel_public_key,
                keepalives_idle=keepalives_idle,
                sslmode=sslmode,
                search_path=search_path,
            )
        )

        pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names.additional_properties = (
            d
        )
        return (
            pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names
        )

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
