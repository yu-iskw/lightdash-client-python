from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_group_member_user_uuid import PickGroupMemberUserUuid


T = TypeVar("T", bound="CreateGroup")


@_attrs_define
class CreateGroup:
    """
    Attributes:
        name (str): A friendly name for the group
        members (Union[Unset, List['PickGroupMemberUserUuid']]):
    """

    name: str
    members: Union[Unset, List["PickGroupMemberUserUuid"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_group_member_user_uuid import PickGroupMemberUserUuid

        d = src_dict.copy()
        name = d.pop("name")

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = PickGroupMemberUserUuid.from_dict(members_item_data)

            members.append(members_item)

        create_group = cls(
            name=name,
            members=members,
        )

        create_group.additional_properties = d
        return create_group

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
