from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_member_role_editor import OrganizationMemberRoleEDITOR
from ..models.organization_member_role_interactiveviewer import (
    OrganizationMemberRoleINTERACTIVEVIEWER,
)
from ..models.organization_member_role_member import OrganizationMemberRoleMEMBER
from ..models.organization_member_role_viewer import OrganizationMemberRoleVIEWER

if TYPE_CHECKING:
    from ..models.allowed_email_domains_projects_item import (
        AllowedEmailDomainsProjectsItem,
    )


T = TypeVar("T", bound="AllowedEmailDomains")


@_attrs_define
class AllowedEmailDomains:
    """
    Attributes:
        projects (List['AllowedEmailDomainsProjectsItem']):
        role (Union[OrganizationMemberRoleEDITOR, OrganizationMemberRoleINTERACTIVEVIEWER, OrganizationMemberRoleMEMBER,
            OrganizationMemberRoleVIEWER]):
        email_domains (List[str]):
        organization_uuid (str):
    """

    projects: List["AllowedEmailDomainsProjectsItem"]
    role: Union[
        OrganizationMemberRoleEDITOR,
        OrganizationMemberRoleINTERACTIVEVIEWER,
        OrganizationMemberRoleMEMBER,
        OrganizationMemberRoleVIEWER,
    ]
    email_domains: List[str]
    organization_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        role: str
        if isinstance(self.role, OrganizationMemberRoleEDITOR):
            role = self.role.value
        elif isinstance(self.role, OrganizationMemberRoleINTERACTIVEVIEWER):
            role = self.role.value
        elif isinstance(self.role, OrganizationMemberRoleVIEWER):
            role = self.role.value
        else:
            role = self.role.value

        email_domains = self.email_domains

        organization_uuid = self.organization_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
                "role": role,
                "emailDomains": email_domains,
                "organizationUuid": organization_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.allowed_email_domains_projects_item import (
            AllowedEmailDomainsProjectsItem,
        )

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = AllowedEmailDomainsProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        def _parse_role(
            data: object,
        ) -> Union[
            OrganizationMemberRoleEDITOR,
            OrganizationMemberRoleINTERACTIVEVIEWER,
            OrganizationMemberRoleMEMBER,
            OrganizationMemberRoleVIEWER,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_allowed_email_domains_role_type_0 = OrganizationMemberRoleEDITOR(data)

                return componentsschemas_allowed_email_domains_role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_allowed_email_domains_role_type_1 = OrganizationMemberRoleINTERACTIVEVIEWER(data)

                return componentsschemas_allowed_email_domains_role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_allowed_email_domains_role_type_2 = OrganizationMemberRoleVIEWER(data)

                return componentsschemas_allowed_email_domains_role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_allowed_email_domains_role_type_3 = OrganizationMemberRoleMEMBER(data)

            return componentsschemas_allowed_email_domains_role_type_3

        role = _parse_role(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        organization_uuid = d.pop("organizationUuid")

        allowed_email_domains = cls(
            projects=projects,
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
