from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.list_organization_email_domains_response_200_results_role_type_0 import (
    ListOrganizationEmailDomainsResponse200ResultsRoleType0,
)
from ..models.list_organization_email_domains_response_200_results_role_type_1 import (
    ListOrganizationEmailDomainsResponse200ResultsRoleType1,
)
from ..models.list_organization_email_domains_response_200_results_role_type_2 import (
    ListOrganizationEmailDomainsResponse200ResultsRoleType2,
)
from ..models.list_organization_email_domains_response_200_results_role_type_3 import (
    ListOrganizationEmailDomainsResponse200ResultsRoleType3,
)

if TYPE_CHECKING:
    from ..models.list_organization_email_domains_response_200_results_projects_item import (
        ListOrganizationEmailDomainsResponse200ResultsProjectsItem,
    )


T = TypeVar("T", bound="ListOrganizationEmailDomainsResponse200Results")


@attr.s(auto_attribs=True)
class ListOrganizationEmailDomainsResponse200Results:
    """
    Attributes:
        projects (List['ListOrganizationEmailDomainsResponse200ResultsProjectsItem']):
        role (Union[ListOrganizationEmailDomainsResponse200ResultsRoleType0,
            ListOrganizationEmailDomainsResponse200ResultsRoleType1,
            ListOrganizationEmailDomainsResponse200ResultsRoleType2,
            ListOrganizationEmailDomainsResponse200ResultsRoleType3]):
        email_domains (List[str]):
        organization_uuid (str):
    """

    projects: List["ListOrganizationEmailDomainsResponse200ResultsProjectsItem"]
    role: Union[
        ListOrganizationEmailDomainsResponse200ResultsRoleType0,
        ListOrganizationEmailDomainsResponse200ResultsRoleType1,
        ListOrganizationEmailDomainsResponse200ResultsRoleType2,
        ListOrganizationEmailDomainsResponse200ResultsRoleType3,
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

        if isinstance(self.role, ListOrganizationEmailDomainsResponse200ResultsRoleType0):
            role = self.role.value

        elif isinstance(self.role, ListOrganizationEmailDomainsResponse200ResultsRoleType1):
            role = self.role.value

        elif isinstance(self.role, ListOrganizationEmailDomainsResponse200ResultsRoleType2):
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
        from ..models.list_organization_email_domains_response_200_results_projects_item import (
            ListOrganizationEmailDomainsResponse200ResultsProjectsItem,
        )

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = ListOrganizationEmailDomainsResponse200ResultsProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        def _parse_role(
            data: object,
        ) -> Union[
            ListOrganizationEmailDomainsResponse200ResultsRoleType0,
            ListOrganizationEmailDomainsResponse200ResultsRoleType1,
            ListOrganizationEmailDomainsResponse200ResultsRoleType2,
            ListOrganizationEmailDomainsResponse200ResultsRoleType3,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = ListOrganizationEmailDomainsResponse200ResultsRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = ListOrganizationEmailDomainsResponse200ResultsRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2 = ListOrganizationEmailDomainsResponse200ResultsRoleType2(data)

                return role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_3 = ListOrganizationEmailDomainsResponse200ResultsRoleType3(data)

            return role_type_3

        role = _parse_role(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        organization_uuid = d.pop("organizationUuid")

        list_organization_email_domains_response_200_results = cls(
            projects=projects,
            role=role,
            email_domains=email_domains,
            organization_uuid=organization_uuid,
        )

        list_organization_email_domains_response_200_results.additional_properties = d
        return list_organization_email_domains_response_200_results

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
