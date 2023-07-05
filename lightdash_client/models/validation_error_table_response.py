import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.validation_error_table_response_error_type import (
    ValidationErrorTableResponseErrorType,
)
from ..models.validation_error_table_response_source import (
    ValidationErrorTableResponseSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorTableResponse")


@attr.s(auto_attribs=True)
class ValidationErrorTableResponse:
    """
    Attributes:
        project_uuid (str):
        validation_id (float):
        created_at (datetime.datetime):
        error (str):
        error_type (ValidationErrorTableResponseErrorType):
        space_uuid (Union[Unset, str]):
        source (Union[Unset, ValidationErrorTableResponseSource]):
        name (Union[Unset, str]):
    """

    project_uuid: str
    validation_id: float
    created_at: datetime.datetime
    error: str
    error_type: ValidationErrorTableResponseErrorType
    space_uuid: Union[Unset, str] = UNSET
    source: Union[Unset, ValidationErrorTableResponseSource] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_uuid = self.project_uuid
        validation_id = self.validation_id
        created_at = self.created_at.isoformat()

        error = self.error
        error_type = self.error_type.value

        space_uuid = self.space_uuid
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectUuid": project_uuid,
                "validationId": validation_id,
                "createdAt": created_at,
                "error": error,
                "errorType": error_type,
            }
        )
        if space_uuid is not UNSET:
            field_dict["spaceUuid"] = space_uuid
        if source is not UNSET:
            field_dict["source"] = source
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_uuid = d.pop("projectUuid")

        validation_id = d.pop("validationId")

        created_at = isoparse(d.pop("createdAt"))

        error = d.pop("error")

        error_type = ValidationErrorTableResponseErrorType(d.pop("errorType"))

        space_uuid = d.pop("spaceUuid", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ValidationErrorTableResponseSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ValidationErrorTableResponseSource(_source)

        name = d.pop("name", UNSET)

        validation_error_table_response = cls(
            project_uuid=project_uuid,
            validation_id=validation_id,
            created_at=created_at,
            error=error,
            error_type=error_type,
            space_uuid=space_uuid,
            source=source,
            name=name,
        )

        validation_error_table_response.additional_properties = d
        return validation_error_table_response

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
