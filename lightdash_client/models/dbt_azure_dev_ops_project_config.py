from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dbt_project_type_azuredevops import DbtProjectTypeAZUREDEVOPS
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dbt_project_environment_variable import DbtProjectEnvironmentVariable


T = TypeVar("T", bound="DbtAzureDevOpsProjectConfig")


@_attrs_define
class DbtAzureDevOpsProjectConfig:
    """
    Attributes:
        type (DbtProjectTypeAZUREDEVOPS):
        personal_access_token (str):
        organization (str):
        project (str):
        repository (str):
        branch (str):
        project_sub_path (str):
        target (Union[Unset, str]):
        environment (Union[Unset, List['DbtProjectEnvironmentVariable']]):
        selector (Union[Unset, str]):
    """

    type: DbtProjectTypeAZUREDEVOPS
    personal_access_token: str
    organization: str
    project: str
    repository: str
    branch: str
    project_sub_path: str
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["DbtProjectEnvironmentVariable"]] = UNSET
    selector: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dbt_project_environment_variable import DbtProjectEnvironmentVariable

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

        selector = self.selector

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dbt_project_environment_variable import DbtProjectEnvironmentVariable

        d = src_dict.copy()
        type = DbtProjectTypeAZUREDEVOPS(d.pop("type"))

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
            environment_item = DbtProjectEnvironmentVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        selector = d.pop("selector", UNSET)

        dbt_azure_dev_ops_project_config = cls(
            type=type,
            personal_access_token=personal_access_token,
            organization=organization,
            project=project,
            repository=repository,
            branch=branch,
            project_sub_path=project_sub_path,
            target=target,
            environment=environment,
            selector=selector,
        )

        dbt_azure_dev_ops_project_config.additional_properties = d
        return dbt_azure_dev_ops_project_config

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
