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
    from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_projects_item import (
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem,
    )


T = TypeVar("T", bound="PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid")


@_attrs_define
class PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        role (Union[OrganizationMemberRoleEDITOR, OrganizationMemberRoleINTERACTIVEVIEWER, OrganizationMemberRoleMEMBER,
            OrganizationMemberRoleVIEWER]):
        email_domains (List[str]):
        projects (List['PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem']):
    """

    role: Union[
        OrganizationMemberRoleEDITOR,
        OrganizationMemberRoleINTERACTIVEVIEWER,
        OrganizationMemberRoleMEMBER,
        OrganizationMemberRoleVIEWER,
    ]
    email_domains: List[str]
    projects: List["PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "emailDomains": email_domains,
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_projects_item import (
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem,
        )

        d = src_dict.copy()

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

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = (
                PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem.from_dict(
                    projects_item_data
                )
            )

            projects.append(projects_item)

        pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid = cls(
            role=role,
            email_domains=email_domains,
            projects=projects,
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
