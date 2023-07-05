from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_chart_results_json_body_filters import (
        PostChartResultsJsonBodyFilters,
    )


T = TypeVar("T", bound="PostChartResultsJsonBody")


@attr.s(auto_attribs=True)
class PostChartResultsJsonBody:
    """
    Attributes:
        filters (Union[Unset, PostChartResultsJsonBodyFilters]):
    """

    filters: Union[Unset, "PostChartResultsJsonBodyFilters"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_chart_results_json_body_filters import (
            PostChartResultsJsonBodyFilters,
        )

        d = src_dict.copy()
        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, PostChartResultsJsonBodyFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = PostChartResultsJsonBodyFilters.from_dict(_filters)

        post_chart_results_json_body = cls(
            filters=filters,
        )

        post_chart_results_json_body.additional_properties = d
        return post_chart_results_json_body

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
