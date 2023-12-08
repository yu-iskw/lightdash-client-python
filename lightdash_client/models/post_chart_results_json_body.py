from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChartResultsJsonBody")


@attr.s(auto_attribs=True)
class PostChartResultsJsonBody:
    """
    Attributes:
        invalidate_cache (Union[Unset, bool]):
    """

    invalidate_cache: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invalidate_cache = self.invalidate_cache

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invalidate_cache is not UNSET:
            field_dict["invalidateCache"] = invalidate_cache

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invalidate_cache = d.pop("invalidateCache", UNSET)

        post_chart_results_json_body = cls(
            invalidate_cache=invalidate_cache,
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
