from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.api_run_query_response_results_metric_query_table_calculations_item_format_separator import (
    ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatSeparator,
)
from ..models.api_run_query_response_results_metric_query_table_calculations_item_format_type import (
    ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatType,
)
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat")


@attr.s(auto_attribs=True)
class ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat:
    """
    Attributes:
        type (ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatType):
        separator (Union[Unset, ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatSeparator]):
        round_ (Union[Unset, float]):
    """

    type: ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatType
    separator: Union[Unset, ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatSeparator] = UNSET
    round_: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        separator: Union[Unset, str] = UNSET
        if not isinstance(self.separator, Unset):
            separator = self.separator.value

        round_ = self.round_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if separator is not UNSET:
            field_dict["separator"] = separator
        if round_ is not UNSET:
            field_dict["round"] = round_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatType(d.pop("type"))

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatSeparator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormatSeparator(_separator)

        round_ = d.pop("round", UNSET)

        api_run_query_response_results_metric_query_table_calculations_item_format = cls(
            type=type,
            separator=separator,
            round_=round_,
        )

        api_run_query_response_results_metric_query_table_calculations_item_format.additional_properties = d
        return api_run_query_response_results_metric_query_table_calculations_item_format

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
