from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PivotConfig")


@_attrs_define
class PivotConfig:
    """
    Attributes:
        metrics_as_rows (bool):
        pivot_dimensions (List[str]):
        row_totals (Union[Unset, bool]):
        column_totals (Union[Unset, bool]):
        summable_metric_field_ids (Union[Unset, List[str]]):
        hidden_metric_field_ids (Union[Unset, List[str]]):
        column_order (Union[Unset, List[str]]):
    """

    metrics_as_rows: bool
    pivot_dimensions: List[str]
    row_totals: Union[Unset, bool] = UNSET
    column_totals: Union[Unset, bool] = UNSET
    summable_metric_field_ids: Union[Unset, List[str]] = UNSET
    hidden_metric_field_ids: Union[Unset, List[str]] = UNSET
    column_order: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_as_rows = self.metrics_as_rows

        pivot_dimensions = self.pivot_dimensions

        row_totals = self.row_totals

        column_totals = self.column_totals

        summable_metric_field_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.summable_metric_field_ids, Unset):
            summable_metric_field_ids = self.summable_metric_field_ids

        hidden_metric_field_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hidden_metric_field_ids, Unset):
            hidden_metric_field_ids = self.hidden_metric_field_ids

        column_order: Union[Unset, List[str]] = UNSET
        if not isinstance(self.column_order, Unset):
            column_order = self.column_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricsAsRows": metrics_as_rows,
                "pivotDimensions": pivot_dimensions,
            }
        )
        if row_totals is not UNSET:
            field_dict["rowTotals"] = row_totals
        if column_totals is not UNSET:
            field_dict["columnTotals"] = column_totals
        if summable_metric_field_ids is not UNSET:
            field_dict["summableMetricFieldIds"] = summable_metric_field_ids
        if hidden_metric_field_ids is not UNSET:
            field_dict["hiddenMetricFieldIds"] = hidden_metric_field_ids
        if column_order is not UNSET:
            field_dict["columnOrder"] = column_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metrics_as_rows = d.pop("metricsAsRows")

        pivot_dimensions = cast(List[str], d.pop("pivotDimensions"))

        row_totals = d.pop("rowTotals", UNSET)

        column_totals = d.pop("columnTotals", UNSET)

        summable_metric_field_ids = cast(List[str], d.pop("summableMetricFieldIds", UNSET))

        hidden_metric_field_ids = cast(List[str], d.pop("hiddenMetricFieldIds", UNSET))

        column_order = cast(List[str], d.pop("columnOrder", UNSET))

        pivot_config = cls(
            metrics_as_rows=metrics_as_rows,
            pivot_dimensions=pivot_dimensions,
            row_totals=row_totals,
            column_totals=column_totals,
            summable_metric_field_ids=summable_metric_field_ids,
            hidden_metric_field_ids=hidden_metric_field_ids,
            column_order=column_order,
        )

        pivot_config.additional_properties = d
        return pivot_config

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
