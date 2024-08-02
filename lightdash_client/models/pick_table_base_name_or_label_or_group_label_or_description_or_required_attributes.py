from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_string_or_string_array import (
        RecordStringStringOrStringArray,
    )


T = TypeVar("T", bound="PickTableBaseNameOrLabelOrGroupLabelOrDescriptionOrRequiredAttributes")


@_attrs_define
class PickTableBaseNameOrLabelOrGroupLabelOrDescriptionOrRequiredAttributes:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        label (str):
        description (Union[Unset, str]):
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        group_label (Union[Unset, str]):
    """

    name: str
    label: str
    description: Union[Unset, str] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    group_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        label = self.label

        description = self.description

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        group_label = self.group_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_string_or_string_array import (
            RecordStringStringOrStringArray,
        )

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        description = d.pop("description", UNSET)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        group_label = d.pop("groupLabel", UNSET)

        pick_table_base_name_or_label_or_group_label_or_description_or_required_attributes = cls(
            name=name,
            label=label,
            description=description,
            required_attributes=required_attributes,
            group_label=group_label,
        )

        pick_table_base_name_or_label_or_group_label_or_description_or_required_attributes.additional_properties = d
        return pick_table_base_name_or_label_or_group_label_or_description_or_required_attributes

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
