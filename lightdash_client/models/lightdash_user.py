import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.organization_member_role import OrganizationMemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="LightdashUser")


@_attrs_define
class LightdashUser:
    """
    Attributes:
        user_uuid (str):
        first_name (str):
        last_name (str):
        is_tracking_anonymized (bool):
        is_marketing_opted_in (bool):
        is_setup_complete (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_active (bool): Whether the user can login
        email (Union[Unset, str]):
        organization_uuid (Union[Unset, str]):
        organization_name (Union[Unset, str]):
        organization_created_at (Union[Unset, datetime.datetime]):
        role (Union[Unset, OrganizationMemberRole]):
        is_pending (Union[Unset, bool]): Whether the user doesn't have an authentication method (password or openId)
    """

    user_uuid: str
    first_name: str
    last_name: str
    is_tracking_anonymized: bool
    is_marketing_opted_in: bool
    is_setup_complete: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_active: bool
    email: Union[Unset, str] = UNSET
    organization_uuid: Union[Unset, str] = UNSET
    organization_name: Union[Unset, str] = UNSET
    organization_created_at: Union[Unset, datetime.datetime] = UNSET
    role: Union[Unset, OrganizationMemberRole] = UNSET
    is_pending: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid

        first_name = self.first_name

        last_name = self.last_name

        is_tracking_anonymized = self.is_tracking_anonymized

        is_marketing_opted_in = self.is_marketing_opted_in

        is_setup_complete = self.is_setup_complete

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_active = self.is_active

        email = self.email

        organization_uuid = self.organization_uuid

        organization_name = self.organization_name

        organization_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.organization_created_at, Unset):
            organization_created_at = self.organization_created_at.isoformat()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        is_pending = self.is_pending

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "firstName": first_name,
                "lastName": last_name,
                "isTrackingAnonymized": is_tracking_anonymized,
                "isMarketingOptedIn": is_marketing_opted_in,
                "isSetupComplete": is_setup_complete,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "isActive": is_active,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if organization_uuid is not UNSET:
            field_dict["organizationUuid"] = organization_uuid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if organization_created_at is not UNSET:
            field_dict["organizationCreatedAt"] = organization_created_at
        if role is not UNSET:
            field_dict["role"] = role
        if is_pending is not UNSET:
            field_dict["isPending"] = is_pending

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        is_tracking_anonymized = d.pop("isTrackingAnonymized")

        is_marketing_opted_in = d.pop("isMarketingOptedIn")

        is_setup_complete = d.pop("isSetupComplete")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        is_active = d.pop("isActive")

        email = d.pop("email", UNSET)

        organization_uuid = d.pop("organizationUuid", UNSET)

        organization_name = d.pop("organizationName", UNSET)

        _organization_created_at = d.pop("organizationCreatedAt", UNSET)
        organization_created_at: Union[Unset, datetime.datetime]
        if isinstance(_organization_created_at, Unset):
            organization_created_at = UNSET
        else:
            organization_created_at = isoparse(_organization_created_at)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrganizationMemberRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrganizationMemberRole(_role)

        is_pending = d.pop("isPending", UNSET)

        lightdash_user = cls(
            user_uuid=user_uuid,
            first_name=first_name,
            last_name=last_name,
            is_tracking_anonymized=is_tracking_anonymized,
            is_marketing_opted_in=is_marketing_opted_in,
            is_setup_complete=is_setup_complete,
            created_at=created_at,
            updated_at=updated_at,
            is_active=is_active,
            email=email,
            organization_uuid=organization_uuid,
            organization_name=organization_name,
            organization_created_at=organization_created_at,
            role=role,
            is_pending=is_pending,
        )

        lightdash_user.additional_properties = d
        return lightdash_user

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
