from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.api_project_response_results_dbt_connection_type_3_type import (
    ApiProjectResponseResultsDbtConnectionType3Type,
)
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.api_project_response_results_dbt_connection_type_3_environment_item import (
        ApiProjectResponseResultsDbtConnectionType3EnvironmentItem,
    )


T = TypeVar("T", bound="ApiProjectResponseResultsDbtConnectionType3")


@attr.s(auto_attribs=True)
class ApiProjectResponseResultsDbtConnectionType3:
    """
    Attributes:
        type (ApiProjectResponseResultsDbtConnectionType3Type):
        username (str):
        personal_access_token (str):
        repository (str):
        branch (str):
        project_sub_path (str):
        target (Union[Unset, str]):
        environment (Union[Unset, List['ApiProjectResponseResultsDbtConnectionType3EnvironmentItem']]):
        host_domain (Union[Unset, str]):
    """

    type: ApiProjectResponseResultsDbtConnectionType3Type
    username: str
    personal_access_token: str
    repository: str
    branch: str
    project_sub_path: str
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["ApiProjectResponseResultsDbtConnectionType3EnvironmentItem"]] = UNSET
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
        from ..models.api_project_response_results_dbt_connection_type_3_environment_item import (
            ApiProjectResponseResultsDbtConnectionType3EnvironmentItem,
        )

        d = src_dict.copy()
        type = ApiProjectResponseResultsDbtConnectionType3Type(d.pop("type"))

        username = d.pop("username")

        personal_access_token = d.pop("personal_access_token")

        repository = d.pop("repository")

        branch = d.pop("branch")

        project_sub_path = d.pop("project_sub_path")

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ApiProjectResponseResultsDbtConnectionType3EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        host_domain = d.pop("host_domain", UNSET)

        api_project_response_results_dbt_connection_type_3 = cls(
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

        return api_project_response_results_dbt_connection_type_3