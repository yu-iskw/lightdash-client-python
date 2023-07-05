from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_space_access_item import CreateSpaceAccessItem


T = TypeVar("T", bound="CreateSpace")


@attr.s(auto_attribs=True)
class CreateSpace:
    """
    Attributes:
        name (str):
        access (Union[Unset, List['CreateSpaceAccessItem']]):
        is_private (Union[Unset, bool]):
    """

    name: str
    access: Union[Unset, List["CreateSpaceAccessItem"]] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            access = []
            for access_item_data in self.access:
                access_item = access_item_data.to_dict()

                access.append(access_item)

        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_space_access_item import CreateSpaceAccessItem

        d = src_dict.copy()
        name = d.pop("name")

        access = []
        _access = d.pop("access", UNSET)
        for access_item_data in _access or []:
            access_item = CreateSpaceAccessItem.from_dict(access_item_data)

            access.append(access_item)

        is_private = d.pop("isPrivate", UNSET)

        create_space = cls(
            name=name,
            access=access,
            is_private=is_private,
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
