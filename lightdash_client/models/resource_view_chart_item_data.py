import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.chart_kind import ChartKind
from ..models.chart_source_type import ChartSourceType
from ..models.chart_type import ChartType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_validation_response_error_or_created_at_or_validation_id import (
        PickValidationResponseErrorOrCreatedAtOrValidationId,
    )
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="ResourceViewChartItemData")


@_attrs_define
class ResourceViewChartItemData:
    """
    Attributes:
        name (str):
        uuid (str):
        space_uuid (str):
        pinned_list_uuid (Union[None, str]):
        slug (str):
        updated_at (datetime.datetime):
        views (float):
        first_viewed_at (Union[None, datetime.datetime, str]):
        pinned_list_order (Union[None, float]):
        description (Union[Unset, str]):
        chart_kind (Union[Unset, ChartKind]):
        updated_by_user (Union[Unset, UpdatedByUser]):
        validation_errors (Union[Unset, List['PickValidationResponseErrorOrCreatedAtOrValidationId']]):
        chart_type (Union[Unset, ChartType]):
        source (Union[Unset, ChartSourceType]):
    """

    name: str
    uuid: str
    space_uuid: str
    pinned_list_uuid: Union[None, str]
    slug: str
    updated_at: datetime.datetime
    views: float
    first_viewed_at: Union[None, datetime.datetime, str]
    pinned_list_order: Union[None, float]
    description: Union[Unset, str] = UNSET
    chart_kind: Union[Unset, ChartKind] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    validation_errors: Union[Unset, List["PickValidationResponseErrorOrCreatedAtOrValidationId"]] = UNSET
    chart_type: Union[Unset, ChartType] = UNSET
    source: Union[Unset, ChartSourceType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        uuid = self.uuid

        space_uuid = self.space_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        views = self.views

        first_viewed_at: Union[None, str]
        if isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()
        else:
            first_viewed_at = self.first_viewed_at

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        description = self.description

        chart_kind: Union[Unset, str] = UNSET
        if not isinstance(self.chart_kind, Unset):
            chart_kind = self.chart_kind.value

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        validation_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()
                validation_errors.append(validation_errors_item)

        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "spaceUuid": space_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "slug": slug,
                "updatedAt": updated_at,
                "views": views,
                "firstViewedAt": first_viewed_at,
                "pinnedListOrder": pinned_list_order,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if chart_kind is not UNSET:
            field_dict["chartKind"] = chart_kind
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_validation_response_error_or_created_at_or_validation_id import (
            PickValidationResponseErrorOrCreatedAtOrValidationId,
        )
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        space_uuid = d.pop("spaceUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        views = d.pop("views")

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

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        description = d.pop("description", UNSET)

        _chart_kind = d.pop("chartKind", UNSET)
        chart_kind: Union[Unset, ChartKind]
        if isinstance(_chart_kind, Unset):
            chart_kind = UNSET
        else:
            chart_kind = ChartKind(_chart_kind)

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

        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, ChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ChartType(_chart_type)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ChartSourceType]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ChartSourceType(_source)

        resource_view_chart_item_data = cls(
            name=name,
            uuid=uuid,
            space_uuid=space_uuid,
            pinned_list_uuid=pinned_list_uuid,
            slug=slug,
            updated_at=updated_at,
            views=views,
            first_viewed_at=first_viewed_at,
            pinned_list_order=pinned_list_order,
            description=description,
            chart_kind=chart_kind,
            updated_by_user=updated_by_user,
            validation_errors=validation_errors,
            chart_type=chart_type,
            source=source,
        )

        resource_view_chart_item_data.additional_properties = d
        return resource_view_chart_item_data

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
