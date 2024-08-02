from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_scheduler_response_201_status import (
    DeleteSchedulerResponse201Status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSchedulerResponse201")


@_attrs_define
class DeleteSchedulerResponse201:
    """
    Attributes:
        status (DeleteSchedulerResponse201Status):
        results (Union[Unset, Any]):
    """

    status: DeleteSchedulerResponse201Status
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
        status = DeleteSchedulerResponse201Status(d.pop("status"))

        results = d.pop("results", UNSET)

        delete_scheduler_response_201 = cls(
            status=status,
            results=results,
        )

        delete_scheduler_response_201.additional_properties = d
        return delete_scheduler_response_201

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
