from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRunQueryJsonBodyFilters")


@attr.s(auto_attribs=True)
class PostRunQueryJsonBodyFilters:
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

        post_run_query_json_body_filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        post_run_query_json_body_filters.additional_properties = d
        return post_run_query_json_body_filters

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
