from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_preview_response_200_status import CreatePreviewResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePreviewResponse200")


@_attrs_define
class CreatePreviewResponse200:
    """
    Attributes:
        results (str):
        status (CreatePreviewResponse200Status):
    """

    results: str
    status: CreatePreviewResponse200Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = self.results

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
        d = src_dict.copy()
        results = d.pop("results")

        status = CreatePreviewResponse200Status(d.pop("status"))

        create_preview_response_200 = cls(
            results=results,
            status=status,
        )

        create_preview_response_200.additional_properties = d
        return create_preview_response_200

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
