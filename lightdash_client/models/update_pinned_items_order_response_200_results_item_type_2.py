from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.update_pinned_items_order_response_200_results_item_type_2_type import (
    UpdatePinnedItemsOrderResponse200ResultsItemType2Type,
)

if TYPE_CHECKING:
    from ..models.update_pinned_items_order_response_200_results_item_type_2_data import (
        UpdatePinnedItemsOrderResponse200ResultsItemType2Data,
    )


T = TypeVar("T", bound="UpdatePinnedItemsOrderResponse200ResultsItemType2")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderResponse200ResultsItemType2:
    """
    Attributes:
        data (UpdatePinnedItemsOrderResponse200ResultsItemType2Data):
        type (UpdatePinnedItemsOrderResponse200ResultsItemType2Type):
    """

    data: "UpdatePinnedItemsOrderResponse200ResultsItemType2Data"
    type: UpdatePinnedItemsOrderResponse200ResultsItemType2Type
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
        from ..models.update_pinned_items_order_response_200_results_item_type_2_data import (
            UpdatePinnedItemsOrderResponse200ResultsItemType2Data,
        )

        d = src_dict.copy()
        data = UpdatePinnedItemsOrderResponse200ResultsItemType2Data.from_dict(d.pop("data"))

        type = UpdatePinnedItemsOrderResponse200ResultsItemType2Type(d.pop("type"))

        update_pinned_items_order_response_200_results_item_type_2 = cls(
            data=data,
            type=type,
        )

        update_pinned_items_order_response_200_results_item_type_2.additional_properties = d
        return update_pinned_items_order_response_200_results_item_type_2

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
