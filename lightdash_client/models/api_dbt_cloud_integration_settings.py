from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_dbt_cloud_integration_settings_status import (
    ApiDbtCloudIntegrationSettingsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_dbt_cloud_integration_settings_results import (
        ApiDbtCloudIntegrationSettingsResults,
    )


T = TypeVar("T", bound="ApiDbtCloudIntegrationSettings")


@attr.s(auto_attribs=True)
class ApiDbtCloudIntegrationSettings:
    """
    Attributes:
        status (ApiDbtCloudIntegrationSettingsStatus):
        results (Union[Unset, ApiDbtCloudIntegrationSettingsResults]): Configuration for a Lightdash integration with
            dbt Cloud
    """

    status: ApiDbtCloudIntegrationSettingsStatus
    results: Union[Unset, "ApiDbtCloudIntegrationSettingsResults"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_dbt_cloud_integration_settings_results import (
            ApiDbtCloudIntegrationSettingsResults,
        )

        d = src_dict.copy()
        status = ApiDbtCloudIntegrationSettingsStatus(d.pop("status"))

        _results = d.pop("results", UNSET)
        results: Union[Unset, ApiDbtCloudIntegrationSettingsResults]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = ApiDbtCloudIntegrationSettingsResults.from_dict(_results)

        api_dbt_cloud_integration_settings = cls(
            status=status,
            results=results,
        )

        api_dbt_cloud_integration_settings.additional_properties = d
        return api_dbt_cloud_integration_settings

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
