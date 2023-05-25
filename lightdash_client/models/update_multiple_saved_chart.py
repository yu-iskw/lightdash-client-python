from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="UpdateMultipleSavedChart")


@attr.s(auto_attribs=True)
class UpdateMultipleSavedChart:
    """
    Attributes:
        uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, None, str]):
        space_uuid (Union[Unset, str]):
    """

    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    space_uuid: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        name = self.name
        description = self.description
        space_uuid = self.space_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if space_uuid is not UNSET:
            field_dict["spaceUuid"] = space_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        space_uuid = d.pop("spaceUuid", UNSET)

        update_multiple_saved_chart = cls(
            uuid=uuid,
            name=name,
            description=description,
            space_uuid=space_uuid,
        )

        return update_multiple_saved_chart