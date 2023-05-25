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

from ..models.step_step_status import StepStepStatus
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.step_error import StepError


T = TypeVar("T", bound="Step")


@attr.s(auto_attribs=True)
class Step:
    """
    Attributes:
        job_uuid (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        step_status (StepStepStatus):
        step_type (str):
        step_label (str):
        started_at (Optional[datetime.datetime]):
        error (Union[Unset, None, StepError]):
    """

    job_uuid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    step_status: StepStepStatus
    step_type: str
    step_label: str
    started_at: Optional[datetime.datetime]
    error: Union[Unset, None, "StepError"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_uuid = self.job_uuid
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        step_status = self.step_status.value

        step_type = self.step_type
        step_label = self.step_label
        started_at = self.started_at.isoformat() if self.started_at else None

        error: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict() if self.error else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobUuid": job_uuid,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "stepStatus": step_status,
                "stepType": step_type,
                "stepLabel": step_label,
                "startedAt": started_at,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.step_error import StepError

        d = src_dict.copy()
        job_uuid = d.pop("jobUuid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        step_status = StepStepStatus(d.pop("stepStatus"))

        step_type = d.pop("stepType")

        step_label = d.pop("stepLabel")

        _started_at = d.pop("startedAt")
        started_at: Optional[datetime.datetime]
        if _started_at is None:
            started_at = None
        else:
            started_at = isoparse(_started_at)

        _error = d.pop("error", UNSET)
        error: Union[Unset, None, StepError]
        if _error is None:
            error = None
        elif isinstance(_error, Unset):
            error = UNSET
        else:
            error = StepError.from_dict(_error)

        step = cls(
            job_uuid=job_uuid,
            created_at=created_at,
            updated_at=updated_at,
            step_status=step_status,
            step_type=step_type,
            step_label=step_label,
            started_at=started_at,
            error=error,
        )

        step.additional_properties = d
        return step

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
