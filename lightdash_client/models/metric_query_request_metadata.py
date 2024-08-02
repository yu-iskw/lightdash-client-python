from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pick_compiled_dimension_label_or_name import (
        PickCompiledDimensionLabelOrName,
    )


T = TypeVar("T", bound="MetricQueryRequestMetadata")


@_attrs_define
class MetricQueryRequestMetadata:
    """
    Attributes:
        has_a_date_dimension (PickCompiledDimensionLabelOrName): From T, pick a set of properties whose keys are in the
            union K
    """

    has_a_date_dimension: "PickCompiledDimensionLabelOrName"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_a_date_dimension = self.has_a_date_dimension.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hasADateDimension": has_a_date_dimension,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_compiled_dimension_label_or_name import (
            PickCompiledDimensionLabelOrName,
        )

        d = src_dict.copy()
        has_a_date_dimension = PickCompiledDimensionLabelOrName.from_dict(d.pop("hasADateDimension"))

        metric_query_request_metadata = cls(
            has_a_date_dimension=has_a_date_dimension,
        )

        metric_query_request_metadata.additional_properties = d
        return metric_query_request_metadata

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
