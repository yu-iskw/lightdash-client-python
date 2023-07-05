from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UpdateSpaceJsonBody")


@attr.s(auto_attribs=True)
class UpdateSpaceJsonBody:
    """
    Attributes:
        is_private (bool):
        name (str):
    """

    is_private: bool
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_private = self.is_private
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isPrivate": is_private,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_private = d.pop("isPrivate")

        name = d.pop("name")

        update_space_json_body = cls(
            is_private=is_private,
            name=name,
        )

        update_space_json_body.additional_properties = d
        return update_space_json_body

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
