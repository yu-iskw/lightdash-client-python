from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_tile_types import DashboardTileTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequiredCreateDashboardTileBase")


@_attrs_define
class RequiredCreateDashboardTileBase:
    """Make all properties in T required

    Attributes:
        uuid (str):
        type (DashboardTileTypes):
        x (float):
        y (float):
        h (float):
        w (float):
        tab_uuid (Union[Unset, str]):
    """

    uuid: str
    type: DashboardTileTypes
    x: float
    y: float
    h: float
    w: float
    tab_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid

        type = self.type.value

        x = self.x

        y = self.y

        h = self.h

        w = self.w

        tab_uuid = self.tab_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "type": type,
                "x": x,
                "y": y,
                "h": h,
                "w": w,
            }
        )
        if tab_uuid is not UNSET:
            field_dict["tabUuid"] = tab_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        type = DashboardTileTypes(d.pop("type"))

        x = d.pop("x")

        y = d.pop("y")

        h = d.pop("h")

        w = d.pop("w")

        tab_uuid = d.pop("tabUuid", UNSET)

        required_create_dashboard_tile_base = cls(
            uuid=uuid,
            type=type,
            x=x,
            y=y,
            h=h,
            w=w,
            tab_uuid=tab_uuid,
        )

        required_create_dashboard_tile_base.additional_properties = d
        return required_create_dashboard_tile_base

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