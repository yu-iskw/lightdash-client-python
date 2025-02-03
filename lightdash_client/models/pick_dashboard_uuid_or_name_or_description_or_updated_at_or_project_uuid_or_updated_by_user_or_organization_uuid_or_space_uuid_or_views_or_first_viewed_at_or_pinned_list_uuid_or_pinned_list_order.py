import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar(
    "T",
    bound="PickDashboardUuidOrNameOrDescriptionOrUpdatedAtOrProjectUuidOrUpdatedByUserOrOrganizationUuidOrSpaceUuidOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrder",
)


@_attrs_define
class PickDashboardUuidOrNameOrDescriptionOrUpdatedAtOrProjectUuidOrUpdatedByUserOrOrganizationUuidOrSpaceUuidOrViewsOrFirstViewedAtOrPinnedListUuidOrPinnedListOrder:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        project_uuid (str):
        uuid (str):
        space_uuid (str):
        organization_uuid (str):
        pinned_list_uuid (Union[None, str]):
        pinned_list_order (Union[None, float]):
        updated_at (datetime.datetime):
        views (float):
        first_viewed_at (Union[None, datetime.datetime, str]):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
    """

    name: str
    project_uuid: str
    uuid: str
    space_uuid: str
    organization_uuid: str
    pinned_list_uuid: Union[None, str]
    pinned_list_order: Union[None, float]
    updated_at: datetime.datetime
    views: float
    first_viewed_at: Union[None, datetime.datetime, str]
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.updated_by_user import UpdatedByUser

        name = self.name

        project_uuid = self.project_uuid

        uuid = self.uuid

        space_uuid = self.space_uuid

        organization_uuid = self.organization_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        updated_at = self.updated_at.isoformat()

        views = self.views

        first_viewed_at: Union[None, str]
        if isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()
        else:
            first_viewed_at = self.first_viewed_at

        description = self.description

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectUuid": project_uuid,
                "uuid": uuid,
                "spaceUuid": space_uuid,
                "organizationUuid": organization_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "pinnedListOrder": pinned_list_order,
                "updatedAt": updated_at,
                "views": views,
                "firstViewedAt": first_viewed_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        uuid = d.pop("uuid")

        space_uuid = d.pop("spaceUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        updated_at = isoparse(d.pop("updatedAt"))

        views = d.pop("views")

        def _parse_first_viewed_at(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_viewed_at_type_1 = isoparse(data)

                return first_viewed_at_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        first_viewed_at = _parse_first_viewed_at(d.pop("firstViewedAt"))

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        pick_dashboard_uuid_or_name_or_description_or_updated_at_or_project_uuid_or_updated_by_user_or_organization_uuid_or_space_uuid_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order = cls(
            name=name,
            project_uuid=project_uuid,
            uuid=uuid,
            space_uuid=space_uuid,
            organization_uuid=organization_uuid,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
            updated_at=updated_at,
            views=views,
            first_viewed_at=first_viewed_at,
            description=description,
            updated_by_user=updated_by_user,
        )

        pick_dashboard_uuid_or_name_or_description_or_updated_at_or_project_uuid_or_updated_by_user_or_organization_uuid_or_space_uuid_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order.additional_properties = d
        return pick_dashboard_uuid_or_name_or_description_or_updated_at_or_project_uuid_or_updated_by_user_or_organization_uuid_or_space_uuid_or_views_or_first_viewed_at_or_pinned_list_uuid_or_pinned_list_order

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
