from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_csv_from_saved_chart_response_200_status import DownloadCsvFromSavedChartResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.download_csv_from_saved_chart_response_200_results import DownloadCsvFromSavedChartResponse200Results


T = TypeVar("T", bound="DownloadCsvFromSavedChartResponse200")


@_attrs_define
class DownloadCsvFromSavedChartResponse200:
    """
    Attributes:
        results (DownloadCsvFromSavedChartResponse200Results):
        status (DownloadCsvFromSavedChartResponse200Status):
    """

    results: "DownloadCsvFromSavedChartResponse200Results"
    status: DownloadCsvFromSavedChartResponse200Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.download_csv_from_saved_chart_response_200_results import (
            DownloadCsvFromSavedChartResponse200Results,
        )

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
        from ..models.download_csv_from_saved_chart_response_200_results import (
            DownloadCsvFromSavedChartResponse200Results,
        )

        d = src_dict.copy()
        results = DownloadCsvFromSavedChartResponse200Results.from_dict(d.pop("results"))

        status = DownloadCsvFromSavedChartResponse200Status(d.pop("status"))

        download_csv_from_saved_chart_response_200 = cls(
            results=results,
            status=status,
        )

        download_csv_from_saved_chart_response_200.additional_properties = d
        return download_csv_from_saved_chart_response_200

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
