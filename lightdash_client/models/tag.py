import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
        PickLightdashUserUserUuidOrFirstNameOrLastName,
    )


T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """
    Attributes:
        created_by (Union['PickLightdashUserUserUuidOrFirstNameOrLastName', None]):
        created_at (datetime.datetime):
        color (str):
        name (str):
        project_uuid (str):
        tag_uuid (str):
    """

    created_by: Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None]
    created_at: datetime.datetime
    color: str
    name: str
    project_uuid: str
    tag_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )

        created_by: Union[Dict[str, Any], None]
        if isinstance(self.created_by, PickLightdashUserUserUuidOrFirstNameOrLastName):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        created_at = self.created_at.isoformat()

        color = self.color

        name = self.name

        project_uuid = self.project_uuid

        tag_uuid = self.tag_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdBy": created_by,
                "createdAt": created_at,
                "color": color,
                "name": name,
                "projectUuid": project_uuid,
                "tagUuid": tag_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )

        d = src_dict.copy()

        def _parse_created_by(data: object) -> Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_1 = PickLightdashUserUserUuidOrFirstNameOrLastName.from_dict(data)

                return created_by_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None], data)

        created_by = _parse_created_by(d.pop("createdBy"))

        created_at = isoparse(d.pop("createdAt"))

        color = d.pop("color")

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        tag_uuid = d.pop("tagUuid")

        tag = cls(
            created_by=created_by,
            created_at=created_at,
            color=color,
            name=name,
            project_uuid=project_uuid,
            tag_uuid=tag_uuid,
        )

        tag.additional_properties = d
        return tag

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
