from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_get_project_member_response_results_role import (
    ApiGetProjectMemberResponseResultsRole,
)

T = TypeVar("T", bound="ApiGetProjectMemberResponseResults")


@attr.s(auto_attribs=True)
class ApiGetProjectMemberResponseResults:
    """
    Attributes:
        last_name (str):
        first_name (str):
        email (str):
        role (ApiGetProjectMemberResponseResultsRole):
        project_uuid (str):
        user_uuid (str):
    """

    last_name: str
    first_name: str
    email: str
    role: ApiGetProjectMemberResponseResultsRole
    project_uuid: str
    user_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_name = self.last_name
        first_name = self.first_name
        email = self.email
        role = self.role.value

        project_uuid = self.project_uuid
        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastName": last_name,
                "firstName": first_name,
                "email": email,
                "role": role,
                "projectUuid": project_uuid,
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        email = d.pop("email")

        role = ApiGetProjectMemberResponseResultsRole(d.pop("role"))

        project_uuid = d.pop("projectUuid")

        user_uuid = d.pop("userUuid")

        api_get_project_member_response_results = cls(
            last_name=last_name,
            first_name=first_name,
            email=email,
            role=role,
            project_uuid=project_uuid,
            user_uuid=user_uuid,
        )

        api_get_project_member_response_results.additional_properties = d
        return api_get_project_member_response_results

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
