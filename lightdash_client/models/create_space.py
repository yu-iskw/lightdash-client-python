from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.space_share import SpaceShare


T = TypeVar("T", bound="CreateSpace")


@attr.s(auto_attribs=True)
class CreateSpace:
    """
    Attributes:
        name (str):
        is_private (Union[Unset, bool]):
        access (Union[Unset, List['SpaceShare']]):
    """

    name: str
    is_private: Union[Unset, bool] = UNSET
    access: Union[Unset, List["SpaceShare"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_private = self.is_private
        access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            access = []
            for access_item_data in self.access:
                access_item = access_item_data.to_dict()

                access.append(access_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.space_share import SpaceShare

        d = src_dict.copy()
        name = d.pop("name")

        is_private = d.pop("isPrivate", UNSET)

        access = []
        _access = d.pop("access", UNSET)
        for access_item_data in _access or []:
            access_item = SpaceShare.from_dict(access_item_data)

            access.append(access_item)

        create_space = cls(
            name=name,
            is_private=is_private,
            access=access,
        )

        create_space.additional_properties = d
        return create_space

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
