from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.update_pinned_items_order_response_200_results_item_type_1_type import (
    UpdatePinnedItemsOrderResponse200ResultsItemType1Type,
)

if TYPE_CHECKING:
    from ..models.update_pinned_items_order_response_200_results_item_type_1_data import (
        UpdatePinnedItemsOrderResponse200ResultsItemType1Data,
    )


T = TypeVar("T", bound="UpdatePinnedItemsOrderResponse200ResultsItemType1")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderResponse200ResultsItemType1:
    """
    Attributes:
        data (UpdatePinnedItemsOrderResponse200ResultsItemType1Data): From T, pick a set of properties whose keys are in
            the union K
        type (UpdatePinnedItemsOrderResponse200ResultsItemType1Type):
    """

    data: "UpdatePinnedItemsOrderResponse200ResultsItemType1Data"
    type: UpdatePinnedItemsOrderResponse200ResultsItemType1Type
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
        from ..models.update_pinned_items_order_response_200_results_item_type_1_data import (
            UpdatePinnedItemsOrderResponse200ResultsItemType1Data,
        )

        d = src_dict.copy()
        data = UpdatePinnedItemsOrderResponse200ResultsItemType1Data.from_dict(d.pop("data"))

        type = UpdatePinnedItemsOrderResponse200ResultsItemType1Type(d.pop("type"))

        update_pinned_items_order_response_200_results_item_type_1 = cls(
            data=data,
            type=type,
        )

        update_pinned_items_order_response_200_results_item_type_1.additional_properties = d
        return update_pinned_items_order_response_200_results_item_type_1

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
