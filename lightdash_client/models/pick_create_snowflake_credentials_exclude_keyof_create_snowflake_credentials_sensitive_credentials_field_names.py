from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_snowflake import WarehouseTypesSNOWFLAKE
from ..models.week_day import WeekDay
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames"
)


@_attrs_define
class PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesSNOWFLAKE):
        warehouse (str):
        account (str):
        database (str):
        schema (str):
        role (Union[Unset, str]):
        require_user_credentials (Union[Unset, bool]):
        threads (Union[Unset, float]):
        client_session_keep_alive (Union[Unset, bool]):
        query_tag (Union[Unset, str]):
        access_url (Union[Unset, str]):
        start_of_week (Union[None, Unset, WeekDay]):
        quoted_identifiers_ignore_case (Union[Unset, bool]):
    """

    type: WarehouseTypesSNOWFLAKE
    warehouse: str
    account: str
    database: str
    schema: str
    role: Union[Unset, str] = UNSET
    require_user_credentials: Union[Unset, bool] = UNSET
    threads: Union[Unset, float] = UNSET
    client_session_keep_alive: Union[Unset, bool] = UNSET
    query_tag: Union[Unset, str] = UNSET
    access_url: Union[Unset, str] = UNSET
    start_of_week: Union[None, Unset, WeekDay] = UNSET
    quoted_identifiers_ignore_case: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        warehouse = self.warehouse

        account = self.account

        database = self.database

        schema = self.schema

        role = self.role

        require_user_credentials = self.require_user_credentials

        threads = self.threads

        client_session_keep_alive = self.client_session_keep_alive

        query_tag = self.query_tag

        access_url = self.access_url

        start_of_week: Union[None, Unset, int]
        if isinstance(self.start_of_week, Unset):
            start_of_week = UNSET
        elif isinstance(self.start_of_week, WeekDay):
            start_of_week = self.start_of_week.value
        else:
            start_of_week = self.start_of_week

        quoted_identifiers_ignore_case = self.quoted_identifiers_ignore_case

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "warehouse": warehouse,
                "account": account,
                "database": database,
                "schema": schema,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if require_user_credentials is not UNSET:
            field_dict["requireUserCredentials"] = require_user_credentials
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
        if quoted_identifiers_ignore_case is not UNSET:
            field_dict["quotedIdentifiersIgnoreCase"] = quoted_identifiers_ignore_case

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesSNOWFLAKE(d.pop("type"))

        warehouse = d.pop("warehouse")

        account = d.pop("account")

        database = d.pop("database")

        schema = d.pop("schema")

        role = d.pop("role", UNSET)

        require_user_credentials = d.pop("requireUserCredentials", UNSET)

        threads = d.pop("threads", UNSET)

        client_session_keep_alive = d.pop("clientSessionKeepAlive", UNSET)

        query_tag = d.pop("queryTag", UNSET)

        access_url = d.pop("accessUrl", UNSET)

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

        quoted_identifiers_ignore_case = d.pop("quotedIdentifiersIgnoreCase", UNSET)

        pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names = cls(
            type=type,
            warehouse=warehouse,
            account=account,
            database=database,
            schema=schema,
            role=role,
            require_user_credentials=require_user_credentials,
            threads=threads,
            client_session_keep_alive=client_session_keep_alive,
            query_tag=query_tag,
            access_url=access_url,
            start_of_week=start_of_week,
            quoted_identifiers_ignore_case=quoted_identifiers_ignore_case,
        )

        pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names.additional_properties = d
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
