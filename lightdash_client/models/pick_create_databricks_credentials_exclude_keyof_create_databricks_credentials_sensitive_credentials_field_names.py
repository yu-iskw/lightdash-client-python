from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names_type import (
    PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names_start_of_week import (
        PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
    )


T = TypeVar(
    "T", bound="PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames"
)


@attr.s(auto_attribs=True)
class PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType):
        database (str):
        server_host_name (str):
        http_path (str):
        start_of_week (Union[Unset, None, PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiv
            eCredentialsFieldNamesStartOfWeek]):
        catalog (Union[Unset, str]):
    """

    type: PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType
    database: str
    server_host_name: str
    http_path: str
    start_of_week: Union[
        Unset,
        None,
        "PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesStartOfWeek",
    ] = UNSET
    catalog: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        database = self.database
        server_host_name = self.server_host_name
        http_path = self.http_path
        start_of_week: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.to_dict() if self.start_of_week else None

        catalog = self.catalog

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "database": database,
                "serverHostName": server_host_name,
                "httpPath": http_path,
            }
        )
        if start_of_week is not UNSET:
            field_dict["startOfWeek"] = start_of_week
        if catalog is not UNSET:
            field_dict["catalog"] = catalog

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names_start_of_week import (
            PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
        )

        d = src_dict.copy()
        type = PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesType(
            d.pop("type")
        )

        database = d.pop("database")

        server_host_name = d.pop("serverHostName")

        http_path = d.pop("httpPath")

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[
            Unset,
            None,
            PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesStartOfWeek,
        ]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNamesStartOfWeek.from_dict(
                _start_of_week
            )

        catalog = d.pop("catalog", UNSET)

        pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names = cls(
            type=type,
            database=database,
            server_host_name=server_host_name,
            http_path=http_path,
            start_of_week=start_of_week,
            catalog=catalog,
        )

        pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names.additional_properties = (
            d
        )
        return pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names

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
