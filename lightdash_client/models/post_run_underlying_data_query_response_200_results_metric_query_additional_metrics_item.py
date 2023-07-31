from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_compact_type_0 import (
    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0,
)
from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_compact_type_1 import (
    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1,
)
from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_format import (
    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFormat,
)
from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_type import (
    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item import (
        PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem,
    )


T = TypeVar("T", bound="PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItem")


@attr.s(auto_attribs=True)
class PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItem:
    """
    Attributes:
        type (PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemType):
        sql (str):
        table (str):
        name (str):
        label (Union[Unset, str]):
        description (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        round_ (Union[Unset, float]):
        compact (Union[PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0,
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1, Unset]):
        format_ (Union[Unset, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFormat]):
        index (Union[Unset, float]):
        filters (Union[Unset,
            List['PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem']]):
        base_dimension_name (Union[Unset, str]):
        uuid (Union[Unset, None, str]):
    """

    type: PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemType
    sql: str
    table: str
    name: str
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    round_: Union[Unset, float] = UNSET
    compact: Union[
        PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0,
        PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1,
        Unset,
    ] = UNSET
    format_: Union[Unset, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFormat] = UNSET
    index: Union[Unset, float] = UNSET
    filters: Union[
        Unset, List["PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem"]
    ] = UNSET
    base_dimension_name: Union[Unset, str] = UNSET
    uuid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        sql = self.sql
        table = self.table
        name = self.name
        label = self.label
        description = self.description
        hidden = self.hidden
        round_ = self.round_
        compact: Union[Unset, str]
        if isinstance(self.compact, Unset):
            compact = UNSET

        elif isinstance(
            self.compact, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0
        ):
            compact = UNSET
            if not isinstance(self.compact, Unset):
                compact = self.compact.value

        else:
            compact = UNSET
            if not isinstance(self.compact, Unset):
                compact = self.compact.value

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        index = self.index
        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)

        base_dimension_name = self.base_dimension_name
        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "sql": sql,
                "table": table,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if round_ is not UNSET:
            field_dict["round"] = round_
        if compact is not UNSET:
            field_dict["compact"] = compact
        if format_ is not UNSET:
            field_dict["format"] = format_
        if index is not UNSET:
            field_dict["index"] = index
        if filters is not UNSET:
            field_dict["filters"] = filters
        if base_dimension_name is not UNSET:
            field_dict["baseDimensionName"] = base_dimension_name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item_filters_item import (
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem,
        )

        d = src_dict.copy()
        type = PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemType(d.pop("type"))

        sql = d.pop("sql")

        table = d.pop("table")

        name = d.pop("name")

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        round_ = d.pop("round", UNSET)

        def _parse_compact(
            data: object,
        ) -> Union[
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0,
            PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _compact_type_0 = data
                compact_type_0: Union[
                    Unset, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0
                ]
                if isinstance(_compact_type_0, Unset):
                    compact_type_0 = UNSET
                else:
                    compact_type_0 = (
                        PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType0(
                            _compact_type_0
                        )
                    )

                return compact_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _compact_type_1 = data
            compact_type_1: Union[
                Unset, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1
            ]
            if isinstance(_compact_type_1, Unset):
                compact_type_1 = UNSET
            else:
                compact_type_1 = (
                    PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemCompactType1(
                        _compact_type_1
                    )
                )

            return compact_type_1

        compact = _parse_compact(d.pop("compact", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFormat(_format_)

        index = d.pop("index", UNSET)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = (
                PostRunUnderlyingDataQueryResponse200ResultsMetricQueryAdditionalMetricsItemFiltersItem.from_dict(
                    filters_item_data
                )
            )

            filters.append(filters_item)

        base_dimension_name = d.pop("baseDimensionName", UNSET)

        uuid = d.pop("uuid", UNSET)

        post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item = cls(
            type=type,
            sql=sql,
            table=table,
            name=name,
            label=label,
            description=description,
            hidden=hidden,
            round_=round_,
            compact=compact,
            format_=format_,
            index=index,
            filters=filters,
            base_dimension_name=base_dimension_name,
            uuid=uuid,
        )

        return post_run_underlying_data_query_response_200_results_metric_query_additional_metrics_item
