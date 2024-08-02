from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_member_role import OrganizationMemberRole
from ..models.project_member_role import ProjectMemberRole
from ..models.space_member_role import SpaceMemberRole
from ..models.space_share_inherited_from import SpaceShareInheritedFrom
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpaceShare")


@_attrs_define
class SpaceShare:
    """
    Attributes:
        has_direct_access (bool):
        role (SpaceMemberRole):
        email (str):
        last_name (str):
        first_name (str):
        user_uuid (str):
        inherited_from (Union[Unset, SpaceShareInheritedFrom]):
        inherited_role (Union[OrganizationMemberRole, ProjectMemberRole, Unset]):
    """

    has_direct_access: bool
    role: SpaceMemberRole
    email: str
    last_name: str
    first_name: str
    user_uuid: str
    inherited_from: Union[Unset, SpaceShareInheritedFrom] = UNSET
    inherited_role: Union[OrganizationMemberRole, ProjectMemberRole, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_direct_access = self.has_direct_access

        role = self.role.value

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        user_uuid = self.user_uuid

        inherited_from: Union[Unset, str] = UNSET
        if not isinstance(self.inherited_from, Unset):
            inherited_from = self.inherited_from.value

        inherited_role: Union[Unset, str]
        if isinstance(self.inherited_role, Unset):
            inherited_role = UNSET
        elif isinstance(self.inherited_role, OrganizationMemberRole):
            inherited_role = self.inherited_role.value
        else:
            inherited_role = self.inherited_role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasDirectAccess": has_direct_access,
                "role": role,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "userUuid": user_uuid,
            }
        )
        if inherited_from is not UNSET:
            field_dict["inheritedFrom"] = inherited_from
        if inherited_role is not UNSET:
            field_dict["inheritedRole"] = inherited_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_direct_access = d.pop("hasDirectAccess")

        role = SpaceMemberRole(d.pop("role"))

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        user_uuid = d.pop("userUuid")

        _inherited_from = d.pop("inheritedFrom", UNSET)
        inherited_from: Union[Unset, SpaceShareInheritedFrom]
        if isinstance(_inherited_from, Unset):
            inherited_from = UNSET
        else:
            inherited_from = SpaceShareInheritedFrom(_inherited_from)

        def _parse_inherited_role(data: object) -> Union[OrganizationMemberRole, ProjectMemberRole, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inherited_role_type_0 = OrganizationMemberRole(data)

                return inherited_role_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            inherited_role_type_1 = ProjectMemberRole(data)

            return inherited_role_type_1

        inherited_role = _parse_inherited_role(d.pop("inheritedRole", UNSET))

        space_share = cls(
            has_direct_access=has_direct_access,
            role=role,
            email=email,
            last_name=last_name,
            first_name=first_name,
            user_uuid=user_uuid,
            inherited_from=inherited_from,
            inherited_role=inherited_role,
        )

        space_share.additional_properties = d
        return space_share

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
