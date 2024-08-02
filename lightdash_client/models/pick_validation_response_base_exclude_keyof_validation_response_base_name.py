import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.validation_error_type import ValidationErrorType
from ..models.validation_source_type import ValidationSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickValidationResponseBaseExcludeKeyofValidationResponseBaseName")


@_attrs_define
class PickValidationResponseBaseExcludeKeyofValidationResponseBaseName:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        project_uuid (str):
        validation_id (float):
        created_at (datetime.datetime):
        error (str):
        error_type (ValidationErrorType):
        space_uuid (Union[Unset, str]):
        source (Union[Unset, ValidationSourceType]):
    """

    project_uuid: str
    validation_id: float
    created_at: datetime.datetime
    error: str
    error_type: ValidationErrorType
    space_uuid: Union[Unset, str] = UNSET
    source: Union[Unset, ValidationSourceType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_uuid = d.pop("projectUuid")

        validation_id = d.pop("validationId")

        created_at = isoparse(d.pop("createdAt"))

        error = d.pop("error")

        error_type = ValidationErrorType(d.pop("errorType"))

        space_uuid = d.pop("spaceUuid", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ValidationSourceType]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ValidationSourceType(_source)

        pick_validation_response_base_exclude_keyof_validation_response_base_name = cls(
            project_uuid=project_uuid,
            validation_id=validation_id,
            created_at=created_at,
            error=error,
            error_type=error_type,
            space_uuid=space_uuid,
            source=source,
        )

        pick_validation_response_base_exclude_keyof_validation_response_base_name.additional_properties = d
        return pick_validation_response_base_exclude_keyof_validation_response_base_name

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
