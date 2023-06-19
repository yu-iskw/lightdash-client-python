from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.organization_member_role import OrganizationMemberRole

T = TypeVar("T", bound="PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid")


@attr.s(auto_attribs=True)
class PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        email_domains (List[str]):
        role (OrganizationMemberRole):
        project_uuids (List[str]):
    """

    email_domains: List[str]
    role: OrganizationMemberRole
    project_uuids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_domains = self.email_domains

        role = self.role.value

        project_uuids = self.project_uuids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailDomains": email_domains,
                "role": role,
                "projectUuids": project_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email_domains = cast(List[str], d.pop("emailDomains"))

        role = OrganizationMemberRole(d.pop("role"))

        project_uuids = cast(List[str], d.pop("projectUuids"))

        pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid = cls(
            email_domains=email_domains,
            role=role,
            project_uuids=project_uuids,
        )

        pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid.additional_properties = d
        return pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid

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
