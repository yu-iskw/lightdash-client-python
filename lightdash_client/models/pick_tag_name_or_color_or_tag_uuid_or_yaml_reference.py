from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickTagNameOrColorOrTagUuidOrYamlReference")


@_attrs_define
class PickTagNameOrColorOrTagUuidOrYamlReference:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        color (str):
        tag_uuid (str):
        yaml_reference (Union[None, str]):
    """

    name: str
    color: str
    tag_uuid: str
    yaml_reference: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        color = self.color

        tag_uuid = self.tag_uuid

        yaml_reference: Union[None, str]
        yaml_reference = self.yaml_reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "color": color,
                "tagUuid": tag_uuid,
                "yamlReference": yaml_reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = d.pop("color")

        tag_uuid = d.pop("tagUuid")

        def _parse_yaml_reference(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        yaml_reference = _parse_yaml_reference(d.pop("yamlReference"))

        pick_tag_name_or_color_or_tag_uuid_or_yaml_reference = cls(
            name=name,
            color=color,
            tag_uuid=tag_uuid,
            yaml_reference=yaml_reference,
        )

        pick_tag_name_or_color_or_tag_uuid_or_yaml_reference.additional_properties = d
        return pick_tag_name_or_color_or_tag_uuid_or_yaml_reference

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
