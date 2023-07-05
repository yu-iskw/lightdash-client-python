from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_organization_member_profile_status import (
    ApiOrganizationMemberProfileStatus,
)

if TYPE_CHECKING:
    from ..models.api_organization_member_profile_results import (
        ApiOrganizationMemberProfileResults,
    )


T = TypeVar("T", bound="ApiOrganizationMemberProfile")


@attr.s(auto_attribs=True)
class ApiOrganizationMemberProfile:
    """
    Attributes:
        results (ApiOrganizationMemberProfileResults): Profile for a user's membership in an organization
        status (ApiOrganizationMemberProfileStatus):
    """

    results: "ApiOrganizationMemberProfileResults"
    status: ApiOrganizationMemberProfileStatus
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
        from ..models.api_organization_member_profile_results import (
            ApiOrganizationMemberProfileResults,
        )

        d = src_dict.copy()
        results = ApiOrganizationMemberProfileResults.from_dict(d.pop("results"))

        status = ApiOrganizationMemberProfileStatus(d.pop("status"))

        api_organization_member_profile = cls(
            results=results,
            status=status,
        )

        api_organization_member_profile.additional_properties = d
        return api_organization_member_profile

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
