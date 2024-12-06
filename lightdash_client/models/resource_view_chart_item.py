from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_item_category import ResourceItemCategory
from ..models.resource_view_item_type_chart import ResourceViewItemTypeCHART
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_view_chart_item_data import ResourceViewChartItemData


T = TypeVar("T", bound="ResourceViewChartItem")


@_attrs_define
class ResourceViewChartItem:
    """
    Attributes:
        data (ResourceViewChartItemData):
        type (ResourceViewItemTypeCHART):
        category (Union[Unset, ResourceItemCategory]):
    """

    data: "ResourceViewChartItemData"
    type: ResourceViewItemTypeCHART
    category: Union[Unset, ResourceItemCategory] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.resource_view_chart_item_data import ResourceViewChartItemData

        data = self.data.to_dict()

        type = self.type.value

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource_view_chart_item_data import ResourceViewChartItemData

        d = src_dict.copy()
        data = ResourceViewChartItemData.from_dict(d.pop("data"))

        type = ResourceViewItemTypeCHART(d.pop("type"))

        _category = d.pop("category", UNSET)
        category: Union[Unset, ResourceItemCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ResourceItemCategory(_category)

        resource_view_chart_item = cls(
            data=data,
            type=type,
            category=category,
        )

        resource_view_chart_item.additional_properties = d
        return resource_view_chart_item

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
