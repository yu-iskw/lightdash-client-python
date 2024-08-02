from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickCreateDbtCloudIntegrationMetricsJobId")


@_attrs_define
class PickCreateDbtCloudIntegrationMetricsJobId:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        metrics_job_id (str): Job id for a dbt cloud job containing a compiled dbt project with available dbt metrics
    """

    metrics_job_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_job_id = self.metrics_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricsJobId": metrics_job_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metrics_job_id = d.pop("metricsJobId")

        pick_create_dbt_cloud_integration_metrics_job_id = cls(
            metrics_job_id=metrics_job_id,
        )

        pick_create_dbt_cloud_integration_metrics_job_id.additional_properties = d
        return pick_create_dbt_cloud_integration_metrics_job_id

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
