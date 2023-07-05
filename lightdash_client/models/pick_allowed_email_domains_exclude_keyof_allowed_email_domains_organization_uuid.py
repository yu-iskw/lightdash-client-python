from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_role_type_0 import (
    PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0,
)
from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_role_type_1 import (
    PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1,
)
from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_role_type_2 import (
    PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2,
)
from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_role_type_3 import (
    PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType3,
)

if TYPE_CHECKING:
    from ..models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid_projects_item import (
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem,
    )


T = TypeVar("T", bound="PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid")


@attr.s(auto_attribs=True)
class PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        email_domains (List[str]):
        role (Union[PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType3]):
        projects (List['PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem']):
    """

    email_domains: List[str]
    role: Union[
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0,
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1,
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2,
        PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType3,
    ]
    projects: List["PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidProjectsItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_domains = self.email_domains

        role: str

        if isinstance(self.role, PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0):
            role = self.role.value

        elif isinstance(self.role, PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1):
            role = self.role.value

        elif isinstance(self.role, PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2):
            role = self.role.value

        else:
            role = self.role.value

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()

            projects.append(projects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailDomains": email_domains,
                "role": role,
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
        email_domains = cast(List[str], d.pop("emailDomains"))

        def _parse_role(
            data: object,
        ) -> Union[
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2,
            PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType3,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2 = PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType2(data)

                return role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_3 = PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuidRoleType3(data)

            return role_type_3

        role = _parse_role(d.pop("role"))

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
            email_domains=email_domains,
            role=role,
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
