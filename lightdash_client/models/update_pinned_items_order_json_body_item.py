from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.update_pinned_items_order_json_body_item_type import (
    UpdatePinnedItemsOrderJsonBodyItemType,
)

if TYPE_CHECKING:
    from ..models.update_pinned_items_order_json_body_item_data import (
        UpdatePinnedItemsOrderJsonBodyItemData,
    )


T = TypeVar("T", bound="UpdatePinnedItemsOrderJsonBodyItem")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderJsonBodyItem:
    """
    Attributes:
        data (UpdatePinnedItemsOrderJsonBodyItemData): From T, pick a set of properties whose keys are in the union K
        type (UpdatePinnedItemsOrderJsonBodyItemType):
    """

    data: "UpdatePinnedItemsOrderJsonBodyItemData"
    type: UpdatePinnedItemsOrderJsonBodyItemType
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
        from ..models.update_pinned_items_order_json_body_item_data import (
            UpdatePinnedItemsOrderJsonBodyItemData,
        )

        d = src_dict.copy()
        data = UpdatePinnedItemsOrderJsonBodyItemData.from_dict(d.pop("data"))

        type = UpdatePinnedItemsOrderJsonBodyItemType(d.pop("type"))

        update_pinned_items_order_json_body_item = cls(
            data=data,
            type=type,
        )

        update_pinned_items_order_json_body_item.additional_properties = d
        return update_pinned_items_order_json_body_item

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
