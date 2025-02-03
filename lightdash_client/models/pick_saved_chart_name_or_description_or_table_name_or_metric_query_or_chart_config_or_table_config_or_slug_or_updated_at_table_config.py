from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig",
)


@_attrs_define
class PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig:
    """
    Attributes:
        column_order (List[str]):
    """

    column_order: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_order = self.column_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnOrder": column_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_order = cast(List[str], d.pop("columnOrder"))

        pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config = cls(
            column_order=column_order,
        )

        pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config.additional_properties = d
        return pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config

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
