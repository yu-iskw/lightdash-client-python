from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bigquery_credentials_priority import BigqueryCredentialsPriority
from ..models.bigquery_credentials_type import BigqueryCredentialsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bigquery_credentials_start_of_week import (
        BigqueryCredentialsStartOfWeek,
    )


T = TypeVar("T", bound="BigqueryCredentials")


@attr.s(auto_attribs=True)
class BigqueryCredentials:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        type (BigqueryCredentialsType):
        project (str):
        dataset (str):
        threads (Union[Unset, float]):
        start_of_week (Union[Unset, None, BigqueryCredentialsStartOfWeek]):
        timeout_seconds (Union[Unset, float]):
        priority (Union[Unset, BigqueryCredentialsPriority]):
        retries (Union[Unset, float]):
        location (Union[Unset, str]):
        maximum_bytes_billed (Union[Unset, float]):
    """

    type: BigqueryCredentialsType
    project: str
    dataset: str
    threads: Union[Unset, float] = UNSET
    start_of_week: Union[Unset, None, "BigqueryCredentialsStartOfWeek"] = UNSET
    timeout_seconds: Union[Unset, float] = UNSET
    priority: Union[Unset, BigqueryCredentialsPriority] = UNSET
    retries: Union[Unset, float] = UNSET
    location: Union[Unset, str] = UNSET
    maximum_bytes_billed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        project = self.project
        dataset = self.dataset
        threads = self.threads
        start_of_week: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.start_of_week, Unset):
            start_of_week = self.start_of_week.to_dict() if self.start_of_week else None

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
        from ..models.bigquery_credentials_start_of_week import (
            BigqueryCredentialsStartOfWeek,
        )

        d = src_dict.copy()
        type = BigqueryCredentialsType(d.pop("type"))

        project = d.pop("project")

        dataset = d.pop("dataset")

        threads = d.pop("threads", UNSET)

        _start_of_week = d.pop("startOfWeek", UNSET)
        start_of_week: Union[Unset, None, BigqueryCredentialsStartOfWeek]
        if _start_of_week is None:
            start_of_week = None
        elif isinstance(_start_of_week, Unset):
            start_of_week = UNSET
        else:
            start_of_week = BigqueryCredentialsStartOfWeek.from_dict(_start_of_week)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, BigqueryCredentialsPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = BigqueryCredentialsPriority(_priority)

        retries = d.pop("retries", UNSET)

        location = d.pop("location", UNSET)

        maximum_bytes_billed = d.pop("maximumBytesBilled", UNSET)

        bigquery_credentials = cls(
            type=type,
            project=project,
            dataset=dataset,
            threads=threads,
            start_of_week=start_of_week,
            timeout_seconds=timeout_seconds,
            priority=priority,
            retries=retries,
            location=location,
            maximum_bytes_billed=maximum_bytes_billed,
        )

        bigquery_credentials.additional_properties = d
        return bigquery_credentials

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
