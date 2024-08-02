from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inline_error import InlineError


T = TypeVar("T", bound="PickExploreErrorSummaryExploreErrorFields")


@_attrs_define
class PickExploreErrorSummaryExploreErrorFields:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        label (str):
        tags (List[str]):
        errors (List['InlineError']):
        group_label (Union[Unset, str]):
    """

    name: str
    label: str
    tags: List[str]
    errors: List["InlineError"]
    group_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        label = self.label

        tags = self.tags

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        group_label = self.group_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "tags": tags,
                "errors": errors,
            }
        )
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inline_error import InlineError

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        tags = cast(List[str], d.pop("tags"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = InlineError.from_dict(errors_item_data)

            errors.append(errors_item)

        group_label = d.pop("groupLabel", UNSET)

        pick_explore_error_summary_explore_error_fields = cls(
            name=name,
            label=label,
            tags=tags,
            errors=errors,
            group_label=group_label,
        )

        pick_explore_error_summary_explore_error_fields.additional_properties = d
        return pick_explore_error_summary_explore_error_fields

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
