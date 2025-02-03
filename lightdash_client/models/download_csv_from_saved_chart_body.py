from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadCsvFromSavedChartBody")


@_attrs_define
class DownloadCsvFromSavedChartBody:
    """
    Attributes:
        only_raw (bool):
        dashboard_filters (Any): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.
        csv_limit (Union[None, Unset, float]):
        tile_uuid (Union[Unset, str]):
    """

    only_raw: bool
    dashboard_filters: Any
    csv_limit: Union[None, Unset, float] = UNSET
    tile_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        only_raw = self.only_raw

        dashboard_filters = self.dashboard_filters

        csv_limit: Union[None, Unset, float]
        if isinstance(self.csv_limit, Unset):
            csv_limit = UNSET
        else:
            csv_limit = self.csv_limit

        tile_uuid = self.tile_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "onlyRaw": only_raw,
                "dashboardFilters": dashboard_filters,
            }
        )
        if csv_limit is not UNSET:
            field_dict["csvLimit"] = csv_limit
        if tile_uuid is not UNSET:
            field_dict["tileUuid"] = tile_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        only_raw = d.pop("onlyRaw")

        dashboard_filters = d.pop("dashboardFilters")

        def _parse_csv_limit(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        csv_limit = _parse_csv_limit(d.pop("csvLimit", UNSET))

        tile_uuid = d.pop("tileUuid", UNSET)

        download_csv_from_saved_chart_body = cls(
            only_raw=only_raw,
            dashboard_filters=dashboard_filters,
            csv_limit=csv_limit,
            tile_uuid=tile_uuid,
        )

        download_csv_from_saved_chart_body.additional_properties = d
        return download_csv_from_saved_chart_body

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
