from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ApiErrorPayloadError")


@attr.s(auto_attribs=True)
class ApiErrorPayloadError:
    """
    Attributes:
        name (str): Unique name for the type of error
        status_code (float): HTTP status code
        data (Union[Unset, Any]): Optional data containing details of the error
        message (Union[Unset, str]): A friendly message summarising the error
    """

    name: str
    status_code: float
    data: Union[Unset, Any] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status_code = self.status_code
        data = self.data
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "statusCode": status_code,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        status_code = d.pop("statusCode")

        data = d.pop("data", UNSET)

        message = d.pop("message", UNSET)

        api_error_payload_error = cls(
            name=name,
            status_code=status_code,
            data=data,
            message=message,
        )

        api_error_payload_error.additional_properties = d
        return api_error_payload_error

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
