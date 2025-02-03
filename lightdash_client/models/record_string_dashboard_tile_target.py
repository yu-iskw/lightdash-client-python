from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_field_target import DashboardFieldTarget


T = TypeVar("T", bound="RecordStringDashboardTileTarget")


@_attrs_define
class RecordStringDashboardTileTarget:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[str, Union["DashboardFieldTarget", bool]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_field_target import DashboardFieldTarget

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, DashboardFieldTarget):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_field_target import DashboardFieldTarget

        d = src_dict.copy()
        record_string_dashboard_tile_target = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union["DashboardFieldTarget", bool]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_dashboard_tile_target_type_0 = DashboardFieldTarget.from_dict(data)

                    return componentsschemas_dashboard_tile_target_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["DashboardFieldTarget", bool], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        record_string_dashboard_tile_target.additional_properties = additional_properties
        return record_string_dashboard_tile_target

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["DashboardFieldTarget", bool]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union["DashboardFieldTarget", bool]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
