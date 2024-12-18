from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitRepo")


@_attrs_define
class GitRepo:
    """
    Attributes:
        owner_login (str):
        full_name (str):
        name (str):
    """

    owner_login: str
    full_name: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_login = self.owner_login

        full_name = self.full_name

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerLogin": owner_login,
                "fullName": full_name,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_login = d.pop("ownerLogin")

        full_name = d.pop("fullName")

        name = d.pop("name")

        git_repo = cls(
            owner_login=owner_login,
            full_name=full_name,
            name=name,
        )

        git_repo.additional_properties = d
        return git_repo

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
