import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_space_response_200_results_dashboards_item_updated_by_user import (
        UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser,
    )
    from ..models.update_space_response_200_results_dashboards_item_validation_errors_item import (
        UpdateSpaceResponse200ResultsDashboardsItemValidationErrorsItem,
    )


T = TypeVar("T", bound="UpdateSpaceResponse200ResultsDashboardsItem")


@attr.s(auto_attribs=True)
class UpdateSpaceResponse200ResultsDashboardsItem:
    """
    Attributes:
        name (str):
        organization_uuid (str):
        uuid (str):
        updated_at (datetime.datetime):
        project_uuid (str):
        space_uuid (str):
        views (float):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser]):
        first_viewed_at (Union[None, datetime.datetime, str]):
        pinned_list_uuid (Optional[str]):
        pinned_list_order (Optional[float]):
        validation_errors (Union[Unset, List['UpdateSpaceResponse200ResultsDashboardsItemValidationErrorsItem']]):
    """

    name: str
    organization_uuid: str
    uuid: str
    updated_at: datetime.datetime
    project_uuid: str
    space_uuid: str
    views: float
    first_viewed_at: Union[None, datetime.datetime, str]
    pinned_list_uuid: Optional[str]
    pinned_list_order: Optional[float]
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser"] = UNSET
    validation_errors: Union[Unset, List["UpdateSpaceResponse200ResultsDashboardsItemValidationErrorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_uuid = self.organization_uuid
        uuid = self.uuid
        updated_at = self.updated_at.isoformat()

        project_uuid = self.project_uuid
        space_uuid = self.space_uuid
        views = self.views
        description = self.description
        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        first_viewed_at: Union[None, str]
        if self.first_viewed_at is None:
            first_viewed_at = None

        elif isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()

        else:
            first_viewed_at = self.first_viewed_at

        pinned_list_uuid = self.pinned_list_uuid
        pinned_list_order = self.pinned_list_order
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
                "organizationUuid": organization_uuid,
                "uuid": uuid,
                "updatedAt": updated_at,
                "projectUuid": project_uuid,
                "spaceUuid": space_uuid,
                "views": views,
                "firstViewedAt": first_viewed_at,
                "pinnedListUuid": pinned_list_uuid,
                "pinnedListOrder": pinned_list_order,
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
        from ..models.update_space_response_200_results_dashboards_item_updated_by_user import (
            UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser,
        )
        from ..models.update_space_response_200_results_dashboards_item_validation_errors_item import (
            UpdateSpaceResponse200ResultsDashboardsItemValidationErrorsItem,
        )

        d = src_dict.copy()
        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        uuid = d.pop("uuid")

        updated_at = isoparse(d.pop("updatedAt"))

        project_uuid = d.pop("projectUuid")

        space_uuid = d.pop("spaceUuid")

        views = d.pop("views")

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdateSpaceResponse200ResultsDashboardsItemUpdatedByUser.from_dict(_updated_by_user)

        def _parse_first_viewed_at(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_viewed_at_type_0 = isoparse(data)

                return first_viewed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        first_viewed_at = _parse_first_viewed_at(d.pop("firstViewedAt"))

        pinned_list_uuid = d.pop("pinnedListUuid")

        pinned_list_order = d.pop("pinnedListOrder")

        validation_errors = []
        _validation_errors = d.pop("validationErrors", UNSET)
        for validation_errors_item_data in _validation_errors or []:
            validation_errors_item = UpdateSpaceResponse200ResultsDashboardsItemValidationErrorsItem.from_dict(
                validation_errors_item_data
            )

            validation_errors.append(validation_errors_item)

        update_space_response_200_results_dashboards_item = cls(
            name=name,
            organization_uuid=organization_uuid,
            uuid=uuid,
            updated_at=updated_at,
            project_uuid=project_uuid,
            space_uuid=space_uuid,
            views=views,
            description=description,
            updated_by_user=updated_by_user,
            first_viewed_at=first_viewed_at,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
            validation_errors=validation_errors,
        )

        update_space_response_200_results_dashboards_item.additional_properties = d
        return update_space_response_200_results_dashboards_item

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
