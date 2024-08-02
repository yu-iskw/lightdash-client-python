from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_highlight import SourceHighlight
    from ..models.source_range import SourceRange


T = TypeVar("T", bound="Source")


@_attrs_define
class Source:
    """
    Attributes:
        content (str):
        range_ (SourceRange):
        path (str):
        highlight (Union[Unset, SourceHighlight]):
    """

    content: str
    range_: "SourceRange"
    path: str
    highlight: Union[Unset, "SourceHighlight"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        range_ = self.range_.to_dict()

        path = self.path

        highlight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.highlight, Unset):
            highlight = self.highlight.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "range": range_,
                "path": path,
            }
        )
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.source_highlight import SourceHighlight
        from ..models.source_range import SourceRange

        d = src_dict.copy()
        content = d.pop("content")

        range_ = SourceRange.from_dict(d.pop("range"))

        path = d.pop("path")

        _highlight = d.pop("highlight", UNSET)
        highlight: Union[Unset, SourceHighlight]
        if isinstance(_highlight, Unset):
            highlight = UNSET
        else:
            highlight = SourceHighlight.from_dict(_highlight)

        source = cls(
            content=content,
            range_=range_,
            path=path,
            highlight=highlight,
        )

        source.additional_properties = d
        return source

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
