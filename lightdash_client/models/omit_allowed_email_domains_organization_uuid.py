from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.omit_allowed_email_domains_organization_uuid_role import OmitAllowedEmailDomainsOrganizationUuidRole

T = TypeVar("T", bound="OmitAllowedEmailDomainsOrganizationUuid")


@attr.s(auto_attribs=True)
class OmitAllowedEmailDomainsOrganizationUuid:
    """Construct a type with the properties of T except for those in type K.

    Attributes:
        role (OmitAllowedEmailDomainsOrganizationUuidRole):
        email_domains (List[str]):
        project_uuids (List[str]):
    """

    role: OmitAllowedEmailDomainsOrganizationUuidRole
    email_domains: List[str]
    project_uuids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        email_domains = self.email_domains

        project_uuids = self.project_uuids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "emailDomains": email_domains,
                "projectUuids": project_uuids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = OmitAllowedEmailDomainsOrganizationUuidRole(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        project_uuids = cast(List[str], d.pop("projectUuids"))

        omit_allowed_email_domains_organization_uuid = cls(
            role=role,
            email_domains=email_domains,
            project_uuids=project_uuids,
        )

        omit_allowed_email_domains_organization_uuid.additional_properties = d
        return omit_allowed_email_domains_organization_uuid

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