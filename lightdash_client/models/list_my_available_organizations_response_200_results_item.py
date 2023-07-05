from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListMyAvailableOrganizationsResponse200ResultsItem")


@attr.s(auto_attribs=True)
class ListMyAvailableOrganizationsResponse200ResultsItem:
    """
    Attributes:
        members_count (float):
        name (str):
        organization_uuid (str):
    """

    members_count: float
    name: str
    organization_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members_count = self.members_count
        name = self.name
        organization_uuid = self.organization_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "membersCount": members_count,
                "name": name,
                "organizationUuid": organization_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members_count = d.pop("membersCount")

        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        list_my_available_organizations_response_200_results_item = cls(
            members_count=members_count,
            name=name,
            organization_uuid=organization_uuid,
        )

        list_my_available_organizations_response_200_results_item.additional_properties = d
        return list_my_available_organizations_response_200_results_item

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
