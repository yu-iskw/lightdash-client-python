from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.get_user_attributes_response_200_status import (
    GetUserAttributesResponse200Status,
)

if TYPE_CHECKING:
    from ..models.get_user_attributes_response_200_results_item import (
        GetUserAttributesResponse200ResultsItem,
    )


T = TypeVar("T", bound="GetUserAttributesResponse200")


@attr.s(auto_attribs=True)
class GetUserAttributesResponse200:
    """
    Attributes:
        results (List['GetUserAttributesResponse200ResultsItem']):
        status (GetUserAttributesResponse200Status):
    """

    results: List["GetUserAttributesResponse200ResultsItem"]
    status: GetUserAttributesResponse200Status
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
        from ..models.get_user_attributes_response_200_results_item import (
            GetUserAttributesResponse200ResultsItem,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = GetUserAttributesResponse200ResultsItem.from_dict(results_item_data)

            results.append(results_item)

        status = GetUserAttributesResponse200Status(d.pop("status"))

        get_user_attributes_response_200 = cls(
            results=results,
            status=status,
        )

        get_user_attributes_response_200.additional_properties = d
        return get_user_attributes_response_200

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
