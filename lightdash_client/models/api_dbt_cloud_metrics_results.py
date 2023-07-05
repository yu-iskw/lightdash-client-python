from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_dbt_cloud_metrics_results_metrics_item import (
        ApiDbtCloudMetricsResultsMetricsItem,
    )


T = TypeVar("T", bound="ApiDbtCloudMetricsResults")


@attr.s(auto_attribs=True)
class ApiDbtCloudMetricsResults:
    """Response from dbt cloud metadata api containing a list of metric definitions

    Attributes:
        metrics (List['ApiDbtCloudMetricsResultsMetricsItem']): A list of dbt metric definitions from the dbt cloud
            metadata api
    """

    metrics: List["ApiDbtCloudMetricsResultsMetricsItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()

            metrics.append(metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_dbt_cloud_metrics_results_metrics_item import (
            ApiDbtCloudMetricsResultsMetricsItem,
        )

        d = src_dict.copy()
        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = ApiDbtCloudMetricsResultsMetricsItem.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        api_dbt_cloud_metrics_results = cls(
            metrics=metrics,
        )

        api_dbt_cloud_metrics_results.additional_properties = d
        return api_dbt_cloud_metrics_results

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
