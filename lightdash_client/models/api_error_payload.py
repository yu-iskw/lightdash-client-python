from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_error_payload_status import ApiErrorPayloadStatus

if TYPE_CHECKING:
    from ..models.api_error_payload_error import ApiErrorPayloadError


T = TypeVar("T", bound="ApiErrorPayload")


@_attrs_define
class ApiErrorPayload:
    """The Error object is returned from the api any time there is an error.
    The message contains

        Attributes:
            error (ApiErrorPayloadError):
            status (ApiErrorPayloadStatus):
    """

    error: "ApiErrorPayloadError"
    status: ApiErrorPayloadStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_error_payload_error import ApiErrorPayloadError

        d = src_dict.copy()
        error = ApiErrorPayloadError.from_dict(d.pop("error"))

        status = ApiErrorPayloadStatus(d.pop("status"))

        api_error_payload = cls(
            error=error,
            status=status,
        )

        api_error_payload.additional_properties = d
        return api_error_payload

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
