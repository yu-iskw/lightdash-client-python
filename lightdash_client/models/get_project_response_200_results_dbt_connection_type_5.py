from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_response_200_results_dbt_connection_type_5_type import (
    GetProjectResponse200ResultsDbtConnectionType5Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_response_200_results_dbt_connection_type_5_environment_item import (
        GetProjectResponse200ResultsDbtConnectionType5EnvironmentItem,
    )


T = TypeVar("T", bound="GetProjectResponse200ResultsDbtConnectionType5")


@attr.s(auto_attribs=True)
class GetProjectResponse200ResultsDbtConnectionType5:
    """
    Attributes:
        type (GetProjectResponse200ResultsDbtConnectionType5Type):
        personal_access_token (str):
        organization (str):
        project (str):
        repository (str):
        branch (str):
        project_sub_path (str):
        target (Union[Unset, str]):
        environment (Union[Unset, List['GetProjectResponse200ResultsDbtConnectionType5EnvironmentItem']]):
    """

    type: GetProjectResponse200ResultsDbtConnectionType5Type
    personal_access_token: str
    organization: str
    project: str
    repository: str
    branch: str
    project_sub_path: str
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["GetProjectResponse200ResultsDbtConnectionType5EnvironmentItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        personal_access_token = self.personal_access_token
        organization = self.organization
        project = self.project
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "personal_access_token": personal_access_token,
                "organization": organization,
                "project": project,
                "repository": repository,
                "branch": branch,
                "project_sub_path": project_sub_path,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_project_response_200_results_dbt_connection_type_5_environment_item import (
            GetProjectResponse200ResultsDbtConnectionType5EnvironmentItem,
        )

        d = src_dict.copy()
        type = GetProjectResponse200ResultsDbtConnectionType5Type(d.pop("type"))

        personal_access_token = d.pop("personal_access_token")

        organization = d.pop("organization")

        project = d.pop("project")

        repository = d.pop("repository")

        branch = d.pop("branch")

        project_sub_path = d.pop("project_sub_path")

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = GetProjectResponse200ResultsDbtConnectionType5EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        get_project_response_200_results_dbt_connection_type_5 = cls(
            type=type,
            personal_access_token=personal_access_token,
            organization=organization,
            project=project,
            repository=repository,
            branch=branch,
            project_sub_path=project_sub_path,
            target=target,
            environment=environment,
        )

        return get_project_response_200_results_dbt_connection_type_5
