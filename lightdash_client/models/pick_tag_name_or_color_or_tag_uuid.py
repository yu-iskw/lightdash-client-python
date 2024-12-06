from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickTagNameOrColorOrTagUuid")


@_attrs_define
class PickTagNameOrColorOrTagUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        color (str):
        tag_uuid (str):
    """

    name: str
    color: str
    tag_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        color = self.color

        tag_uuid = self.tag_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "color": color,
                "tagUuid": tag_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = d.pop("color")

        tag_uuid = d.pop("tagUuid")

        pick_tag_name_or_color_or_tag_uuid = cls(
            name=name,
            color=color,
            tag_uuid=tag_uuid,
        )

        pick_tag_name_or_color_or_tag_uuid.additional_properties = d
        return pick_tag_name_or_color_or_tag_uuid

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
