from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.success_status import SuccessStatus
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.project_tables_configuration import ProjectTablesConfiguration


T = TypeVar("T", bound="GetProjectTablesConfigurationResponse200")


@attr.s(auto_attribs=True)
class GetProjectTablesConfigurationResponse200:
    """
    Attributes:
        results (ProjectTablesConfiguration):
        status (Union[Unset, SuccessStatus]):
    """

    results: "ProjectTablesConfiguration"
    status: Union[Unset, SuccessStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_tables_configuration import ProjectTablesConfiguration

        d = src_dict.copy()
        results = ProjectTablesConfiguration.from_dict(d.pop("results"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SuccessStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SuccessStatus(_status)

        get_project_tables_configuration_response_200 = cls(
            results=results,
            status=status,
        )

        get_project_tables_configuration_response_200.additional_properties = d
        return get_project_tables_configuration_response_200

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
