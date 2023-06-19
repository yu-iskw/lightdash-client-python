from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.dbt_project_type_none import DbtProjectTypeNONE
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.dbt_project_environment_variable import DbtProjectEnvironmentVariable


T = TypeVar("T", bound="DbtNoneProjectConfig")


@attr.s(auto_attribs=True)
class DbtNoneProjectConfig:
    """
    Attributes:
        type (DbtProjectTypeNONE):
        target (Union[Unset, str]):
        environment (Union[Unset, List['DbtProjectEnvironmentVariable']]):
        hide_refresh_button (Union[Unset, bool]):
    """

    type: DbtProjectTypeNONE
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["DbtProjectEnvironmentVariable"]] = UNSET
    hide_refresh_button: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        target = self.target
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        hide_refresh_button = self.hide_refresh_button

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
        if hide_refresh_button is not UNSET:
            field_dict["hideRefreshButton"] = hide_refresh_button

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dbt_project_environment_variable import DbtProjectEnvironmentVariable

        d = src_dict.copy()
        type = DbtProjectTypeNONE(d.pop("type"))

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = DbtProjectEnvironmentVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        hide_refresh_button = d.pop("hideRefreshButton", UNSET)

        dbt_none_project_config = cls(
            type=type,
            target=target,
            environment=environment,
            hide_refresh_button=hide_refresh_button,
        )

        return dbt_none_project_config
