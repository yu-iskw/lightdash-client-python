from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types import DashboardTileTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickDashboardTileExcludeKeyofDashboardTileProperties")


@_attrs_define
class PickDashboardTileExcludeKeyofDashboardTileProperties:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (DashboardTileTypes):
        x (float):
        y (float):
        h (float):
        w (float):
        uuid (Union[Unset, str]):
        tab_uuid (Union[Unset, str]):
    """

    type: DashboardTileTypes
    x: float
    y: float
    h: float
    w: float
    uuid: Union[Unset, str] = UNSET
    tab_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        x = self.x

        y = self.y

        h = self.h

        w = self.w

        uuid = self.uuid

        tab_uuid = self.tab_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "x": x,
                "y": y,
                "h": h,
                "w": w,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if tab_uuid is not UNSET:
            field_dict["tabUuid"] = tab_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DashboardTileTypes(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        h = d.pop("h")

        w = d.pop("w")

        uuid = d.pop("uuid", UNSET)

        tab_uuid = d.pop("tabUuid", UNSET)

        pick_dashboard_tile_exclude_keyof_dashboard_tile_properties = cls(
            type=type,
            x=x,
            y=y,
            h=h,
            w=w,
            uuid=uuid,
            tab_uuid=tab_uuid,
        )

        pick_dashboard_tile_exclude_keyof_dashboard_tile_properties.additional_properties = d
        return pick_dashboard_tile_exclude_keyof_dashboard_tile_properties

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
