import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scheduler_job_status import SchedulerJobStatus
from ..models.scheduler_log_target_type import SchedulerLogTargetType
from ..models.scheduler_log_task import SchedulerLogTask
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="SchedulerLog")


@_attrs_define
class SchedulerLog:
    """
    Attributes:
        status (SchedulerJobStatus):
        created_at (datetime.datetime):
        scheduled_time (datetime.datetime):
        job_id (str):
        task (SchedulerLogTask):
        details (Union[Unset, RecordStringAny]): Construct a type with a set of properties K of type T
        target_type (Union[Unset, SchedulerLogTargetType]):
        target (Union[Unset, str]):
        job_group (Union[Unset, str]):
        scheduler_uuid (Union[Unset, str]):
    """

    status: SchedulerJobStatus
    created_at: datetime.datetime
    scheduled_time: datetime.datetime
    job_id: str
    task: SchedulerLogTask
    details: Union[Unset, "RecordStringAny"] = UNSET
    target_type: Union[Unset, SchedulerLogTargetType] = UNSET
    target: Union[Unset, str] = UNSET
    job_group: Union[Unset, str] = UNSET
    scheduler_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.record_string_any import RecordStringAny

        d = src_dict.copy()
        status = SchedulerJobStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        scheduled_time = isoparse(d.pop("scheduledTime"))

        job_id = d.pop("jobId")

        task = SchedulerLogTask(d.pop("task"))

        _details = d.pop("details", UNSET)
        details: Union[Unset, RecordStringAny]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RecordStringAny.from_dict(_details)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, SchedulerLogTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = SchedulerLogTargetType(_target_type)

        target = d.pop("target", UNSET)

        job_group = d.pop("jobGroup", UNSET)

        scheduler_uuid = d.pop("schedulerUuid", UNSET)

        scheduler_log = cls(
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

        scheduler_log.additional_properties = d
        return scheduler_log

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
