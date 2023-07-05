from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ValidateProjectResponse200Results")


@attr.s(auto_attribs=True)
class ValidateProjectResponse200Results:
    """
    Attributes:
        job_id (str):
    """

    job_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId")

        validate_project_response_200_results = cls(
            job_id=job_id,
        )

        validate_project_response_200_results.additional_properties = d
        return validate_project_response_200_results

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
