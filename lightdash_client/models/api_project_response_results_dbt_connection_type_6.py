from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_project_response_results_dbt_connection_type_6_type import (
    ApiProjectResponseResultsDbtConnectionType6Type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_response_results_dbt_connection_type_6_environment_item import (
        ApiProjectResponseResultsDbtConnectionType6EnvironmentItem,
    )


T = TypeVar("T", bound="ApiProjectResponseResultsDbtConnectionType6")


@attr.s(auto_attribs=True)
class ApiProjectResponseResultsDbtConnectionType6:
    """
    Attributes:
        type (ApiProjectResponseResultsDbtConnectionType6Type):
        target (Union[Unset, str]):
        environment (Union[Unset, List['ApiProjectResponseResultsDbtConnectionType6EnvironmentItem']]):
        hide_refresh_button (Union[Unset, bool]):
    """

    type: ApiProjectResponseResultsDbtConnectionType6Type
    target: Union[Unset, str] = UNSET
    environment: Union[Unset, List["ApiProjectResponseResultsDbtConnectionType6EnvironmentItem"]] = UNSET
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
        from ..models.api_project_response_results_dbt_connection_type_6_environment_item import (
            ApiProjectResponseResultsDbtConnectionType6EnvironmentItem,
        )

        d = src_dict.copy()
        type = ApiProjectResponseResultsDbtConnectionType6Type(d.pop("type"))

        target = d.pop("target", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ApiProjectResponseResultsDbtConnectionType6EnvironmentItem.from_dict(
                environment_item_data
            )

            environment.append(environment_item)

        hide_refresh_button = d.pop("hideRefreshButton", UNSET)

        api_project_response_results_dbt_connection_type_6 = cls(
            type=type,
            target=target,
            environment=environment,
            hide_refresh_button=hide_refresh_button,
        )

        return api_project_response_results_dbt_connection_type_6
