from typing import Any
from typing import cast
from typing import Dict
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.dbt_project_type_dbtcloudide import DbtProjectTypeDBTCLOUDIDE

T = TypeVar("T", bound="DbtCloudIDEProjectConfig")


@attr.s(auto_attribs=True)
class DbtCloudIDEProjectConfig:
    """
    Attributes:
        type (DbtProjectTypeDBTCLOUDIDE):
        api_key (str):
        account_id (Union[float, str]):
        environment_id (Union[float, str]):
        project_id (Union[float, str]):
    """

    type: DbtProjectTypeDBTCLOUDIDE
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
        type = DbtProjectTypeDBTCLOUDIDE(d.pop("type"))

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

        dbt_cloud_ide_project_config = cls(
            type=type,
            api_key=api_key,
            account_id=account_id,
            environment_id=environment_id,
            project_id=project_id,
        )

        return dbt_cloud_ide_project_config
