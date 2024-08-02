from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_member_role_editor import ProjectMemberRoleEDITOR
from ..models.project_member_role_interactiveviewer import (
    ProjectMemberRoleINTERACTIVEVIEWER,
)
from ..models.project_member_role_viewer import ProjectMemberRoleVIEWER

T = TypeVar("T", bound="AllowedEmailDomainsProjectsItem")


@_attrs_define
class AllowedEmailDomainsProjectsItem:
    """
    Attributes:
        role (Union[ProjectMemberRoleEDITOR, ProjectMemberRoleINTERACTIVEVIEWER, ProjectMemberRoleVIEWER]):
        project_uuid (str):
    """

    role: Union[ProjectMemberRoleEDITOR, ProjectMemberRoleINTERACTIVEVIEWER, ProjectMemberRoleVIEWER]
    project_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: str
        if isinstance(self.role, ProjectMemberRoleEDITOR):
            role = self.role.value
        elif isinstance(self.role, ProjectMemberRoleINTERACTIVEVIEWER):
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
        ) -> Union[ProjectMemberRoleEDITOR, ProjectMemberRoleINTERACTIVEVIEWER, ProjectMemberRoleVIEWER]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_allowed_email_domain_projects_role_type_0 = ProjectMemberRoleEDITOR(data)

                return componentsschemas_allowed_email_domain_projects_role_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_allowed_email_domain_projects_role_type_1 = ProjectMemberRoleINTERACTIVEVIEWER(data)

                return componentsschemas_allowed_email_domain_projects_role_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_allowed_email_domain_projects_role_type_2 = ProjectMemberRoleVIEWER(data)

            return componentsschemas_allowed_email_domain_projects_role_type_2

        role = _parse_role(d.pop("role"))

        project_uuid = d.pop("projectUuid")

        allowed_email_domains_projects_item = cls(
            role=role,
            project_uuid=project_uuid,
        )

        allowed_email_domains_projects_item.additional_properties = d
        return allowed_email_domains_projects_item

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
