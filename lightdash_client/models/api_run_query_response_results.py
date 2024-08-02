from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_metadata import CacheMetadata
    from ..models.metric_query_response import MetricQueryResponse
    from ..models.record_string_item_or_additional_metric import (
        RecordStringItemOrAdditionalMetric,
    )


T = TypeVar("T", bound="ApiRunQueryResponseResults")


@_attrs_define
class ApiRunQueryResponseResults:
    """
    Attributes:
        rows (List[Any]):
        cache_metadata (CacheMetadata):
        metric_query (MetricQueryResponse):
        fields (Union[Unset, RecordStringItemOrAdditionalMetric]): Construct a type with a set of properties K of type T
    """

    rows: List[Any]
    cache_metadata: "CacheMetadata"
    metric_query: "MetricQueryResponse"
    fields: Union[Unset, "RecordStringItemOrAdditionalMetric"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = self.rows

        cache_metadata = self.cache_metadata.to_dict()

        metric_query = self.metric_query.to_dict()

        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "cacheMetadata": cache_metadata,
                "metricQuery": metric_query,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cache_metadata import CacheMetadata
        from ..models.metric_query_response import MetricQueryResponse
        from ..models.record_string_item_or_additional_metric import (
            RecordStringItemOrAdditionalMetric,
        )

        d = src_dict.copy()
        rows = cast(List[Any], d.pop("rows"))

        cache_metadata = CacheMetadata.from_dict(d.pop("cacheMetadata"))

        metric_query = MetricQueryResponse.from_dict(d.pop("metricQuery"))

        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, RecordStringItemOrAdditionalMetric]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = RecordStringItemOrAdditionalMetric.from_dict(_fields)

        api_run_query_response_results = cls(
            rows=rows,
            cache_metadata=cache_metadata,
            metric_query=metric_query,
            fields=fields,
        )

        api_run_query_response_results.additional_properties = d
        return api_run_query_response_results

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
