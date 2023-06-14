from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

from ..models.resource_view_item_type import ResourceViewItemType

if TYPE_CHECKING:
    from ..models.pick_resource_view_item_at_data_uuid_or_pinned_list_order import (
        PickResourceViewItemAtDataUuidOrPinnedListOrder,
    )


T = TypeVar("T", bound="UpdatePinnedItemOrder")


@attr.s(auto_attribs=True)
class UpdatePinnedItemOrder:
    """
    Attributes:
        data (PickResourceViewItemAtDataUuidOrPinnedListOrder): From T, pick a set of properties whose keys are in the
            union K
        type (ResourceViewItemType):
    """

    data: "PickResourceViewItemAtDataUuidOrPinnedListOrder"
    type: ResourceViewItemType
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
        from ..models.pick_resource_view_item_at_data_uuid_or_pinned_list_order import (
            PickResourceViewItemAtDataUuidOrPinnedListOrder,
        )

        d = src_dict.copy()
        data = PickResourceViewItemAtDataUuidOrPinnedListOrder.from_dict(d.pop("data"))

        type = ResourceViewItemType(d.pop("type"))

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
