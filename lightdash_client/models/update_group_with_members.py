from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_group_member_user_uuid import PickGroupMemberUserUuid


T = TypeVar("T", bound="UpdateGroupWithMembers")


@_attrs_define
class UpdateGroupWithMembers:
    """
    Attributes:
        members (Union[Unset, List['PickGroupMemberUserUuid']]):
        name (Union[Unset, str]):
    """

    members: Union[Unset, List["PickGroupMemberUserUuid"]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_group_member_user_uuid import PickGroupMemberUserUuid

        d = src_dict.copy()
        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = PickGroupMemberUserUuid.from_dict(members_item_data)

            members.append(members_item)

        name = d.pop("name", UNSET)

        update_group_with_members = cls(
            members=members,
            name=name,
        )

        update_group_with_members.additional_properties = d
        return update_group_with_members

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
