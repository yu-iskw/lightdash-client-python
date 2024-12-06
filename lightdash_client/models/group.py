import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """
    Attributes:
        organization_uuid (str): The UUID of the organization that the group belongs to
        updated_by_user_uuid (Union[None, str]): The UUID of the user that last updated the group
        updated_at (datetime.datetime): The time that the group was last updated
        created_by_user_uuid (Union[None, str]): The UUID of the user that created the group
        created_at (datetime.datetime): The time that the group was created
        name (str): A friendly name for the group
        uuid (str): The group's UUID
    """

    organization_uuid: str
    updated_by_user_uuid: Union[None, str]
    updated_at: datetime.datetime
    created_by_user_uuid: Union[None, str]
    created_at: datetime.datetime
    name: str
    uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_uuid = self.organization_uuid

        updated_by_user_uuid: Union[None, str]
        updated_by_user_uuid = self.updated_by_user_uuid

        updated_at = self.updated_at.isoformat()

        created_by_user_uuid: Union[None, str]
        created_by_user_uuid = self.created_by_user_uuid

        created_at = self.created_at.isoformat()

        name = self.name

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationUuid": organization_uuid,
                "updatedByUserUuid": updated_by_user_uuid,
                "updatedAt": updated_at,
                "createdByUserUuid": created_by_user_uuid,
                "createdAt": created_at,
                "name": name,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_uuid = d.pop("organizationUuid")

        def _parse_updated_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_user_uuid = _parse_updated_by_user_uuid(d.pop("updatedByUserUuid"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_created_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_uuid = _parse_created_by_user_uuid(d.pop("createdByUserUuid"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        uuid = d.pop("uuid")

        group = cls(
            organization_uuid=organization_uuid,
            updated_by_user_uuid=updated_by_user_uuid,
            updated_at=updated_at,
            created_by_user_uuid=created_by_user_uuid,
            created_at=created_at,
            name=name,
            uuid=uuid,
        )

        group.additional_properties = d
        return group

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
