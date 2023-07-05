from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.update_organization_email_domains_response_200_results_role_type_0 import (
    UpdateOrganizationEmailDomainsResponse200ResultsRoleType0,
)
from ..models.update_organization_email_domains_response_200_results_role_type_1 import (
    UpdateOrganizationEmailDomainsResponse200ResultsRoleType1,
)
from ..models.update_organization_email_domains_response_200_results_role_type_2 import (
    UpdateOrganizationEmailDomainsResponse200ResultsRoleType2,
)
from ..models.update_organization_email_domains_response_200_results_role_type_3 import (
    UpdateOrganizationEmailDomainsResponse200ResultsRoleType3,
)

if TYPE_CHECKING:
    from ..models.update_organization_email_domains_response_200_results_projects_item import (
        UpdateOrganizationEmailDomainsResponse200ResultsProjectsItem,
    )


T = TypeVar("T", bound="UpdateOrganizationEmailDomainsResponse200Results")


@attr.s(auto_attribs=True)
class UpdateOrganizationEmailDomainsResponse200Results:
    """
    Attributes:
        projects (List['UpdateOrganizationEmailDomainsResponse200ResultsProjectsItem']):
        role (Union[UpdateOrganizationEmailDomainsResponse200ResultsRoleType0,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType1,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType2,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType3]):
        email_domains (List[str]):
        organization_uuid (str):
    """

    projects: List["UpdateOrganizationEmailDomainsResponse200ResultsProjectsItem"]
    role: Union[
        UpdateOrganizationEmailDomainsResponse200ResultsRoleType0,
        UpdateOrganizationEmailDomainsResponse200ResultsRoleType1,
        UpdateOrganizationEmailDomainsResponse200ResultsRoleType2,
        UpdateOrganizationEmailDomainsResponse200ResultsRoleType3,
    ]
    email_domains: List[str]
    organization_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()

            projects.append(projects_item)

        role: str

        if isinstance(self.role, UpdateOrganizationEmailDomainsResponse200ResultsRoleType0):
            role = self.role.value

        elif isinstance(self.role, UpdateOrganizationEmailDomainsResponse200ResultsRoleType1):
            role = self.role.value

        elif isinstance(self.role, UpdateOrganizationEmailDomainsResponse200ResultsRoleType2):
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
        from ..models.update_organization_email_domains_response_200_results_projects_item import (
            UpdateOrganizationEmailDomainsResponse200ResultsProjectsItem,
        )

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = UpdateOrganizationEmailDomainsResponse200ResultsProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        def _parse_role(
            data: object,
        ) -> Union[
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType0,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType1,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType2,
            UpdateOrganizationEmailDomainsResponse200ResultsRoleType3,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = UpdateOrganizationEmailDomainsResponse200ResultsRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = UpdateOrganizationEmailDomainsResponse200ResultsRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2 = UpdateOrganizationEmailDomainsResponse200ResultsRoleType2(data)

                return role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_3 = UpdateOrganizationEmailDomainsResponse200ResultsRoleType3(data)

            return role_type_3

        role = _parse_role(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        organization_uuid = d.pop("organizationUuid")

        update_organization_email_domains_response_200_results = cls(
            projects=projects,
            role=role,
            email_domains=email_domains,
            organization_uuid=organization_uuid,
        )

        update_organization_email_domains_response_200_results.additional_properties = d
        return update_organization_email_domains_response_200_results

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
