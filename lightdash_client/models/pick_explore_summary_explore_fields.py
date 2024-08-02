from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickExploreSummaryExploreFields")


@_attrs_define
class PickExploreSummaryExploreFields:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        label (str):
        tags (List[str]):
        group_label (Union[Unset, str]):
    """

    name: str
    label: str
    tags: List[str]
    group_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        label = self.label

        tags = self.tags

        group_label = self.group_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "tags": tags,
            }
        )
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        tags = cast(List[str], d.pop("tags"))

        group_label = d.pop("groupLabel", UNSET)

        pick_explore_summary_explore_fields = cls(
            name=name,
            label=label,
            tags=tags,
            group_label=group_label,
        )

        pick_explore_summary_explore_fields.additional_properties = d
        return pick_explore_summary_explore_fields

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
