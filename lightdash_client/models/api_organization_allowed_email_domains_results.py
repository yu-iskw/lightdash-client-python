from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.api_organization_allowed_email_domains_results_role_type_0 import (
    ApiOrganizationAllowedEmailDomainsResultsRoleType0,
)
from ..models.api_organization_allowed_email_domains_results_role_type_1 import (
    ApiOrganizationAllowedEmailDomainsResultsRoleType1,
)
from ..models.api_organization_allowed_email_domains_results_role_type_2 import (
    ApiOrganizationAllowedEmailDomainsResultsRoleType2,
)
from ..models.api_organization_allowed_email_domains_results_role_type_3 import (
    ApiOrganizationAllowedEmailDomainsResultsRoleType3,
)

if TYPE_CHECKING:
    from ..models.api_organization_allowed_email_domains_results_projects_item import (
        ApiOrganizationAllowedEmailDomainsResultsProjectsItem,
    )


T = TypeVar("T", bound="ApiOrganizationAllowedEmailDomainsResults")


@attr.s(auto_attribs=True)
class ApiOrganizationAllowedEmailDomainsResults:
    """
    Attributes:
        projects (List['ApiOrganizationAllowedEmailDomainsResultsProjectsItem']):
        role (Union[ApiOrganizationAllowedEmailDomainsResultsRoleType0,
            ApiOrganizationAllowedEmailDomainsResultsRoleType1, ApiOrganizationAllowedEmailDomainsResultsRoleType2,
            ApiOrganizationAllowedEmailDomainsResultsRoleType3]):
        email_domains (List[str]):
        organization_uuid (str):
    """

    projects: List["ApiOrganizationAllowedEmailDomainsResultsProjectsItem"]
    role: Union[
        ApiOrganizationAllowedEmailDomainsResultsRoleType0,
        ApiOrganizationAllowedEmailDomainsResultsRoleType1,
        ApiOrganizationAllowedEmailDomainsResultsRoleType2,
        ApiOrganizationAllowedEmailDomainsResultsRoleType3,
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

        if isinstance(self.role, ApiOrganizationAllowedEmailDomainsResultsRoleType0):
            role = self.role.value

        elif isinstance(self.role, ApiOrganizationAllowedEmailDomainsResultsRoleType1):
            role = self.role.value

        elif isinstance(self.role, ApiOrganizationAllowedEmailDomainsResultsRoleType2):
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
        from ..models.api_organization_allowed_email_domains_results_projects_item import (
            ApiOrganizationAllowedEmailDomainsResultsProjectsItem,
        )

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = ApiOrganizationAllowedEmailDomainsResultsProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        def _parse_role(
            data: object,
        ) -> Union[
            ApiOrganizationAllowedEmailDomainsResultsRoleType0,
            ApiOrganizationAllowedEmailDomainsResultsRoleType1,
            ApiOrganizationAllowedEmailDomainsResultsRoleType2,
            ApiOrganizationAllowedEmailDomainsResultsRoleType3,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = ApiOrganizationAllowedEmailDomainsResultsRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = ApiOrganizationAllowedEmailDomainsResultsRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2 = ApiOrganizationAllowedEmailDomainsResultsRoleType2(data)

                return role_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_3 = ApiOrganizationAllowedEmailDomainsResultsRoleType3(data)

            return role_type_3

        role = _parse_role(d.pop("role"))

        email_domains = cast(List[str], d.pop("emailDomains"))

        organization_uuid = d.pop("organizationUuid")

        api_organization_allowed_email_domains_results = cls(
            projects=projects,
            role=role,
            email_domains=email_domains,
            organization_uuid=organization_uuid,
        )

        api_organization_allowed_email_domains_results.additional_properties = d
        return api_organization_allowed_email_domains_results

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
