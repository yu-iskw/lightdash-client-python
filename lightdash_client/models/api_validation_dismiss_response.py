from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.api_validation_dismiss_response_status import ApiValidationDismissResponseStatus

T = TypeVar("T", bound="ApiValidationDismissResponse")


@attr.s(auto_attribs=True)
class ApiValidationDismissResponse:
    """
    Attributes:
        status (ApiValidationDismissResponseStatus):
    """

    status: ApiValidationDismissResponseStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = ApiValidationDismissResponseStatus(d.pop("status"))

        api_validation_dismiss_response = cls(
            status=status,
        )

        api_validation_dismiss_response.additional_properties = d
        return api_validation_dismiss_response

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
