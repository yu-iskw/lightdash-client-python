import datetime
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..models.space_query_chart_type import SpaceQueryChartType
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.space_query_updated_by_user import SpaceQueryUpdatedByUser
    from ..models.space_query_validation_errors_item import SpaceQueryValidationErrorsItem


T = TypeVar("T", bound="SpaceQuery")


@attr.s(auto_attribs=True)
class SpaceQuery:
    """
    Attributes:
        name (str):
        uuid (str):
        updated_at (datetime.datetime):
        space_uuid (str):
        views (float):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, SpaceQueryUpdatedByUser]):
        pinned_list_uuid (Optional[str]):
        pinned_list_order (Optional[float]):
        first_viewed_at (Union[None, datetime.datetime, str]):
        validation_errors (Union[Unset, List['SpaceQueryValidationErrorsItem']]):
        chart_type (Union[Unset, SpaceQueryChartType]):
    """

    name: str
    uuid: str
    updated_at: datetime.datetime
    space_uuid: str
    views: float
    pinned_list_uuid: Optional[str]
    pinned_list_order: Optional[float]
    first_viewed_at: Union[None, datetime.datetime, str]
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "SpaceQueryUpdatedByUser"] = UNSET
    validation_errors: Union[Unset, List["SpaceQueryValidationErrorsItem"]] = UNSET
    chart_type: Union[Unset, SpaceQueryChartType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        uuid = self.uuid
        updated_at = self.updated_at.isoformat()

        space_uuid = self.space_uuid
        views = self.views
        description = self.description
        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        pinned_list_uuid = self.pinned_list_uuid
        pinned_list_order = self.pinned_list_order
        first_viewed_at: Union[None, str]
        if self.first_viewed_at is None:
            first_viewed_at = None

        elif isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()

        else:
            first_viewed_at = self.first_viewed_at

        validation_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()

                validation_errors.append(validation_errors_item)

        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "updatedAt": updated_at,
                "spaceUuid": space_uuid,
                "views": views,
                "pinnedListUuid": pinned_list_uuid,
                "pinnedListOrder": pinned_list_order,
                "firstViewedAt": first_viewed_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.space_query_updated_by_user import SpaceQueryUpdatedByUser
        from ..models.space_query_validation_errors_item import SpaceQueryValidationErrorsItem

        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        updated_at = isoparse(d.pop("updatedAt"))

        space_uuid = d.pop("spaceUuid")

        views = d.pop("views")

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, SpaceQueryUpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = SpaceQueryUpdatedByUser.from_dict(_updated_by_user)

        pinned_list_uuid = d.pop("pinnedListUuid")

        pinned_list_order = d.pop("pinnedListOrder")

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

        validation_errors = []
        _validation_errors = d.pop("validationErrors", UNSET)
        for validation_errors_item_data in _validation_errors or []:
            validation_errors_item = SpaceQueryValidationErrorsItem.from_dict(validation_errors_item_data)

            validation_errors.append(validation_errors_item)

        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, SpaceQueryChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = SpaceQueryChartType(_chart_type)

        space_query = cls(
            name=name,
            uuid=uuid,
            updated_at=updated_at,
            space_uuid=space_uuid,
            views=views,
            description=description,
            updated_by_user=updated_by_user,
            pinned_list_uuid=pinned_list_uuid,
            pinned_list_order=pinned_list_order,
            first_viewed_at=first_viewed_at,
            validation_errors=validation_errors,
            chart_type=chart_type,
        )

        space_query.additional_properties = d
        return space_query

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
