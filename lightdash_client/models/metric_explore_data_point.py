import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_explore_data_point_compare_metric import MetricExploreDataPointCompareMetric
    from ..models.metric_explore_data_point_metric import MetricExploreDataPointMetric


T = TypeVar("T", bound="MetricExploreDataPoint")


@_attrs_define
class MetricExploreDataPoint:
    """
    Attributes:
        compare_metric (MetricExploreDataPointCompareMetric):
        metric (MetricExploreDataPointMetric):
        segment (Union[None, str]):
        date (datetime.datetime):
    """

    compare_metric: "MetricExploreDataPointCompareMetric"
    metric: "MetricExploreDataPointMetric"
    segment: Union[None, str]
    date: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.metric_explore_data_point_compare_metric import MetricExploreDataPointCompareMetric
        from ..models.metric_explore_data_point_metric import MetricExploreDataPointMetric

        compare_metric = self.compare_metric.to_dict()

        metric = self.metric.to_dict()

        segment: Union[None, str]
        segment = self.segment

        date = self.date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compareMetric": compare_metric,
                "metric": metric,
                "segment": segment,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metric_explore_data_point_compare_metric import MetricExploreDataPointCompareMetric
        from ..models.metric_explore_data_point_metric import MetricExploreDataPointMetric

        d = src_dict.copy()
        compare_metric = MetricExploreDataPointCompareMetric.from_dict(d.pop("compareMetric"))

        metric = MetricExploreDataPointMetric.from_dict(d.pop("metric"))

        def _parse_segment(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        segment = _parse_segment(d.pop("segment"))

        date = isoparse(d.pop("date"))

        metric_explore_data_point = cls(
            compare_metric=compare_metric,
            metric=metric,
            segment=segment,
            date=date,
        )

        metric_explore_data_point.additional_properties = d
        return metric_explore_data_point

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
