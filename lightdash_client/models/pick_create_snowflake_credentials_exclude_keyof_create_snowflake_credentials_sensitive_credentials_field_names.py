from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.warehouse_types_snowflake import WarehouseTypesSNOWFLAKE
from ..models.week_day import WeekDay
from ..types import UNSET
from ..types import Unset

T = TypeVar(
    "T", bound="PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames"
)


@attr.s(auto_attribs=True)
class PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesSNOWFLAKE):
        account (str):
        database (str):
        warehouse (str):
        schema (str):
        role (Union[Unset, str]):
        threads (Union[Unset, float]):
        client_session_keep_alive (Union[Unset, bool]):
        query_tag (Union[Unset, str]):
        access_url (Union[Unset, str]):
        start_of_week (Union[Unset, None, WeekDay]):
    """

    type: WarehouseTypesSNOWFLAKE
    account: str
    database: str
    warehouse: str
    schema: str
    role: Union[Unset, str] = UNSET
    threads: Union[Unset, float] = UNSET
    client_session_keep_alive: Union[Unset, bool] = UNSET
    query_tag: Union[Unset, str] = UNSET
    access_url: Union[Unset, str] = UNSET
    start_of_week: Union[Unset, None, WeekDay] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        account = self.account
        database = self.database
        warehouse = self.warehouse
        schema = self.schema
        role = self.role
        threads = self.threads
        client_session_keep_alive = self.client_session_keep_alive
        query_tag = self.query_tag
        access_url = self.access_url
        start_of_week: Union[Unset, None, int] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.value if self.start_of_week else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "account": account,
                "database": database,
                "warehouse": warehouse,
                "schema": schema,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if threads is not UNSET:
            field_dict["threads"] = threads
        if client_session_keep_alive is not UNSET:
            field_dict["clientSessionKeepAlive"] = client_session_keep_alive
        if query_tag is not UNSET:
            field_dict["queryTag"] = query_tag
        if access_url is not UNSET:
            field_dict["accessUrl"] = access_url
        if start_of_week is not UNSET:
            field_dict["startOfWeek"] = start_of_week

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesSNOWFLAKE(d.pop("type"))

        account = d.pop("account")

        database = d.pop("database")

        warehouse = d.pop("warehouse")

        schema = d.pop("schema")

        role = d.pop("role", UNSET)

        threads = d.pop("threads", UNSET)

        client_session_keep_alive = d.pop("clientSessionKeepAlive", UNSET)

        query_tag = d.pop("queryTag", UNSET)

        access_url = d.pop("accessUrl", UNSET)

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, WeekDay]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = WeekDay(_start_of_week)

        pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names = cls(
            type=type,
            account=account,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            threads=threads,
            client_session_keep_alive=client_session_keep_alive,
            query_tag=query_tag,
            access_url=access_url,
            start_of_week=start_of_week,
        )

        pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names.additional_properties = (
            d
        )
        return pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names

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
