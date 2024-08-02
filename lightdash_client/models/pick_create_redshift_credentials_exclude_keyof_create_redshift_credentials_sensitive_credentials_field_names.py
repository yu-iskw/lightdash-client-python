from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_redshift import WarehouseTypesREDSHIFT
from ..models.week_day import WeekDay
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames"
)


@_attrs_define
class PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesREDSHIFT):
        schema (str):
        host (str):
        port (float):
        dbname (str):
        require_user_credentials (Union[Unset, bool]):
        threads (Union[Unset, float]):
        start_of_week (Union[None, Unset, WeekDay]):
        use_ssh_tunnel (Union[Unset, bool]):
        ssh_tunnel_host (Union[Unset, str]):
        ssh_tunnel_port (Union[Unset, float]):
        ssh_tunnel_user (Union[Unset, str]):
        ssh_tunnel_public_key (Union[Unset, str]):
        keepalives_idle (Union[Unset, float]):
        sslmode (Union[Unset, str]):
        ra_3_node (Union[Unset, bool]):
    """

    type: WarehouseTypesREDSHIFT
    schema: str
    host: str
    port: float
    dbname: str
    require_user_credentials: Union[Unset, bool] = UNSET
    threads: Union[Unset, float] = UNSET
    start_of_week: Union[None, Unset, WeekDay] = UNSET
    use_ssh_tunnel: Union[Unset, bool] = UNSET
    ssh_tunnel_host: Union[Unset, str] = UNSET
    ssh_tunnel_port: Union[Unset, float] = UNSET
    ssh_tunnel_user: Union[Unset, str] = UNSET
    ssh_tunnel_public_key: Union[Unset, str] = UNSET
    keepalives_idle: Union[Unset, float] = UNSET
    sslmode: Union[Unset, str] = UNSET
    ra_3_node: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        schema = self.schema

        host = self.host

        port = self.port

        dbname = self.dbname

        require_user_credentials = self.require_user_credentials

        threads = self.threads

        start_of_week: Union[None, Unset, int]
        if isinstance(self.start_of_week, Unset):
            start_of_week = UNSET
        elif isinstance(self.start_of_week, WeekDay):
            start_of_week = self.start_of_week.value
        else:
            start_of_week = self.start_of_week

        use_ssh_tunnel = self.use_ssh_tunnel

        ssh_tunnel_host = self.ssh_tunnel_host

        ssh_tunnel_port = self.ssh_tunnel_port

        ssh_tunnel_user = self.ssh_tunnel_user

        ssh_tunnel_public_key = self.ssh_tunnel_public_key

        keepalives_idle = self.keepalives_idle

        sslmode = self.sslmode

        ra_3_node = self.ra_3_node

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
        if require_user_credentials is not UNSET:
            field_dict["requireUserCredentials"] = require_user_credentials
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
        if ra_3_node is not UNSET:
            field_dict["ra3Node"] = ra_3_node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesREDSHIFT(d.pop("type"))

        schema = d.pop("schema")

        host = d.pop("host")

        port = d.pop("port")

        dbname = d.pop("dbname")

        require_user_credentials = d.pop("requireUserCredentials", UNSET)

        threads = d.pop("threads", UNSET)

        def _parse_start_of_week(data: object) -> Union[None, Unset, WeekDay]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                start_of_week_type_1 = WeekDay(data)

                return start_of_week_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WeekDay], data)

        start_of_week = _parse_start_of_week(d.pop("startOfWeek", UNSET))

        use_ssh_tunnel = d.pop("useSshTunnel", UNSET)

        ssh_tunnel_host = d.pop("sshTunnelHost", UNSET)

        ssh_tunnel_port = d.pop("sshTunnelPort", UNSET)

        ssh_tunnel_user = d.pop("sshTunnelUser", UNSET)

        ssh_tunnel_public_key = d.pop("sshTunnelPublicKey", UNSET)

        keepalives_idle = d.pop("keepalivesIdle", UNSET)

        sslmode = d.pop("sslmode", UNSET)

        ra_3_node = d.pop("ra3Node", UNSET)

        pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names = (
            cls(
                type=type,
                schema=schema,
                host=host,
                port=port,
                dbname=dbname,
                require_user_credentials=require_user_credentials,
                threads=threads,
                start_of_week=start_of_week,
                use_ssh_tunnel=use_ssh_tunnel,
                ssh_tunnel_host=ssh_tunnel_host,
                ssh_tunnel_port=ssh_tunnel_port,
                ssh_tunnel_user=ssh_tunnel_user,
                ssh_tunnel_public_key=ssh_tunnel_public_key,
                keepalives_idle=keepalives_idle,
                sslmode=sslmode,
                ra_3_node=ra_3_node,
            )
        )

        pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names.additional_properties = d
        return (
            pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names
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
