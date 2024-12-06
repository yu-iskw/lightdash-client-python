import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_member import GroupMember


T = TypeVar("T", bound="GroupWithMembers")


@_attrs_define
class GroupWithMembers:
    """Details for a group including a list of the group's members.

    Attributes:
        organization_uuid (str): The UUID of the organization that the group belongs to
        updated_by_user_uuid (Union[None, str]): The UUID of the user that last updated the group
        updated_at (datetime.datetime): The time that the group was last updated
        created_by_user_uuid (Union[None, str]): The UUID of the user that created the group
        created_at (datetime.datetime): The time that the group was created
        name (str): A friendly name for the group
        uuid (str): The group's UUID
        member_uuids (List[str]):
        members (List['GroupMember']): A list of the group's members.
    """

    organization_uuid: str
    updated_by_user_uuid: Union[None, str]
    updated_at: datetime.datetime
    created_by_user_uuid: Union[None, str]
    created_at: datetime.datetime
    name: str
    uuid: str
    member_uuids: List[str]
    members: List["GroupMember"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group_member import GroupMember

        organization_uuid = self.organization_uuid

        updated_by_user_uuid: Union[None, str]
        updated_by_user_uuid = self.updated_by_user_uuid

        updated_at = self.updated_at.isoformat()

        created_by_user_uuid: Union[None, str]
        created_by_user_uuid = self.created_by_user_uuid

        created_at = self.created_at.isoformat()

        name = self.name

        uuid = self.uuid

        member_uuids = self.member_uuids

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationUuid": organization_uuid,
                "updatedByUserUuid": updated_by_user_uuid,
                "updatedAt": updated_at,
                "createdByUserUuid": created_by_user_uuid,
                "createdAt": created_at,
                "name": name,
                "uuid": uuid,
                "memberUuids": member_uuids,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_member import GroupMember

        d = src_dict.copy()
        organization_uuid = d.pop("organizationUuid")

        def _parse_updated_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_user_uuid = _parse_updated_by_user_uuid(d.pop("updatedByUserUuid"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_created_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_uuid = _parse_created_by_user_uuid(d.pop("createdByUserUuid"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        uuid = d.pop("uuid")

        member_uuids = cast(List[str], d.pop("memberUuids"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = GroupMember.from_dict(members_item_data)

            members.append(members_item)

        group_with_members = cls(
            organization_uuid=organization_uuid,
            updated_by_user_uuid=updated_by_user_uuid,
            updated_at=updated_at,
            created_by_user_uuid=created_by_user_uuid,
            created_at=created_at,
            name=name,
            uuid=uuid,
            member_uuids=member_uuids,
            members=members,
        )

        group_with_members.additional_properties = d
        return group_with_members

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
