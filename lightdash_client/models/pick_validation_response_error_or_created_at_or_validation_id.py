import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PickValidationResponseErrorOrCreatedAtOrValidationId")


@_attrs_define
class PickValidationResponseErrorOrCreatedAtOrValidationId:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        created_at (datetime.datetime):
        validation_id (float):
        error (str):
    """

    created_at: datetime.datetime
    validation_id: float
    error: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        validation_id = self.validation_id

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "validationId": validation_id,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        validation_id = d.pop("validationId")

        error = d.pop("error")

        pick_validation_response_error_or_created_at_or_validation_id = cls(
            created_at=created_at,
            validation_id=validation_id,
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
