from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PickDashboardTileAtPropertiesExcludeKeyofDashboardTileAtPropertiesSavedChartUuidOrSavedSqlUuidOrSavedSemanticViewerChartUuid",
)


@_attrs_define
class PickDashboardTileAtPropertiesExcludeKeyofDashboardTileAtPropertiesSavedChartUuidOrSavedSqlUuidOrSavedSemanticViewerChartUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        title (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        pick_dashboard_tile_at_properties_exclude_keyof_dashboard_tile_at_properties_saved_chart_uuid_or_saved_sql_uuid_or_saved_semantic_viewer_chart_uuid = cls(
            title=title,
        )

        pick_dashboard_tile_at_properties_exclude_keyof_dashboard_tile_at_properties_saved_chart_uuid_or_saved_sql_uuid_or_saved_semantic_viewer_chart_uuid.additional_properties = d
        return pick_dashboard_tile_at_properties_exclude_keyof_dashboard_tile_at_properties_saved_chart_uuid_or_saved_sql_uuid_or_saved_semantic_viewer_chart_uuid

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
