from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.delete_validation_dismiss_response_200_status import DeleteValidationDismissResponse200Status

T = TypeVar("T", bound="DeleteValidationDismissResponse200")


@attr.s(auto_attribs=True)
class DeleteValidationDismissResponse200:
    """
    Attributes:
        status (DeleteValidationDismissResponse200Status):
    """

    status: DeleteValidationDismissResponse200Status
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
        status = DeleteValidationDismissResponse200Status(d.pop("status"))

        delete_validation_dismiss_response_200 = cls(
            status=status,
        )

        delete_validation_dismiss_response_200.additional_properties = d
        return delete_validation_dismiss_response_200

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