from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="PickSpaceNameOrIsPrivate")


@attr.s(auto_attribs=True)
class PickSpaceNameOrIsPrivate:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        is_private (bool):
    """

    name: str
    is_private: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "isPrivate": is_private,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        is_private = d.pop("isPrivate")

        pick_space_name_or_is_private = cls(
            name=name,
            is_private=is_private,
        )

        pick_space_name_or_is_private.additional_properties = d
        return pick_space_name_or_is_private

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
