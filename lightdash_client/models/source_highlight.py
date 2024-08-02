from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.source_position import SourcePosition


T = TypeVar("T", bound="SourceHighlight")


@_attrs_define
class SourceHighlight:
    """
    Attributes:
        end (SourcePosition):
        start (SourcePosition):
    """

    end: "SourcePosition"
    start: "SourcePosition"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        source_highlight = cls(
            end=end,
            start=start,
        )

        source_highlight.additional_properties = d
        return source_highlight

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
