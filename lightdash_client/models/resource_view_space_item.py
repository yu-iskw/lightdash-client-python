from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_view_item_type_space import ResourceViewItemTypeSPACE

if TYPE_CHECKING:
    from ..models.resource_view_space_item_data import ResourceViewSpaceItemData


T = TypeVar("T", bound="ResourceViewSpaceItem")


@_attrs_define
class ResourceViewSpaceItem:
    """
    Attributes:
        data (ResourceViewSpaceItemData):
        type (ResourceViewItemTypeSPACE):
    """

    data: "ResourceViewSpaceItemData"
    type: ResourceViewItemTypeSPACE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.resource_view_space_item_data import ResourceViewSpaceItemData

        d = src_dict.copy()
        data = ResourceViewSpaceItemData.from_dict(d.pop("data"))

        type = ResourceViewItemTypeSPACE(d.pop("type"))

        resource_view_space_item = cls(
            data=data,
            type=type,
        )

        resource_view_space_item.additional_properties = d
        return resource_view_space_item

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
