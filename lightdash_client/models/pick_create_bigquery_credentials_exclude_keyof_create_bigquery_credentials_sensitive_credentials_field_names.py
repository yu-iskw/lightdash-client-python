from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names_priority import (
    PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority,
)
from ..models.warehouse_types_bigquery import WarehouseTypesBIGQUERY
from ..models.week_day import WeekDay
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames"
)


@_attrs_define
class PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesBIGQUERY):
        project (str):
        dataset (str):
        require_user_credentials (Union[Unset, bool]):
        threads (Union[Unset, float]):
        start_of_week (Union[None, Unset, WeekDay]):
        timeout_seconds (Union[Unset, float]):
        priority (Union[Unset,
            PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority]):
        retries (Union[Unset, float]):
        location (Union[Unset, str]):
        maximum_bytes_billed (Union[Unset, float]):
    """

    type: WarehouseTypesBIGQUERY
    project: str
    dataset: str
    require_user_credentials: Union[Unset, bool] = UNSET
    threads: Union[Unset, float] = UNSET
    start_of_week: Union[None, Unset, WeekDay] = UNSET
    timeout_seconds: Union[Unset, float] = UNSET
    priority: Union[
        Unset, PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority
    ] = UNSET
    retries: Union[Unset, float] = UNSET
    location: Union[Unset, str] = UNSET
    maximum_bytes_billed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        project = self.project

        dataset = self.dataset

        require_user_credentials = self.require_user_credentials

        threads = self.threads

        start_of_week: Union[None, Unset, int]
        if isinstance(self.start_of_week, Unset):
            start_of_week = UNSET
        elif isinstance(self.start_of_week, WeekDay):
            start_of_week = self.start_of_week.value
        else:
            start_of_week = self.start_of_week

        timeout_seconds = self.timeout_seconds

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        retries = self.retries

        location = self.location

        maximum_bytes_billed = self.maximum_bytes_billed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "project": project,
                "dataset": dataset,
            }
        )
        if require_user_credentials is not UNSET:
            field_dict["requireUserCredentials"] = require_user_credentials
        if threads is not UNSET:
            field_dict["threads"] = threads
        if start_of_week is not UNSET:
            field_dict["startOfWeek"] = start_of_week
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retries is not UNSET:
            field_dict["retries"] = retries
        if location is not UNSET:
            field_dict["location"] = location
        if maximum_bytes_billed is not UNSET:
            field_dict["maximumBytesBilled"] = maximum_bytes_billed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesBIGQUERY(d.pop("type"))

        project = d.pop("project")

        dataset = d.pop("dataset")

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

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[
            Unset,
            PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority,
        ]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNamesPriority(
                _priority
            )

        retries = d.pop("retries", UNSET)

        location = d.pop("location", UNSET)

        maximum_bytes_billed = d.pop("maximumBytesBilled", UNSET)

        pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names = (
            cls(
                type=type,
                project=project,
                dataset=dataset,
                require_user_credentials=require_user_credentials,
                threads=threads,
                start_of_week=start_of_week,
                timeout_seconds=timeout_seconds,
                priority=priority,
                retries=retries,
                location=location,
                maximum_bytes_billed=maximum_bytes_billed,
            )
        )

        pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names.additional_properties = d
        return (
            pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names
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
