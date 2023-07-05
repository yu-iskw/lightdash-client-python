from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.databricks_credentials_type import DatabricksCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.databricks_credentials_start_of_week import (
        DatabricksCredentialsStartOfWeek,
    )


T = TypeVar("T", bound="DatabricksCredentials")


@attr.s(auto_attribs=True)
class DatabricksCredentials:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        type (DatabricksCredentialsType):
        database (str):
        server_host_name (str):
        http_path (str):
        start_of_week (Union[Unset, None, DatabricksCredentialsStartOfWeek]):
        catalog (Union[Unset, str]):
    """

    type: DatabricksCredentialsType
    database: str
    server_host_name: str
    http_path: str
    start_of_week: Union[Unset, None, "DatabricksCredentialsStartOfWeek"] = UNSET
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
        from ..models.databricks_credentials_start_of_week import (
            DatabricksCredentialsStartOfWeek,
        )

        d = src_dict.copy()
        type = DatabricksCredentialsType(d.pop("type"))

        database = d.pop("database")

        server_host_name = d.pop("serverHostName")

        http_path = d.pop("httpPath")

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, DatabricksCredentialsStartOfWeek]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = DatabricksCredentialsStartOfWeek.from_dict(_start_of_week)

        catalog = d.pop("catalog", UNSET)

        databricks_credentials = cls(
            type=type,
            database=database,
            server_host_name=server_host_name,
            http_path=http_path,
            start_of_week=start_of_week,
            catalog=catalog,
        )

        databricks_credentials.additional_properties = d
        return databricks_credentials

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
