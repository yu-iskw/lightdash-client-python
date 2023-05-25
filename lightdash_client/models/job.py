import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..models.job_job_status import JobJobStatus
from ..models.job_job_type import JobJobType
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.job_job_results import JobJobResults
    from ..models.step import Step


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        job_uuid (str):
        updated_at (datetime.datetime):
        job_status (JobJobStatus):
        job_type (JobJobType):
        steps (List['Step']):
        project_uuid (Union[Unset, None, str]):
        created_at (Optional[datetime.datetime]):
        job_results (Union[Unset, None, JobJobResults]):
    """

    job_uuid: str
    updated_at: datetime.datetime
    job_status: JobJobStatus
    job_type: JobJobType
    steps: List["Step"]
    created_at: Optional[datetime.datetime]
    project_uuid: Union[Unset, None, str] = UNSET
    job_results: Union[Unset, None, "JobJobResults"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_uuid = self.job_uuid
        updated_at = self.updated_at.isoformat()

        job_status = self.job_status.value

        job_type = self.job_type.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        project_uuid = self.project_uuid
        created_at = self.created_at.isoformat() if self.created_at else None

        job_results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_results, Unset):
            job_results = self.job_results.to_dict() if self.job_results else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobUuid": job_uuid,
                "updatedAt": updated_at,
                "jobStatus": job_status,
                "jobType": job_type,
                "steps": steps,
                "createdAt": created_at,
            }
        )
        if project_uuid is not UNSET:
            field_dict["projectUuid"] = project_uuid
        if job_results is not UNSET:
            field_dict["jobResults"] = job_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_job_results import JobJobResults
        from ..models.step import Step

        d = src_dict.copy()
        job_uuid = d.pop("jobUuid")

        updated_at = isoparse(d.pop("updatedAt"))

        job_status = JobJobStatus(d.pop("jobStatus"))

        job_type = JobJobType(d.pop("jobType"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = Step.from_dict(steps_item_data)

            steps.append(steps_item)

        project_uuid = d.pop("projectUuid", UNSET)

        _created_at = d.pop("createdAt")
        created_at: Optional[datetime.datetime]
        if _created_at is None:
            created_at = None
        else:
            created_at = isoparse(_created_at)

        _job_results = d.pop("jobResults", UNSET)
        job_results: Union[Unset, None, JobJobResults]
        if _job_results is None:
            job_results = None
        elif isinstance(_job_results, Unset):
            job_results = UNSET
        else:
            job_results = JobJobResults.from_dict(_job_results)

        job = cls(
            job_uuid=job_uuid,
            updated_at=updated_at,
            job_status=job_status,
            job_type=job_type,
            steps=steps,
            project_uuid=project_uuid,
            created_at=created_at,
            job_results=job_results,
        )

        job.additional_properties = d
        return job

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
