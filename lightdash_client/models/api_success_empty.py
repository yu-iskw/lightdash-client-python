from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_success_empty_status import ApiSuccessEmptyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSuccessEmpty")


@_attrs_define
class ApiSuccessEmpty:
    """
    Attributes:
        status (ApiSuccessEmptyStatus):
        results (Union[Unset, Any]):
    """

    status: ApiSuccessEmptyStatus
    results: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        status = ApiSuccessEmptyStatus(d.pop("status"))

        results = d.pop("results", UNSET)

        api_success_empty = cls(
            status=status,
            results=results,
        )

        api_success_empty.additional_properties = d
        return api_success_empty

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
