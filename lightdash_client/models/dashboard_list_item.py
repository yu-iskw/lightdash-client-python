import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="DashboardListItem")


@attr.s(auto_attribs=True)
class DashboardListItem:
    """
    Attributes:
        uuid (str):
        name (str):
        updated_at (datetime.datetime):
        description (Union[Unset, None, str]):
    """

    uuid: str
    name: str
    updated_at: datetime.datetime
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        name = self.name
        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        name = d.pop("name")

        updated_at = isoparse(d.pop("updatedAt"))

        description = d.pop("description", UNSET)

        dashboard_list_item = cls(
            uuid=uuid,
            name=name,
            updated_at=updated_at,
            description=description,
        )

        dashboard_list_item.additional_properties = d
        return dashboard_list_item

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
