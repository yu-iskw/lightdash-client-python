from typing import Any, Dict, Type, TypeVar, Union, cast

import attr

from ..models.dbt_project_config_type_1_type import DbtProjectConfigType1Type

T = TypeVar("T", bound="DbtProjectConfigType1")


@attr.s(auto_attribs=True)
class DbtProjectConfigType1:
    """
    Attributes:
        type (DbtProjectConfigType1Type):
        api_key (str):
        account_id (Union[float, str]):
        environment_id (Union[float, str]):
        project_id (Union[float, str]):
    """

    type: DbtProjectConfigType1Type
    api_key: str
    account_id: Union[float, str]
    environment_id: Union[float, str]
    project_id: Union[float, str]

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        api_key = self.api_key
        account_id: Union[float, str]

        account_id = self.account_id

        environment_id: Union[float, str]

        environment_id = self.environment_id

        project_id: Union[float, str]

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "api_key": api_key,
                "account_id": account_id,
                "environment_id": environment_id,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DbtProjectConfigType1Type(d.pop("type"))

        api_key = d.pop("api_key")

        def _parse_account_id(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        account_id = _parse_account_id(d.pop("account_id"))

        def _parse_environment_id(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        environment_id = _parse_environment_id(d.pop("environment_id"))

        def _parse_project_id(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        project_id = _parse_project_id(d.pop("project_id"))

        dbt_project_config_type_1 = cls(
            type=type,
            api_key=api_key,
            account_id=account_id,
            environment_id=environment_id,
            project_id=project_id,
        )

        return dbt_project_config_type_1
