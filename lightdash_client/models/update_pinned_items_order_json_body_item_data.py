from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdatePinnedItemsOrderJsonBodyItemData")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderJsonBodyItemData:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        uuid (str):
        pinned_list_order (Optional[float]):
    """

    uuid: str
    pinned_list_order: Optional[float]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        pinned_list_order = self.pinned_list_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "pinnedListOrder": pinned_list_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        pinned_list_order = d.pop("pinnedListOrder")

        update_pinned_items_order_json_body_item_data = cls(
            uuid=uuid,
            pinned_list_order=pinned_list_order,
        )

        update_pinned_items_order_json_body_item_data.additional_properties = d
        return update_pinned_items_order_json_body_item_data

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
