from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.api_project_response_results_dbt_connection_type_5_type import (
    ApiProjectResponseResultsDbtConnectionType5Type,
)
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.api_project_response_results_dbt_connection_type_5_environment_item import (
        ApiProjectResponseResultsDbtConnectionType5EnvironmentItem,
    )


T = TypeVar("T", bound="ApiProjectResponseResultsDbtConnectionType5")


@attr.s(auto_attribs=True)
class ApiProjectResponseResultsDbtConnectionType5:
    """
    Attributes:
        type (ApiProjectResponseResultsDbtConnectionType5Type):
        personal_access_token (str):
        organization (str):
        project (str):
        repository (str):
        branch (str):
        project_sub_path (str):
        target (Union[Unset, str]):
        environment (Union[Unset, List['ApiProjectResponseResultsDbtConnectionType5EnvironmentItem']]):
    """

    type: ApiProjectResponseResultsDbtConnectionType5Type
    personal_access_token: str
    organization: str
    project: str
    repository: str
    branch: str
    project_sub_path: str
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["ApiProjectResponseResultsDbtConnectionType5EnvironmentItem"]] = UNSET

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
        from ..models.api_project_response_results_dbt_connection_type_5_environment_item import (
            ApiProjectResponseResultsDbtConnectionType5EnvironmentItem,
        )

        d = src_dict.copy()
        type = ApiProjectResponseResultsDbtConnectionType5Type(d.pop("type"))

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
            environment_item = ApiProjectResponseResultsDbtConnectionType5EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        api_project_response_results_dbt_connection_type_5 = cls(
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

        return api_project_response_results_dbt_connection_type_5