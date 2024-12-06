from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_icon import CustomIcon
    from ..models.emoji_icon import EmojiIcon


T = TypeVar("T", bound="UpdateCatalogItemIconBody")


@_attrs_define
class UpdateCatalogItemIconBody:
    """
    Attributes:
        icon (Union['CustomIcon', 'EmojiIcon', None]):
    """

    icon: Union["CustomIcon", "EmojiIcon", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon

        icon: Union[Dict[str, Any], None]
        if isinstance(self.icon, EmojiIcon):
            icon = self.icon.to_dict()
        elif isinstance(self.icon, CustomIcon):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon

        d = src_dict.copy()

        def _parse_icon(data: object) -> Union["CustomIcon", "EmojiIcon", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_catalog_item_icon_type_0 = EmojiIcon.from_dict(data)

                return componentsschemas_catalog_item_icon_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_catalog_item_icon_type_1 = CustomIcon.from_dict(data)

                return componentsschemas_catalog_item_icon_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomIcon", "EmojiIcon", None], data)

        icon = _parse_icon(d.pop("icon"))

        update_catalog_item_icon_body = cls(
            icon=icon,
        )

        update_catalog_item_icon_body.additional_properties = d
        return update_catalog_item_icon_body

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
