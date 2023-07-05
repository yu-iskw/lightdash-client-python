from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.update_pinned_item_order_type import UpdatePinnedItemOrderType

if TYPE_CHECKING:
    from ..models.update_pinned_item_order_data import UpdatePinnedItemOrderData


T = TypeVar("T", bound="UpdatePinnedItemOrder")


@attr.s(auto_attribs=True)
class UpdatePinnedItemOrder:
    """
    Attributes:
        data (UpdatePinnedItemOrderData): From T, pick a set of properties whose keys are in the union K
        type (UpdatePinnedItemOrderType):
    """

    data: "UpdatePinnedItemOrderData"
    type: UpdatePinnedItemOrderType
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
        from ..models.update_pinned_item_order_data import UpdatePinnedItemOrderData

        d = src_dict.copy()
        data = UpdatePinnedItemOrderData.from_dict(d.pop("data"))

        type = UpdatePinnedItemOrderType(d.pop("type"))

        update_pinned_item_order = cls(
            data=data,
            type=type,
        )

        update_pinned_item_order.additional_properties = d
        return update_pinned_item_order

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
