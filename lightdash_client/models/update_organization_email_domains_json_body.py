from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.update_organization_email_domains_json_body_role_type_0 import (
    UpdateOrganizationEmailDomainsJsonBodyRoleType0,
)
from ..models.update_organization_email_domains_json_body_role_type_1 import (
    UpdateOrganizationEmailDomainsJsonBodyRoleType1,
)
from ..models.update_organization_email_domains_json_body_role_type_2 import (
    UpdateOrganizationEmailDomainsJsonBodyRoleType2,
)
from ..models.update_organization_email_domains_json_body_role_type_3 import (
    UpdateOrganizationEmailDomainsJsonBodyRoleType3,
)

if TYPE_CHECKING:
    from ..models.update_organization_email_domains_json_body_projects_item import (
        UpdateOrganizationEmailDomainsJsonBodyProjectsItem,
    )


T = TypeVar("T", bound="UpdateOrganizationEmailDomainsJsonBody")


@attr.s(auto_attribs=True)
class UpdateOrganizationEmailDomainsJsonBody:
    """the new allowed email domains

    Attributes:
        email_domains (List[str]):
        role (Union[UpdateOrganizationEmailDomainsJsonBodyRoleType0, UpdateOrganizationEmailDomainsJsonBodyRoleType1,
            UpdateOrganizationEmailDomainsJsonBodyRoleType2, UpdateOrganizationEmailDomainsJsonBodyRoleType3]):
        projects (List['UpdateOrganizationEmailDomainsJsonBodyProjectsItem']):
    """

    email_domains: List[str]
    role: Union[
        UpdateOrganizationEmailDomainsJsonBodyRoleType0,
        UpdateOrganizationEmailDomainsJsonBodyRoleType1,
        UpdateOrganizationEmailDomainsJsonBodyRoleType2,
        UpdateOrganizationEmailDomainsJsonBodyRoleType3,
    ]
    projects: List["UpdateOrganizationEmailDomainsJsonBodyProjectsItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_domains = self.email_domains

        role: str

        if isinstance(self.role, UpdateOrganizationEmailDomainsJsonBodyRoleType0):
            role = self.role.value

        elif isinstance(self.role, UpdateOrganizationEmailDomainsJsonBodyRoleType1):
            role = self.role.value

        elif isinstance(self.role, UpdateOrganizationEmailDomainsJsonBodyRoleType2):
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
        from ..models.update_organization_email_domains_json_body_projects_item import (
            UpdateOrganizationEmailDomainsJsonBodyProjectsItem,
        )

        d = src_dict.copy()
        email_domains = cast(List[str], d.pop("emailDomains"))

        def _parse_role(
            data: object,
        ) -> Union[
            UpdateOrganizationEmailDomainsJsonBodyRoleType0,
            UpdateOrganizationEmailDomainsJsonBodyRoleType1,
            UpdateOrganizationEmailDomainsJsonBodyRoleType2,
            UpdateOrganizationEmailDomainsJsonBodyRoleType3,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = UpdateOrganizationEmailDomainsJsonBodyRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = UpdateOrganizationEmailDomainsJsonBodyRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2 = UpdateOrganizationEmailDomainsJsonBodyRoleType2(data)

                return role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_3 = UpdateOrganizationEmailDomainsJsonBodyRoleType3(data)

            return role_type_3

        role = _parse_role(d.pop("role"))

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = UpdateOrganizationEmailDomainsJsonBodyProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        update_organization_email_domains_json_body = cls(
            email_domains=email_domains,
            role=role,
            projects=projects,
        )

        update_organization_email_domains_json_body.additional_properties = d
        return update_organization_email_domains_json_body

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
