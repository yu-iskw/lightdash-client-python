from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pivot_reference import PivotReference


T = TypeVar("T", bound="SeriesEncode")


@_attrs_define
class SeriesEncode:
    """
    Attributes:
        y_ref (PivotReference):
        x_ref (PivotReference):
        y (Union[Unset, str]):
        x (Union[Unset, str]):
    """

    y_ref: "PivotReference"
    x_ref: "PivotReference"
    y: Union[Unset, str] = UNSET
    x: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        y_ref = self.y_ref.to_dict()

        x_ref = self.x_ref.to_dict()

        y = self.y

        x = self.x

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yRef": y_ref,
                "xRef": x_ref,
            }
        )
        if y is not UNSET:
            field_dict["y"] = y
        if x is not UNSET:
            field_dict["x"] = x

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pivot_reference import PivotReference

        d = src_dict.copy()
        y_ref = PivotReference.from_dict(d.pop("yRef"))

        x_ref = PivotReference.from_dict(d.pop("xRef"))

        y = d.pop("y", UNSET)

        x = d.pop("x", UNSET)

        series_encode = cls(
            y_ref=y_ref,
            x_ref=x_ref,
            y=y,
            x=x,
        )

        series_encode.additional_properties = d
        return series_encode

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
