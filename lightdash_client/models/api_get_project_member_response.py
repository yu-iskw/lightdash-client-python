from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_get_project_member_response_status import (
    ApiGetProjectMemberResponseStatus,
)

if TYPE_CHECKING:
    from ..models.api_get_project_member_response_results import (
        ApiGetProjectMemberResponseResults,
    )


T = TypeVar("T", bound="ApiGetProjectMemberResponse")


@attr.s(auto_attribs=True)
class ApiGetProjectMemberResponse:
    """
    Attributes:
        results (ApiGetProjectMemberResponseResults):
        status (ApiGetProjectMemberResponseStatus):
    """

    results: "ApiGetProjectMemberResponseResults"
    status: ApiGetProjectMemberResponseStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_get_project_member_response_results import (
            ApiGetProjectMemberResponseResults,
        )

        d = src_dict.copy()
        results = ApiGetProjectMemberResponseResults.from_dict(d.pop("results"))

        status = ApiGetProjectMemberResponseStatus(d.pop("status"))

        api_get_project_member_response = cls(
            results=results,
            status=status,
        )

        api_get_project_member_response.additional_properties = d
        return api_get_project_member_response

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
