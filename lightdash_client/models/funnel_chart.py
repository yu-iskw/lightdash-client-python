from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.funnel_chart_data_input import FunnelChartDataInput
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_string_series_metadata import RecordStringSeriesMetadata


T = TypeVar("T", bound="FunnelChart")


@_attrs_define
class FunnelChart:
    """
    Attributes:
        metadata (Union[Unset, RecordStringSeriesMetadata]): Construct a type with a set of properties K of type T
        field_id (Union[Unset, str]):
        data_input (Union[Unset, FunnelChartDataInput]):
    """

    metadata: Union[Unset, "RecordStringSeriesMetadata"] = UNSET
    field_id: Union[Unset, str] = UNSET
    data_input: Union[Unset, FunnelChartDataInput] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_id = self.field_id

        data_input: Union[Unset, str] = UNSET
        if not isinstance(self.data_input, Unset):
            data_input = self.data_input.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if data_input is not UNSET:
            field_dict["dataInput"] = data_input

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_series_metadata import RecordStringSeriesMetadata

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, RecordStringSeriesMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RecordStringSeriesMetadata.from_dict(_metadata)

        field_id = d.pop("fieldId", UNSET)

        _data_input = d.pop("dataInput", UNSET)
        data_input: Union[Unset, FunnelChartDataInput]
        if isinstance(_data_input, Unset):
            data_input = UNSET
        else:
            data_input = FunnelChartDataInput(_data_input)

        funnel_chart = cls(
            metadata=metadata,
            field_id=field_id,
            data_input=data_input,
        )

        funnel_chart.additional_properties = d
        return funnel_chart

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
