from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_create_user_attribute_response_status import ApiCreateUserAttributeResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_attribute import UserAttribute


T = TypeVar("T", bound="ApiCreateUserAttributeResponse")


@_attrs_define
class ApiCreateUserAttributeResponse:
    """
    Attributes:
        results (UserAttribute):
        status (ApiCreateUserAttributeResponseStatus):
    """

    results: "UserAttribute"
    status: ApiCreateUserAttributeResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.user_attribute import UserAttribute

        results = self.results.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_attribute import UserAttribute

        d = src_dict.copy()
        results = UserAttribute.from_dict(d.pop("results"))

        status = ApiCreateUserAttributeResponseStatus(d.pop("status"))

        api_create_user_attribute_response = cls(
            results=results,
            status=status,
        )

        api_create_user_attribute_response.additional_properties = d
        return api_create_user_attribute_response

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
