import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dashboard_tile_types import DashboardTileTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_validation_response_error_or_created_at_or_validation_id import (
        PickValidationResponseErrorOrCreatedAtOrValidationId,
    )
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="DashboardBasicDetailsWithTileTypes")


@_attrs_define
class DashboardBasicDetailsWithTileTypes:
    """
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
        tile_types (List[DashboardTileTypes]):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
        validation_errors (Union[Unset, List['PickValidationResponseErrorOrCreatedAtOrValidationId']]):
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
    tile_types: List[DashboardTileTypes]
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    validation_errors: Union[Unset, List["PickValidationResponseErrorOrCreatedAtOrValidationId"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_validation_response_error_or_created_at_or_validation_id import (
            PickValidationResponseErrorOrCreatedAtOrValidationId,
        )
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

        tile_types = []
        for tile_types_item_data in self.tile_types:
            tile_types_item = tile_types_item_data.value
            tile_types.append(tile_types_item)

        description = self.description

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        validation_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()
                validation_errors.append(validation_errors_item)

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
                "tileTypes": tile_types,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_validation_response_error_or_created_at_or_validation_id import (
            PickValidationResponseErrorOrCreatedAtOrValidationId,
        )
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

        tile_types = []
        _tile_types = d.pop("tileTypes")
        for tile_types_item_data in _tile_types:
            tile_types_item = DashboardTileTypes(tile_types_item_data)

            tile_types.append(tile_types_item)

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        validation_errors = []
        _validation_errors = d.pop("validationErrors", UNSET)
        for validation_errors_item_data in _validation_errors or []:
            validation_errors_item = PickValidationResponseErrorOrCreatedAtOrValidationId.from_dict(
                validation_errors_item_data
            )

            validation_errors.append(validation_errors_item)

        dashboard_basic_details_with_tile_types = cls(
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
            tile_types=tile_types,
            description=description,
            updated_by_user=updated_by_user,
            validation_errors=validation_errors,
        )

        dashboard_basic_details_with_tile_types.additional_properties = d
        return dashboard_basic_details_with_tile_types

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
