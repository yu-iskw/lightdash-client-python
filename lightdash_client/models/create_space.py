from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_space_share_user_uuid_or_role import PickSpaceShareUserUuidOrRole


T = TypeVar("T", bound="CreateSpace")


@_attrs_define
class CreateSpace:
    """
    Attributes:
        name (str):
        access (Union[Unset, List['PickSpaceShareUserUuidOrRole']]):
        is_private (Union[Unset, bool]):
    """

    name: str
    access: Union[Unset, List["PickSpaceShareUserUuidOrRole"]] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            access = []
            for access_item_data in self.access:
                access_item = access_item_data.to_dict()
                access.append(access_item)

        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_space_share_user_uuid_or_role import (
            PickSpaceShareUserUuidOrRole,
        )

        d = src_dict.copy()
        name = d.pop("name")

        access = []
        _access = d.pop("access", UNSET)
        for access_item_data in _access or []:
            access_item = PickSpaceShareUserUuidOrRole.from_dict(access_item_data)

            access.append(access_item)

        is_private = d.pop("isPrivate", UNSET)

        create_space = cls(
            name=name,
            access=access,
            is_private=is_private,
        )

        create_space.additional_properties = d
        return create_space

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
