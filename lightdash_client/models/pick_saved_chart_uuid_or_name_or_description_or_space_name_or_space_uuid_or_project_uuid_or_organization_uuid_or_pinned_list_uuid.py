from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar(
    "T",
    bound="PickSavedChartUuidOrNameOrDescriptionOrSpaceNameOrSpaceUuidOrProjectUuidOrOrganizationUuidOrPinnedListUuid",
)


@attr.s(auto_attribs=True)
class PickSavedChartUuidOrNameOrDescriptionOrSpaceNameOrSpaceUuidOrProjectUuidOrOrganizationUuidOrPinnedListUuid:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        organization_uuid (str):
        uuid (str):
        project_uuid (str):
        space_uuid (str):
        space_name (str):
        description (Union[Unset, str]):
        pinned_list_uuid (Optional[str]):
    """

    name: str
    organization_uuid: str
    uuid: str
    project_uuid: str
    space_uuid: str
    space_name: str
    pinned_list_uuid: Optional[str]
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_uuid = self.organization_uuid
        uuid = self.uuid
        project_uuid = self.project_uuid
        space_uuid = self.space_uuid
        space_name = self.space_name
        description = self.description
        pinned_list_uuid = self.pinned_list_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationUuid": organization_uuid,
                "uuid": uuid,
                "projectUuid": project_uuid,
                "spaceUuid": space_uuid,
                "spaceName": space_name,
                "pinnedListUuid": pinned_list_uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        uuid = d.pop("uuid")

        project_uuid = d.pop("projectUuid")

        space_uuid = d.pop("spaceUuid")

        space_name = d.pop("spaceName")

        description = d.pop("description", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid")

        pick_saved_chart_uuid_or_name_or_description_or_space_name_or_space_uuid_or_project_uuid_or_organization_uuid_or_pinned_list_uuid = cls(
            name=name,
            organization_uuid=organization_uuid,
            uuid=uuid,
            project_uuid=project_uuid,
            space_uuid=space_uuid,
            space_name=space_name,
            description=description,
            pinned_list_uuid=pinned_list_uuid,
        )

        pick_saved_chart_uuid_or_name_or_description_or_space_name_or_space_uuid_or_project_uuid_or_organization_uuid_or_pinned_list_uuid.additional_properties = (
            d
        )
        return pick_saved_chart_uuid_or_name_or_description_or_space_name_or_space_uuid_or_project_uuid_or_organization_uuid_or_pinned_list_uuid

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
