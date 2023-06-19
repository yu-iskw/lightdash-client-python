from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.warehouse_types_databricks import WarehouseTypesDATABRICKS
from ..models.week_day import WeekDay
from ..types import UNSET
from ..types import Unset

T = TypeVar(
    "T", bound="PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames"
)


@attr.s(auto_attribs=True)
class PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesDATABRICKS):
        database (str):
        server_host_name (str):
        http_path (str):
        start_of_week (Union[Unset, None, WeekDay]):
        catalog (Union[Unset, str]):
    """

    type: WarehouseTypesDATABRICKS
    database: str
    server_host_name: str
    http_path: str
    start_of_week: Union[Unset, None, WeekDay] = UNSET
    catalog: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        database = self.database
        server_host_name = self.server_host_name
        http_path = self.http_path
        start_of_week: Union[Unset, None, int] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.value if self.start_of_week else None

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
        d = src_dict.copy()
        type = WarehouseTypesDATABRICKS(d.pop("type"))

        database = d.pop("database")

        server_host_name = d.pop("serverHostName")

        http_path = d.pop("httpPath")

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, WeekDay]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = WeekDay(_start_of_week)

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
