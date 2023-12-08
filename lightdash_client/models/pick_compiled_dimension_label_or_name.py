from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PickCompiledDimensionLabelOrName")


@attr.s(auto_attribs=True)
class PickCompiledDimensionLabelOrName:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        label (str):
        name (str):
    """

    label: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        name = d.pop("name")

        pick_compiled_dimension_label_or_name = cls(
            label=label,
            name=name,
        )

        pick_compiled_dimension_label_or_name.additional_properties = d
        return pick_compiled_dimension_label_or_name

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
