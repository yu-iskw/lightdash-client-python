from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_pinned_items_results_item_type_2_type import (
    ApiPinnedItemsResultsItemType2Type,
)

if TYPE_CHECKING:
    from ..models.api_pinned_items_results_item_type_2_data import (
        ApiPinnedItemsResultsItemType2Data,
    )


T = TypeVar("T", bound="ApiPinnedItemsResultsItemType2")


@attr.s(auto_attribs=True)
class ApiPinnedItemsResultsItemType2:
    """
    Attributes:
        data (ApiPinnedItemsResultsItemType2Data):
        type (ApiPinnedItemsResultsItemType2Type):
    """

    data: "ApiPinnedItemsResultsItemType2Data"
    type: ApiPinnedItemsResultsItemType2Type
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
        from ..models.api_pinned_items_results_item_type_2_data import (
            ApiPinnedItemsResultsItemType2Data,
        )

        d = src_dict.copy()
        data = ApiPinnedItemsResultsItemType2Data.from_dict(d.pop("data"))

        type = ApiPinnedItemsResultsItemType2Type(d.pop("type"))

        api_pinned_items_results_item_type_2 = cls(
            data=data,
            type=type,
        )

        api_pinned_items_results_item_type_2.additional_properties = d
        return api_pinned_items_results_item_type_2

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
