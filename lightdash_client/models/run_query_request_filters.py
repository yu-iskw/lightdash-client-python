from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="RunQueryRequestFilters")


@attr.s(auto_attribs=True)
class RunQueryRequestFilters:
    """
    Attributes:
        metrics (Union[Unset, Any]):
        dimensions (Union[Unset, Any]):
    """

    metrics: Union[Unset, Any] = UNSET
    dimensions: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics = self.metrics
        dimensions = self.dimensions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metrics = d.pop("metrics", UNSET)

        dimensions = d.pop("dimensions", UNSET)

        run_query_request_filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        run_query_request_filters.additional_properties = d
        return run_query_request_filters

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
