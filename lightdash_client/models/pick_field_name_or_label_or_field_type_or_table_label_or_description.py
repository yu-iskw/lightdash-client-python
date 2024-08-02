from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_type import FieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickFieldNameOrLabelOrFieldTypeOrTableLabelOrDescription")


@_attrs_define
class PickFieldNameOrLabelOrFieldTypeOrTableLabelOrDescription:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        label (str):
        field_type (FieldType):
        table_label (str):
        description (Union[Unset, str]):
    """

    name: str
    label: str
    field_type: FieldType
    table_label: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        label = self.label

        field_type = self.field_type.value

        table_label = self.table_label

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "fieldType": field_type,
                "tableLabel": table_label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        field_type = FieldType(d.pop("fieldType"))

        table_label = d.pop("tableLabel")

        description = d.pop("description", UNSET)

        pick_field_name_or_label_or_field_type_or_table_label_or_description = cls(
            name=name,
            label=label,
            field_type=field_type,
            table_label=table_label,
            description=description,
        )

        pick_field_name_or_label_or_field_type_or_table_label_or_description.additional_properties = d
        return pick_field_name_or_label_or_field_type_or_table_label_or_description

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
