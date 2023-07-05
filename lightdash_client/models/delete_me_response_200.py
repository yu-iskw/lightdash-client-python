from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delete_me_response_200_status import DeleteMeResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteMeResponse200")


@attr.s(auto_attribs=True)
class DeleteMeResponse200:
    """
    Attributes:
        status (DeleteMeResponse200Status):
        results (Union[Unset, Any]):
    """

    status: DeleteMeResponse200Status
    results: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        results = self.results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = DeleteMeResponse200Status(d.pop("status"))

        results = d.pop("results", UNSET)

        delete_me_response_200 = cls(
            status=status,
            results=results,
        )

        delete_me_response_200.additional_properties = d
        return delete_me_response_200

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
