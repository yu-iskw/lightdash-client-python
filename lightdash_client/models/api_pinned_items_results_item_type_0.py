from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_pinned_items_results_item_type_0_type import (
    ApiPinnedItemsResultsItemType0Type,
)

if TYPE_CHECKING:
    from ..models.api_pinned_items_results_item_type_0_data import (
        ApiPinnedItemsResultsItemType0Data,
    )


T = TypeVar("T", bound="ApiPinnedItemsResultsItemType0")


@attr.s(auto_attribs=True)
class ApiPinnedItemsResultsItemType0:
    """
    Attributes:
        data (ApiPinnedItemsResultsItemType0Data): From T, pick a set of properties whose keys are in the union K
        type (ApiPinnedItemsResultsItemType0Type):
    """

    data: "ApiPinnedItemsResultsItemType0Data"
    type: ApiPinnedItemsResultsItemType0Type
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_pinned_items_results_item_type_0_data import (
            ApiPinnedItemsResultsItemType0Data,
        )

        d = src_dict.copy()
        data = ApiPinnedItemsResultsItemType0Data.from_dict(d.pop("data"))

        type = ApiPinnedItemsResultsItemType0Type(d.pop("type"))

        api_pinned_items_results_item_type_0 = cls(
            data=data,
            type=type,
        )

        api_pinned_items_results_item_type_0.additional_properties = d
        return api_pinned_items_results_item_type_0

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
