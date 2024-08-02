from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_project_access_list_response_status import (
    ApiProjectAccessListResponseStatus,
)

if TYPE_CHECKING:
    from ..models.project_member_profile import ProjectMemberProfile


T = TypeVar("T", bound="ApiProjectAccessListResponse")


@_attrs_define
class ApiProjectAccessListResponse:
    """
    Attributes:
        results (List['ProjectMemberProfile']):
        status (ApiProjectAccessListResponseStatus):
    """

    results: List["ProjectMemberProfile"]
    status: ApiProjectAccessListResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

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
        from ..models.project_member_profile import ProjectMemberProfile

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ProjectMemberProfile.from_dict(results_item_data)

            results.append(results_item)

        status = ApiProjectAccessListResponseStatus(d.pop("status"))

        api_project_access_list_response = cls(
            results=results,
            status=status,
        )

        api_project_access_list_response.additional_properties = d
        return api_project_access_list_response

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
