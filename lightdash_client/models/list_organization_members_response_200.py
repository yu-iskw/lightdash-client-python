from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

from ..models.list_organization_members_response_200_status import ListOrganizationMembersResponse200Status

if TYPE_CHECKING:
    from ..models.list_organization_members_response_200_results_item import (
        ListOrganizationMembersResponse200ResultsItem,
    )


T = TypeVar("T", bound="ListOrganizationMembersResponse200")


@attr.s(auto_attribs=True)
class ListOrganizationMembersResponse200:
    """
    Attributes:
        results (List['ListOrganizationMembersResponse200ResultsItem']):
        status (ListOrganizationMembersResponse200Status):
    """

    results: List["ListOrganizationMembersResponse200ResultsItem"]
    status: ListOrganizationMembersResponse200Status
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.list_organization_members_response_200_results_item import (
            ListOrganizationMembersResponse200ResultsItem,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ListOrganizationMembersResponse200ResultsItem.from_dict(results_item_data)

            results.append(results_item)

        status = ListOrganizationMembersResponse200Status(d.pop("status"))

        list_organization_members_response_200 = cls(
            results=results,
            status=status,
        )

        list_organization_members_response_200.additional_properties = d
        return list_organization_members_response_200

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
