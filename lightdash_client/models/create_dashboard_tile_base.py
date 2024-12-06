from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types import DashboardTileTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDashboardTileBase")


@_attrs_define
class CreateDashboardTileBase:
    """
    Attributes:
        w (float):
        h (float):
        y (float):
        x (float):
        type (DashboardTileTypes):
        tab_uuid (Union[Unset, str]):
        uuid (Union[Unset, str]):
    """

    w: float
    h: float
    y: float
    x: float
    type: DashboardTileTypes
    tab_uuid: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        w = self.w

        h = self.h

        y = self.y

        x = self.x

        type = self.type.value

        tab_uuid = self.tab_uuid

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "w": w,
                "h": h,
                "y": y,
                "x": x,
                "type": type,
            }
        )
        if tab_uuid is not UNSET:
            field_dict["tabUuid"] = tab_uuid
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        w = d.pop("w")

        h = d.pop("h")

        y = d.pop("y")

        x = d.pop("x")

        type = DashboardTileTypes(d.pop("type"))

        tab_uuid = d.pop("tabUuid", UNSET)

        uuid = d.pop("uuid", UNSET)

        create_dashboard_tile_base = cls(
            w=w,
            h=h,
            y=y,
            x=x,
            type=type,
            tab_uuid=tab_uuid,
            uuid=uuid,
        )

        create_dashboard_tile_base.additional_properties = d
        return create_dashboard_tile_base

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
