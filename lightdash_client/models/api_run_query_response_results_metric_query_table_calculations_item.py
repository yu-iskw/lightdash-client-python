from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_run_query_response_results_metric_query_table_calculations_item_format import (
        ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat,
    )


T = TypeVar("T", bound="ApiRunQueryResponseResultsMetricQueryTableCalculationsItem")


@attr.s(auto_attribs=True)
class ApiRunQueryResponseResultsMetricQueryTableCalculationsItem:
    """
    Attributes:
        sql (str):
        display_name (str):
        name (str):
        format_ (Union[Unset, ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat]):
        index (Union[Unset, float]):
    """

    sql: str
    display_name: str
    name: str
    format_: Union[Unset, "ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat"] = UNSET
    index: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql = self.sql
        display_name = self.display_name
        name = self.name
        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql": sql,
                "displayName": display_name,
                "name": name,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_run_query_response_results_metric_query_table_calculations_item_format import (
            ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat,
        )

        d = src_dict.copy()
        sql = d.pop("sql")

        display_name = d.pop("displayName")

        name = d.pop("name")

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ApiRunQueryResponseResultsMetricQueryTableCalculationsItemFormat.from_dict(_format_)

        index = d.pop("index", UNSET)

        api_run_query_response_results_metric_query_table_calculations_item = cls(
            sql=sql,
            display_name=display_name,
            name=name,
            format_=format_,
            index=index,
        )

        api_run_query_response_results_metric_query_table_calculations_item.additional_properties = d
        return api_run_query_response_results_metric_query_table_calculations_item

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
