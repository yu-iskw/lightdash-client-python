import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..models.chart_kind import ChartKind
from ..models.validation_error_type import ValidationErrorType
from ..models.validation_source_type import ValidationSourceType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ValidationErrorChartResponse")


@attr.s(auto_attribs=True)
class ValidationErrorChartResponse:
    """
    Attributes:
        project_uuid (str):
        error_type (ValidationErrorType):
        error (str):
        name (str):
        created_at (datetime.datetime):
        validation_id (float):
        chart_views (float):
        source (Union[Unset, ValidationSourceType]):
        space_uuid (Union[Unset, str]):
        last_updated_at (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, str]):
        field_name (Union[Unset, str]):
        chart_type (Union[Unset, ChartKind]):
        chart_uuid (Union[Unset, str]):
    """

    project_uuid: str
    error_type: ValidationErrorType
    error: str
    name: str
    created_at: datetime.datetime
    validation_id: float
    chart_views: float
    source: Union[Unset, ValidationSourceType] = UNSET
    space_uuid: Union[Unset, str] = UNSET
    last_updated_at: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    chart_type: Union[Unset, ChartKind] = UNSET
    chart_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_uuid = self.project_uuid
        error_type = self.error_type.value

        error = self.error
        name = self.name
        created_at = self.created_at.isoformat()

        validation_id = self.validation_id
        chart_views = self.chart_views
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        space_uuid = self.space_uuid
        last_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_at, Unset):
            last_updated_at = self.last_updated_at.isoformat()

        last_updated_by = self.last_updated_by
        field_name = self.field_name
        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        chart_uuid = self.chart_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectUuid": project_uuid,
                "errorType": error_type,
                "error": error,
                "name": name,
                "createdAt": created_at,
                "validationId": validation_id,
                "chartViews": chart_views,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if space_uuid is not UNSET:
            field_dict["spaceUuid"] = space_uuid
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if chart_uuid is not UNSET:
            field_dict["chartUuid"] = chart_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_uuid = d.pop("projectUuid")

        error_type = ValidationErrorType(d.pop("errorType"))

        error = d.pop("error")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        validation_id = d.pop("validationId")

        chart_views = d.pop("chartViews")

        _source = d.pop("source", UNSET)
        source: Union[Unset, ValidationSourceType]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ValidationSourceType(_source)

        space_uuid = d.pop("spaceUuid", UNSET)

        _last_updated_at = d.pop("lastUpdatedAt", UNSET)
        last_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = isoparse(_last_updated_at)

        last_updated_by = d.pop("lastUpdatedBy", UNSET)

        field_name = d.pop("fieldName", UNSET)

        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, ChartKind]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ChartKind(_chart_type)

        chart_uuid = d.pop("chartUuid", UNSET)

        validation_error_chart_response = cls(
            project_uuid=project_uuid,
            error_type=error_type,
            error=error,
            name=name,
            created_at=created_at,
            validation_id=validation_id,
            chart_views=chart_views,
            source=source,
            space_uuid=space_uuid,
            last_updated_at=last_updated_at,
            last_updated_by=last_updated_by,
            field_name=field_name,
            chart_type=chart_type,
            chart_uuid=chart_uuid,
        )

        validation_error_chart_response.additional_properties = d
        return validation_error_chart_response

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
