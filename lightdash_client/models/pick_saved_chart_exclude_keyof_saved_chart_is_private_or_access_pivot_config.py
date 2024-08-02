from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig")


@_attrs_define
class PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig:
    """
    Attributes:
        columns (List[str]):
    """

    columns: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        columns = self.columns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        columns = cast(List[str], d.pop("columns"))

        pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_pivot_config = cls(
            columns=columns,
        )

        pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_pivot_config.additional_properties = d
        return pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_pivot_config

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
