from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_response_200_results_dbt_connection_type_0_type import (
    GetProjectResponse200ResultsDbtConnectionType0Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_response_200_results_dbt_connection_type_0_environment_item import (
        GetProjectResponse200ResultsDbtConnectionType0EnvironmentItem,
    )


T = TypeVar("T", bound="GetProjectResponse200ResultsDbtConnectionType0")


@attr.s(auto_attribs=True)
class GetProjectResponse200ResultsDbtConnectionType0:
    """
    Attributes:
        type (GetProjectResponse200ResultsDbtConnectionType0Type):
        target (Union[Unset, str]):
        environment (Union[Unset, List['GetProjectResponse200ResultsDbtConnectionType0EnvironmentItem']]):
        profiles_dir (Union[Unset, str]):
        project_dir (Union[Unset, str]):
    """

    type: GetProjectResponse200ResultsDbtConnectionType0Type
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["GetProjectResponse200ResultsDbtConnectionType0EnvironmentItem"]] = UNSET
    profiles_dir: Union[Unset, str] = UNSET
    project_dir: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        target = self.target
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        profiles_dir = self.profiles_dir
        project_dir = self.project_dir

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if environment is not UNSET:
            field_dict["environment"] = environment
        if profiles_dir is not UNSET:
            field_dict["profiles_dir"] = profiles_dir
        if project_dir is not UNSET:
            field_dict["project_dir"] = project_dir

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_project_response_200_results_dbt_connection_type_0_environment_item import (
            GetProjectResponse200ResultsDbtConnectionType0EnvironmentItem,
        )

        d = src_dict.copy()
        type = GetProjectResponse200ResultsDbtConnectionType0Type(d.pop("type"))

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = GetProjectResponse200ResultsDbtConnectionType0EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        profiles_dir = d.pop("profiles_dir", UNSET)

        project_dir = d.pop("project_dir", UNSET)

        get_project_response_200_results_dbt_connection_type_0 = cls(
            type=type,
            target=target,
            environment=environment,
            profiles_dir=profiles_dir,
            project_dir=project_dir,
        )

        return get_project_response_200_results_dbt_connection_type_0
