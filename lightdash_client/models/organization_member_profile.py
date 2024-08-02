from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_member_role import OrganizationMemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationMemberProfile")


@_attrs_define
class OrganizationMemberProfile:
    """Profile for a user's membership in an organization

    Attributes:
        is_active (bool): Whether the user has accepted their invite to the organization
        role (OrganizationMemberRole):
        organization_uuid (str): Unique identifier for the organization the user is a member of
        email (str):
        last_name (str):
        first_name (str):
        user_uuid (str): Unique identifier for the user
        is_invite_expired (Union[Unset, bool]): Whether the user's invite to the organization has expired
    """

    is_active: bool
    role: OrganizationMemberRole
    organization_uuid: str
    email: str
    last_name: str
    first_name: str
    user_uuid: str
    is_invite_expired: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_active = self.is_active

        role = self.role.value

        organization_uuid = self.organization_uuid

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        user_uuid = self.user_uuid

        is_invite_expired = self.is_invite_expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isActive": is_active,
                "role": role,
                "organizationUuid": organization_uuid,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "userUuid": user_uuid,
            }
        )
        if is_invite_expired is not UNSET:
            field_dict["isInviteExpired"] = is_invite_expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("isActive")

        role = OrganizationMemberRole(d.pop("role"))

        organization_uuid = d.pop("organizationUuid")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        user_uuid = d.pop("userUuid")

        is_invite_expired = d.pop("isInviteExpired", UNSET)

        organization_member_profile = cls(
            is_active=is_active,
            role=role,
            organization_uuid=organization_uuid,
            email=email,
            last_name=last_name,
            first_name=first_name,
            user_uuid=user_uuid,
            is_invite_expired=is_invite_expired,
        )

        organization_member_profile.additional_properties = d
        return organization_member_profile

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
