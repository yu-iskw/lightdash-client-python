import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="GetGroupResponse200Results")


@attr.s(auto_attribs=True)
class GetGroupResponse200Results:
    """
    Attributes:
        organization_uuid (str): The UUID of the organization that the group belongs to
        created_at (datetime.datetime): The time that the group was created
        name (str): A friendly name for the group
        uuid (str): The group's UUID
    """

    organization_uuid: str
    created_at: datetime.datetime
    name: str
    uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_uuid = self.organization_uuid
        created_at = self.created_at.isoformat()

        name = self.name
        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationUuid": organization_uuid,
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

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        uuid = d.pop("uuid")

        get_group_response_200_results = cls(
            organization_uuid=organization_uuid,
            created_at=created_at,
            name=name,
            uuid=uuid,
        )

        get_group_response_200_results.additional_properties = d
        return get_group_response_200_results

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
