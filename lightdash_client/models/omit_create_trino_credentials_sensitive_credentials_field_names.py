from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.omit_create_trino_credentials_sensitive_credentials_field_names_type import (
    OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.omit_create_trino_credentials_sensitive_credentials_field_names_start_of_week import (
        OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
    )


T = TypeVar("T", bound="OmitCreateTrinoCredentialsSensitiveCredentialsFieldNames")


@attr.s(auto_attribs=True)
class OmitCreateTrinoCredentialsSensitiveCredentialsFieldNames:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        type (OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesType):
        schema (str):
        host (str):
        port (float):
        dbname (str):
        http_scheme (str):
        start_of_week (Union[Unset, None, OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek]):
    """

    type: OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesType
    schema: str
    host: str
    port: float
    dbname: str
    http_scheme: str
    start_of_week: Union[Unset, None, "OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        schema = self.schema
        host = self.host
        port = self.port
        dbname = self.dbname
        http_scheme = self.http_scheme
        start_of_week: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.to_dict() if self.start_of_week else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "schema": schema,
                "host": host,
                "port": port,
                "dbname": dbname,
                "http_scheme": http_scheme,
            }
        )
        if start_of_week is not UNSET:
            field_dict["startOfWeek"] = start_of_week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.omit_create_trino_credentials_sensitive_credentials_field_names_start_of_week import (
            OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
        )

        d = src_dict.copy()
        type = OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesType(d.pop("type"))

        schema = d.pop("schema")

        host = d.pop("host")

        port = d.pop("port")

        dbname = d.pop("dbname")

        http_scheme = d.pop("http_scheme")

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = OmitCreateTrinoCredentialsSensitiveCredentialsFieldNamesStartOfWeek.from_dict(
                _start_of_week
            )

        omit_create_trino_credentials_sensitive_credentials_field_names = cls(
            type=type,
            schema=schema,
            host=host,
            port=port,
            dbname=dbname,
            http_scheme=http_scheme,
            start_of_week=start_of_week,
        )

        omit_create_trino_credentials_sensitive_credentials_field_names.additional_properties = d
        return omit_create_trino_credentials_sensitive_credentials_field_names

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
