from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickDashboardUuidOrNameOrDescriptionOrSpaceUuid")


@_attrs_define
class PickDashboardUuidOrNameOrDescriptionOrSpaceUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        uuid (str):
        space_uuid (str):
        description (Union[Unset, str]):
    """

    name: str
    uuid: str
    space_uuid: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        uuid = self.uuid

        space_uuid = self.space_uuid

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "spaceUuid": space_uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        space_uuid = d.pop("spaceUuid")

        description = d.pop("description", UNSET)

        pick_dashboard_uuid_or_name_or_description_or_space_uuid = cls(
            name=name,
            uuid=uuid,
            space_uuid=space_uuid,
            description=description,
        )

        pick_dashboard_uuid_or_name_or_description_or_space_uuid.additional_properties = d
        return pick_dashboard_uuid_or_name_or_description_or_space_uuid

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
