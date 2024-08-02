import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PickValidationResponseErrorOrCreatedAtOrValidationId")


@_attrs_define
class PickValidationResponseErrorOrCreatedAtOrValidationId:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        validation_id (float):
        created_at (datetime.datetime):
        error (str):
    """

    validation_id: float
    created_at: datetime.datetime
    error: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validation_id = self.validation_id

        created_at = self.created_at.isoformat()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "validationId": validation_id,
                "createdAt": created_at,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validation_id = d.pop("validationId")

        created_at = isoparse(d.pop("createdAt"))

        error = d.pop("error")

        pick_validation_response_error_or_created_at_or_validation_id = cls(
            validation_id=validation_id,
            created_at=created_at,
            error=error,
        )

        pick_validation_response_error_or_created_at_or_validation_id.additional_properties = d
        return pick_validation_response_error_or_created_at_or_validation_id

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
