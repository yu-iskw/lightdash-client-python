from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_dbt_cloud_metrics_status import ApiDbtCloudMetricsStatus

if TYPE_CHECKING:
    from ..models.api_dbt_cloud_metrics_results import ApiDbtCloudMetricsResults


T = TypeVar("T", bound="ApiDbtCloudMetrics")


@attr.s(auto_attribs=True)
class ApiDbtCloudMetrics:
    """
    Attributes:
        results (ApiDbtCloudMetricsResults): Response from dbt cloud metadata api containing a list of metric
            definitions
        status (ApiDbtCloudMetricsStatus):
    """

    results: "ApiDbtCloudMetricsResults"
    status: ApiDbtCloudMetricsStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_dbt_cloud_metrics_results import ApiDbtCloudMetricsResults

        d = src_dict.copy()
        results = ApiDbtCloudMetricsResults.from_dict(d.pop("results"))

        status = ApiDbtCloudMetricsStatus(d.pop("status"))

        api_dbt_cloud_metrics = cls(
            results=results,
            status=status,
        )

        api_dbt_cloud_metrics.additional_properties = d
        return api_dbt_cloud_metrics

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
