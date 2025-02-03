from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_metric_format_options import PickMetricFormatOptions


T = TypeVar("T", bound="MetricOverrides")


@_attrs_define
class MetricOverrides:
    """ """

    additional_properties: Dict[str, "PickMetricFormatOptions"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_metric_format_options import PickMetricFormatOptions

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_metric_format_options import PickMetricFormatOptions

        d = src_dict.copy()
        metric_overrides = cls()

        from ..models.custom_format import CustomFormat

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PickMetricFormatOptions.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        metric_overrides.additional_properties = additional_properties
        return metric_overrides

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "PickMetricFormatOptions":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "PickMetricFormatOptions") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
