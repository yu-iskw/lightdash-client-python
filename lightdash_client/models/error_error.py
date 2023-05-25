from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.error_error_data import ErrorErrorData


T = TypeVar("T", bound="ErrorError")


@attr.s(auto_attribs=True)
class ErrorError:
    """
    Attributes:
        name (str):
        status_code (float):
        message (str):
        data (Union[Unset, ErrorErrorData]):
    """

    name: str
    status_code: float
    message: str
    data: Union[Unset, "ErrorErrorData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status_code = self.status_code
        message = self.message
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "statusCode": status_code,
                "message": message,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_error_data import ErrorErrorData

        d = src_dict.copy()
        name = d.pop("name")

        status_code = d.pop("statusCode")

        message = d.pop("message")

        _data = d.pop("data", UNSET)
        data: Union[Unset, ErrorErrorData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ErrorErrorData.from_dict(_data)

        error_error = cls(
            name=name,
            status_code=status_code,
            message=message,
            data=data,
        )

        error_error.additional_properties = d
        return error_error

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
