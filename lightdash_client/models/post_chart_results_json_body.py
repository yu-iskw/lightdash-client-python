from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.filters import Filters


T = TypeVar("T", bound="PostChartResultsJsonBody")


@attr.s(auto_attribs=True)
class PostChartResultsJsonBody:
    """
    Attributes:
        filters (Union[Unset, Filters]):
    """

    filters: Union[Unset, "Filters"] = UNSET
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
        from ..models.filters import Filters

        d = src_dict.copy()
        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, Filters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = Filters.from_dict(_filters)

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
