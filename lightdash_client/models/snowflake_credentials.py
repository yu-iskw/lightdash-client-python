from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.snowflake_credentials_type import SnowflakeCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snowflake_credentials_start_of_week import (
        SnowflakeCredentialsStartOfWeek,
    )


T = TypeVar("T", bound="SnowflakeCredentials")


@attr.s(auto_attribs=True)
class SnowflakeCredentials:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        type (SnowflakeCredentialsType):
        account (str):
        database (str):
        warehouse (str):
        schema (str):
        role (Union[Unset, str]):
        threads (Union[Unset, float]):
        client_session_keep_alive (Union[Unset, bool]):
        query_tag (Union[Unset, str]):
        access_url (Union[Unset, str]):
        start_of_week (Union[Unset, None, SnowflakeCredentialsStartOfWeek]):
    """

    type: SnowflakeCredentialsType
    account: str
    database: str
    warehouse: str
    schema: str
    role: Union[Unset, str] = UNSET
    threads: Union[Unset, float] = UNSET
    client_session_keep_alive: Union[Unset, bool] = UNSET
    query_tag: Union[Unset, str] = UNSET
    access_url: Union[Unset, str] = UNSET
    start_of_week: Union[Unset, None, "SnowflakeCredentialsStartOfWeek"] = UNSET
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
        start_of_week: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.to_dict() if self.start_of_week else None

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
        from ..models.snowflake_credentials_start_of_week import (
            SnowflakeCredentialsStartOfWeek,
        )

        d = src_dict.copy()
        type = SnowflakeCredentialsType(d.pop("type"))

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
        start_of_week: Union[Unset, None, SnowflakeCredentialsStartOfWeek]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = SnowflakeCredentialsStartOfWeek.from_dict(_start_of_week)

        snowflake_credentials = cls(
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

        snowflake_credentials.additional_properties = d
        return snowflake_credentials

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
