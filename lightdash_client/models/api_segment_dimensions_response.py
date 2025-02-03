from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_segment_dimensions_response_status import ApiSegmentDimensionsResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compiled_dimension import CompiledDimension


T = TypeVar("T", bound="ApiSegmentDimensionsResponse")


@_attrs_define
class ApiSegmentDimensionsResponse:
    """
    Attributes:
        results (List['CompiledDimension']):
        status (ApiSegmentDimensionsResponseStatus):
    """

    results: List["CompiledDimension"]
    status: ApiSegmentDimensionsResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.compiled_dimension import CompiledDimension

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

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
        from ..models.compiled_dimension import CompiledDimension

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = CompiledDimension.from_dict(results_item_data)

            results.append(results_item)

        status = ApiSegmentDimensionsResponseStatus(d.pop("status"))

        api_segment_dimensions_response = cls(
            results=results,
            status=status,
        )

        api_segment_dimensions_response.additional_properties = d
        return api_segment_dimensions_response

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
