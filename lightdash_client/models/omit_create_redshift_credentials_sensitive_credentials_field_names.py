from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.omit_create_redshift_credentials_sensitive_credentials_field_names_type import (
    OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.omit_create_redshift_credentials_sensitive_credentials_field_names_start_of_week import (
        OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
    )


T = TypeVar("T", bound="OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNames")


@attr.s(auto_attribs=True)
class OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNames:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        type (OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesType):
        schema (str):
        host (str):
        port (float):
        dbname (str):
        threads (Union[Unset, float]):
        start_of_week (Union[Unset, None, OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek]):
        use_ssh_tunnel (Union[Unset, bool]):
        ssh_tunnel_host (Union[Unset, str]):
        ssh_tunnel_port (Union[Unset, float]):
        ssh_tunnel_user (Union[Unset, str]):
        ssh_tunnel_public_key (Union[Unset, str]):
        keepalives_idle (Union[Unset, float]):
        sslmode (Union[Unset, str]):
        ra_3_node (Union[Unset, bool]):
    """

    type: OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesType
    schema: str
    host: str
    port: float
    dbname: str
    threads: Union[Unset, float] = UNSET
    start_of_week: Union[Unset, None, "OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek"] = UNSET
    use_ssh_tunnel: Union[Unset, bool] = UNSET
    ssh_tunnel_host: Union[Unset, str] = UNSET
    ssh_tunnel_port: Union[Unset, float] = UNSET
    ssh_tunnel_user: Union[Unset, str] = UNSET
    ssh_tunnel_public_key: Union[Unset, str] = UNSET
    keepalives_idle: Union[Unset, float] = UNSET
    sslmode: Union[Unset, str] = UNSET
    ra_3_node: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        schema = self.schema
        host = self.host
        port = self.port
        dbname = self.dbname
        threads = self.threads
        start_of_week: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.to_dict() if self.start_of_week else None

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
        from ..models.omit_create_redshift_credentials_sensitive_credentials_field_names_start_of_week import (
            OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
        )

        d = src_dict.copy()
        type = OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesType(d.pop("type"))

        schema = d.pop("schema")

        host = d.pop("host")

        port = d.pop("port")

        dbname = d.pop("dbname")

        threads = d.pop("threads", UNSET)

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = OmitCreateRedshiftCredentialsSensitiveCredentialsFieldNamesStartOfWeek.from_dict(
                _start_of_week
            )

        use_ssh_tunnel = d.pop("useSshTunnel", UNSET)

        ssh_tunnel_host = d.pop("sshTunnelHost", UNSET)

        ssh_tunnel_port = d.pop("sshTunnelPort", UNSET)

        ssh_tunnel_user = d.pop("sshTunnelUser", UNSET)

        ssh_tunnel_public_key = d.pop("sshTunnelPublicKey", UNSET)

        keepalives_idle = d.pop("keepalivesIdle", UNSET)

        sslmode = d.pop("sslmode", UNSET)

        ra_3_node = d.pop("ra3Node", UNSET)

        omit_create_redshift_credentials_sensitive_credentials_field_names = cls(
            type=type,
            schema=schema,
            host=host,
            port=port,
            dbname=dbname,
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

        omit_create_redshift_credentials_sensitive_credentials_field_names.additional_properties = d
        return omit_create_redshift_credentials_sensitive_credentials_field_names

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
