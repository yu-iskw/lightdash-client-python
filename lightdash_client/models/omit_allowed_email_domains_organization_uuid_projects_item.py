from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.omit_allowed_email_domains_organization_uuid_projects_item_role_type_0 import (
    OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0,
)
from ..models.omit_allowed_email_domains_organization_uuid_projects_item_role_type_1 import (
    OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1,
)
from ..models.omit_allowed_email_domains_organization_uuid_projects_item_role_type_2 import (
    OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType2,
)

T = TypeVar("T", bound="OmitAllowedEmailDomainsOrganizationUuidProjectsItem")


@attr.s(auto_attribs=True)
class OmitAllowedEmailDomainsOrganizationUuidProjectsItem:
    """
    Attributes:
        role (Union[OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0,
            OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1,
            OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType2]):
        project_uuid (str):
    """

    role: Union[
        OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0,
        OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1,
        OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType2,
    ]
    project_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: str

        if isinstance(self.role, OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0):
            role = self.role.value

        elif isinstance(self.role, OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1):
            role = self.role.value

        else:
            role = self.role.value

        project_uuid = self.project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "projectUuid": project_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_role(
            data: object,
        ) -> Union[
            OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0,
            OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1,
            OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType2,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType0(data)

                return role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_2 = OmitAllowedEmailDomainsOrganizationUuidProjectsItemRoleType2(data)

            return role_type_2

        role = _parse_role(d.pop("role"))

        project_uuid = d.pop("projectUuid")

        omit_allowed_email_domains_organization_uuid_projects_item = cls(
            role=role,
            project_uuid=project_uuid,
        )

        omit_allowed_email_domains_organization_uuid_projects_item.additional_properties = d
        return omit_allowed_email_domains_organization_uuid_projects_item

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
