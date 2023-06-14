from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.organization_member_role import OrganizationMemberRole

T = TypeVar("T", bound="AllowedEmailDomains")


@attr.s(auto_attribs=True)
class AllowedEmailDomains:
    """
    Attributes:
        project_uuids (List[str]):
        role (OrganizationMemberRole):
        email_domains (List[str]):
        organization_uuid (str):
    """

    project_uuids: List[str]
    role: OrganizationMemberRole
    email_domains: List[str]
    organization_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_uuids = self.project_uuids

        role = self.role.value

        email_domains = self.email_domains

        organization_uuid = self.organization_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectUuids": project_uuids,
                "role": role,
                "emailDomains": email_domains,
                "organizationUuid": organization_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_uuids = cast(List[str], d.pop("projectUuids"))

        role = OrganizationMemberRole(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        organization_uuid = d.pop("organizationUuid")

        allowed_email_domains = cls(
            project_uuids=project_uuids,
            role=role,
            email_domains=email_domains,
            organization_uuid=organization_uuid,
        )

        allowed_email_domains.additional_properties = d
        return allowed_email_domains

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
