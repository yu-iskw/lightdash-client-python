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
    from ..models.field import Field


T = TypeVar("T", bound="GetAvailableChartFiltersResponse200")


@attr.s(auto_attribs=True)
class GetAvailableChartFiltersResponse200:
    """
    Attributes:
        status (Union[Unset, SuccessStatus]):
        results (Union[Unset, List['Field']]):
    """

    status: Union[Unset, SuccessStatus] = UNSET
    results: Union[Unset, List["Field"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for componentsschemas_fields_item_data in self.results:
                componentsschemas_fields_item = componentsschemas_fields_item_data.to_dict()

                results.append(componentsschemas_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field import Field

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SuccessStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SuccessStatus(_status)

        results = []
        _results = d.pop("results", UNSET)
        for componentsschemas_fields_item_data in _results or []:
            componentsschemas_fields_item = Field.from_dict(componentsschemas_fields_item_data)

            results.append(componentsschemas_fields_item)

        get_available_chart_filters_response_200 = cls(
            status=status,
            results=results,
        )

        get_available_chart_filters_response_200.additional_properties = d
        return get_available_chart_filters_response_200

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
