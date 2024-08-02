import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.validation_error_type import ValidationErrorType
from ..models.validation_source_type import ValidationSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationResponseBase")


@_attrs_define
class ValidationResponseBase:
    """
    Attributes:
        project_uuid (str):
        error_type (ValidationErrorType):
        error (str):
        name (str):
        created_at (datetime.datetime):
        validation_id (float):
        source (Union[Unset, ValidationSourceType]):
        space_uuid (Union[Unset, str]):
    """

    project_uuid: str
    error_type: ValidationErrorType
    error: str
    name: str
    created_at: datetime.datetime
    validation_id: float
    source: Union[Unset, ValidationSourceType] = UNSET
    space_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_uuid = self.project_uuid

        error_type = self.error_type.value

        error = self.error

        name = self.name

        created_at = self.created_at.isoformat()

        validation_id = self.validation_id

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        space_uuid = self.space_uuid

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
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if space_uuid is not UNSET:
            field_dict["spaceUuid"] = space_uuid

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

        _source = d.pop("source", UNSET)
        source: Union[Unset, ValidationSourceType]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ValidationSourceType(_source)

        space_uuid = d.pop("spaceUuid", UNSET)

        validation_response_base = cls(
            project_uuid=project_uuid,
            error_type=error_type,
            error=error,
            name=name,
            created_at=created_at,
            validation_id=validation_id,
            source=source,
            space_uuid=space_uuid,
        )

        validation_response_base.additional_properties = d
        return validation_response_base

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
