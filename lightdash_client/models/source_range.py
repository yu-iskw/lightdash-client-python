from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_position import SourcePosition


T = TypeVar("T", bound="SourceRange")


@_attrs_define
class SourceRange:
    """
    Attributes:
        end (SourcePosition):
        start (SourcePosition):
    """

    end: "SourcePosition"
    start: "SourcePosition"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.source_position import SourcePosition

        end = self.end.to_dict()

        start = self.start.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.source_position import SourcePosition

        d = src_dict.copy()
        end = SourcePosition.from_dict(d.pop("end"))

        start = SourcePosition.from_dict(d.pop("start"))

        source_range = cls(
            end=end,
            start=start,
        )

        source_range.additional_properties = d
        return source_range

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
