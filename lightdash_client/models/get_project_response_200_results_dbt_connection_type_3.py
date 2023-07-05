from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_response_200_results_dbt_connection_type_3_type import (
    GetProjectResponse200ResultsDbtConnectionType3Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_response_200_results_dbt_connection_type_3_environment_item import (
        GetProjectResponse200ResultsDbtConnectionType3EnvironmentItem,
    )


T = TypeVar("T", bound="GetProjectResponse200ResultsDbtConnectionType3")


@attr.s(auto_attribs=True)
class GetProjectResponse200ResultsDbtConnectionType3:
    """
    Attributes:
        type (GetProjectResponse200ResultsDbtConnectionType3Type):
        username (str):
        personal_access_token (str):
        repository (str):
        branch (str):
        project_sub_path (str):
        target (Union[Unset, str]):
        environment (Union[Unset, List['GetProjectResponse200ResultsDbtConnectionType3EnvironmentItem']]):
        host_domain (Union[Unset, str]):
    """

    type: GetProjectResponse200ResultsDbtConnectionType3Type
    username: str
    personal_access_token: str
    repository: str
    branch: str
    project_sub_path: str
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["GetProjectResponse200ResultsDbtConnectionType3EnvironmentItem"]] = UNSET
    host_domain: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        username = self.username
        personal_access_token = self.personal_access_token
        repository = self.repository
        branch = self.branch
        project_sub_path = self.project_sub_path
        target = self.target
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        host_domain = self.host_domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "username": username,
                "personal_access_token": personal_access_token,
                "repository": repository,
                "branch": branch,
                "project_sub_path": project_sub_path,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if environment is not UNSET:
            field_dict["environment"] = environment
        if host_domain is not UNSET:
            field_dict["host_domain"] = host_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_project_response_200_results_dbt_connection_type_3_environment_item import (
            GetProjectResponse200ResultsDbtConnectionType3EnvironmentItem,
        )

        d = src_dict.copy()
        type = GetProjectResponse200ResultsDbtConnectionType3Type(d.pop("type"))

        username = d.pop("username")

        personal_access_token = d.pop("personal_access_token")

        repository = d.pop("repository")

        branch = d.pop("branch")

        project_sub_path = d.pop("project_sub_path")

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = GetProjectResponse200ResultsDbtConnectionType3EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        host_domain = d.pop("host_domain", UNSET)

        get_project_response_200_results_dbt_connection_type_3 = cls(
            type=type,
            username=username,
            personal_access_token=personal_access_token,
            repository=repository,
            branch=branch,
            project_sub_path=project_sub_path,
            target=target,
            environment=environment,
            host_domain=host_domain,
        )

        return get_project_response_200_results_dbt_connection_type_3
