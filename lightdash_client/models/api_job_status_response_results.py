from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scheduler_job_status import SchedulerJobStatus

if TYPE_CHECKING:
    from ..models.record_string_any import RecordStringAny


T = TypeVar("T", bound="ApiJobStatusResponseResults")


@_attrs_define
class ApiJobStatusResponseResults:
    """
    Attributes:
        details (Union['RecordStringAny', None]):
        status (SchedulerJobStatus):
    """

    details: Union["RecordStringAny", None]
    status: SchedulerJobStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.record_string_any import RecordStringAny

        details: Union[Dict[str, Any], None]
        if isinstance(self.details, RecordStringAny):
            details = self.details.to_dict()
        else:
            details = self.details

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "details": details,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_any import RecordStringAny

        d = src_dict.copy()

        def _parse_details(data: object) -> Union["RecordStringAny", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = RecordStringAny.from_dict(data)

                return details_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RecordStringAny", None], data)

        details = _parse_details(d.pop("details"))

        status = SchedulerJobStatus(d.pop("status"))

        api_job_status_response_results = cls(
            details=details,
            status=status,
        )

        api_job_status_response_results.additional_properties = d
        return api_job_status_response_results

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
