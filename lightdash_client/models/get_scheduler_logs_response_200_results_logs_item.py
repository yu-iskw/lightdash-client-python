import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.get_scheduler_logs_response_200_results_logs_item_status import (
    GetSchedulerLogsResponse200ResultsLogsItemStatus,
)
from ..models.get_scheduler_logs_response_200_results_logs_item_target_type import (
    GetSchedulerLogsResponse200ResultsLogsItemTargetType,
)
from ..models.get_scheduler_logs_response_200_results_logs_item_task import (
    GetSchedulerLogsResponse200ResultsLogsItemTask,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_scheduler_logs_response_200_results_logs_item_details import (
        GetSchedulerLogsResponse200ResultsLogsItemDetails,
    )


T = TypeVar("T", bound="GetSchedulerLogsResponse200ResultsLogsItem")


@attr.s(auto_attribs=True)
class GetSchedulerLogsResponse200ResultsLogsItem:
    """
    Attributes:
        status (GetSchedulerLogsResponse200ResultsLogsItemStatus):
        created_at (datetime.datetime):
        scheduled_time (datetime.datetime):
        job_id (str):
        task (GetSchedulerLogsResponse200ResultsLogsItemTask):
        details (Union[Unset, GetSchedulerLogsResponse200ResultsLogsItemDetails]): Construct a type with a set of
            properties K of type T
        target_type (Union[Unset, GetSchedulerLogsResponse200ResultsLogsItemTargetType]):
        target (Union[Unset, str]):
        job_group (Union[Unset, str]):
        scheduler_uuid (Union[Unset, str]):
    """

    status: GetSchedulerLogsResponse200ResultsLogsItemStatus
    created_at: datetime.datetime
    scheduled_time: datetime.datetime
    job_id: str
    task: GetSchedulerLogsResponse200ResultsLogsItemTask
    details: Union[Unset, "GetSchedulerLogsResponse200ResultsLogsItemDetails"] = UNSET
    target_type: Union[Unset, GetSchedulerLogsResponse200ResultsLogsItemTargetType] = UNSET
    target: Union[Unset, str] = UNSET
    job_group: Union[Unset, str] = UNSET
    scheduler_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        created_at = self.created_at.isoformat()

        scheduled_time = self.scheduled_time.isoformat()

        job_id = self.job_id
        task = self.task.value

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target = self.target
        job_group = self.job_group
        scheduler_uuid = self.scheduler_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "createdAt": created_at,
                "scheduledTime": scheduled_time,
                "jobId": job_id,
                "task": task,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target is not UNSET:
            field_dict["target"] = target
        if job_group is not UNSET:
            field_dict["jobGroup"] = job_group
        if scheduler_uuid is not UNSET:
            field_dict["schedulerUuid"] = scheduler_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_scheduler_logs_response_200_results_logs_item_details import (
            GetSchedulerLogsResponse200ResultsLogsItemDetails,
        )

        d = src_dict.copy()
        status = GetSchedulerLogsResponse200ResultsLogsItemStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        scheduled_time = isoparse(d.pop("scheduledTime"))

        job_id = d.pop("jobId")

        task = GetSchedulerLogsResponse200ResultsLogsItemTask(d.pop("task"))

        _details = d.pop("details", UNSET)
        details: Union[Unset, GetSchedulerLogsResponse200ResultsLogsItemDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GetSchedulerLogsResponse200ResultsLogsItemDetails.from_dict(_details)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, GetSchedulerLogsResponse200ResultsLogsItemTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = GetSchedulerLogsResponse200ResultsLogsItemTargetType(_target_type)

        target = d.pop("target", UNSET)

        job_group = d.pop("jobGroup", UNSET)

        scheduler_uuid = d.pop("schedulerUuid", UNSET)

        get_scheduler_logs_response_200_results_logs_item = cls(
            status=status,
            created_at=created_at,
            scheduled_time=scheduled_time,
            job_id=job_id,
            task=task,
            details=details,
            target_type=target_type,
            target=target,
            job_group=job_group,
            scheduler_uuid=scheduler_uuid,
        )

        get_scheduler_logs_response_200_results_logs_item.additional_properties = d
        return get_scheduler_logs_response_200_results_logs_item

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
