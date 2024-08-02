from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compile_query_response_200_status import CompileQueryResponse200Status

T = TypeVar("T", bound="CompileQueryResponse200")


@_attrs_define
class CompileQueryResponse200:
    """
    Attributes:
        results (str):
        status (CompileQueryResponse200Status):
    """

    results: str
    status: CompileQueryResponse200Status
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

        status = CompileQueryResponse200Status(d.pop("status"))

        compile_query_response_200 = cls(
            results=results,
            status=status,
        )

        compile_query_response_200.additional_properties = d
        return compile_query_response_200

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
