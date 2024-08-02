from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_databricks import WarehouseTypesDATABRICKS
from ..models.week_day import WeekDay
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames"
)


@_attrs_define
class PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesDATABRICKS):
        database (str):
        server_host_name (str):
        http_path (str):
        require_user_credentials (Union[Unset, bool]):
        start_of_week (Union[None, Unset, WeekDay]):
        catalog (Union[Unset, str]):
    """

    type: WarehouseTypesDATABRICKS
    database: str
    server_host_name: str
    http_path: str
    require_user_credentials: Union[Unset, bool] = UNSET
    start_of_week: Union[None, Unset, WeekDay] = UNSET
    catalog: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        database = self.database

        server_host_name = self.server_host_name

        http_path = self.http_path

        require_user_credentials = self.require_user_credentials

        start_of_week: Union[None, Unset, int]
        if isinstance(self.start_of_week, Unset):
            start_of_week = UNSET
        elif isinstance(self.start_of_week, WeekDay):
            start_of_week = self.start_of_week.value
        else:
            start_of_week = self.start_of_week

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
        if require_user_credentials is not UNSET:
            field_dict["requireUserCredentials"] = require_user_credentials
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

        require_user_credentials = d.pop("requireUserCredentials", UNSET)

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

        catalog = d.pop("catalog", UNSET)

        pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names = cls(
            type=type,
            database=database,
            server_host_name=server_host_name,
            http_path=http_path,
            require_user_credentials=require_user_credentials,
            start_of_week=start_of_week,
            catalog=catalog,
        )

        pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names.additional_properties = d
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
