from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_dbt_cloud_integration_settings_response_200_status import (
    GetDbtCloudIntegrationSettingsResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_dbt_cloud_integration_settings_response_200_results import (
        GetDbtCloudIntegrationSettingsResponse200Results,
    )


T = TypeVar("T", bound="GetDbtCloudIntegrationSettingsResponse200")


@attr.s(auto_attribs=True)
class GetDbtCloudIntegrationSettingsResponse200:
    """
    Attributes:
        status (GetDbtCloudIntegrationSettingsResponse200Status):
        results (Union[Unset, GetDbtCloudIntegrationSettingsResponse200Results]): Configuration for a Lightdash
            integration with dbt Cloud
    """

    status: GetDbtCloudIntegrationSettingsResponse200Status
    results: Union[Unset, "GetDbtCloudIntegrationSettingsResponse200Results"] = UNSET
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
        from ..models.get_dbt_cloud_integration_settings_response_200_results import (
            GetDbtCloudIntegrationSettingsResponse200Results,
        )

        d = src_dict.copy()
        status = GetDbtCloudIntegrationSettingsResponse200Status(d.pop("status"))

        _results = d.pop("results", UNSET)
        results: Union[Unset, GetDbtCloudIntegrationSettingsResponse200Results]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = GetDbtCloudIntegrationSettingsResponse200Results.from_dict(_results)

        get_dbt_cloud_integration_settings_response_200 = cls(
            status=status,
            results=results,
        )

        get_dbt_cloud_integration_settings_response_200.additional_properties = d
        return get_dbt_cloud_integration_settings_response_200

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
