from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditional_formatting_config_with_color_range import (
        ConditionalFormattingConfigWithColorRange,
    )
    from ..models.conditional_formatting_config_with_single_color import (
        ConditionalFormattingConfigWithSingleColor,
    )
    from ..models.record_string_column_properties import RecordStringColumnProperties


T = TypeVar("T", bound="TableChart")


@_attrs_define
class TableChart:
    """
    Attributes:
        metrics_as_rows (Union[Unset, bool]):
        conditional_formattings (Union[Unset, List[Union['ConditionalFormattingConfigWithColorRange',
            'ConditionalFormattingConfigWithSingleColor']]]):
        columns (Union[Unset, RecordStringColumnProperties]): Construct a type with a set of properties K of type T
        show_subtotals (Union[Unset, bool]):
        show_results_total (Union[Unset, bool]):
        hide_row_numbers (Union[Unset, bool]):
        show_table_names (Union[Unset, bool]):
        show_row_calculation (Union[Unset, bool]):
        show_column_calculation (Union[Unset, bool]):
    """

    metrics_as_rows: Union[Unset, bool] = UNSET
    conditional_formattings: Union[
        Unset, List[Union["ConditionalFormattingConfigWithColorRange", "ConditionalFormattingConfigWithSingleColor"]]
    ] = UNSET
    columns: Union[Unset, "RecordStringColumnProperties"] = UNSET
    show_subtotals: Union[Unset, bool] = UNSET
    show_results_total: Union[Unset, bool] = UNSET
    hide_row_numbers: Union[Unset, bool] = UNSET
    show_table_names: Union[Unset, bool] = UNSET
    show_row_calculation: Union[Unset, bool] = UNSET
    show_column_calculation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.conditional_formatting_config_with_single_color import (
            ConditionalFormattingConfigWithSingleColor,
        )

        metrics_as_rows = self.metrics_as_rows

        conditional_formattings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditional_formattings, Unset):
            conditional_formattings = []
            for conditional_formattings_item_data in self.conditional_formattings:
                conditional_formattings_item: Dict[str, Any]
                if isinstance(conditional_formattings_item_data, ConditionalFormattingConfigWithSingleColor):
                    conditional_formattings_item = conditional_formattings_item_data.to_dict()
                else:
                    conditional_formattings_item = conditional_formattings_item_data.to_dict()

                conditional_formattings.append(conditional_formattings_item)

        columns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns.to_dict()

        show_subtotals = self.show_subtotals

        show_results_total = self.show_results_total

        hide_row_numbers = self.hide_row_numbers

        show_table_names = self.show_table_names

        show_row_calculation = self.show_row_calculation

        show_column_calculation = self.show_column_calculation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_as_rows is not UNSET:
            field_dict["metricsAsRows"] = metrics_as_rows
        if conditional_formattings is not UNSET:
            field_dict["conditionalFormattings"] = conditional_formattings
        if columns is not UNSET:
            field_dict["columns"] = columns
        if show_subtotals is not UNSET:
            field_dict["showSubtotals"] = show_subtotals
        if show_results_total is not UNSET:
            field_dict["showResultsTotal"] = show_results_total
        if hide_row_numbers is not UNSET:
            field_dict["hideRowNumbers"] = hide_row_numbers
        if show_table_names is not UNSET:
            field_dict["showTableNames"] = show_table_names
        if show_row_calculation is not UNSET:
            field_dict["showRowCalculation"] = show_row_calculation
        if show_column_calculation is not UNSET:
            field_dict["showColumnCalculation"] = show_column_calculation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conditional_formatting_config_with_color_range import (
            ConditionalFormattingConfigWithColorRange,
        )
        from ..models.conditional_formatting_config_with_single_color import (
            ConditionalFormattingConfigWithSingleColor,
        )
        from ..models.record_string_column_properties import (
            RecordStringColumnProperties,
        )

        d = src_dict.copy()
        metrics_as_rows = d.pop("metricsAsRows", UNSET)

        conditional_formattings = []
        _conditional_formattings = d.pop("conditionalFormattings", UNSET)
        for conditional_formattings_item_data in _conditional_formattings or []:

            def _parse_conditional_formattings_item(
                data: object,
            ) -> Union["ConditionalFormattingConfigWithColorRange", "ConditionalFormattingConfigWithSingleColor"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_conditional_formatting_config_type_0 = (
                        ConditionalFormattingConfigWithSingleColor.from_dict(data)
                    )

                    return componentsschemas_conditional_formatting_config_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_conditional_formatting_config_type_1 = (
                    ConditionalFormattingConfigWithColorRange.from_dict(data)
                )

                return componentsschemas_conditional_formatting_config_type_1

            conditional_formattings_item = _parse_conditional_formattings_item(conditional_formattings_item_data)

            conditional_formattings.append(conditional_formattings_item)

        _columns = d.pop("columns", UNSET)
        columns: Union[Unset, RecordStringColumnProperties]
        if isinstance(_columns, Unset):
            columns = UNSET
        else:
            columns = RecordStringColumnProperties.from_dict(_columns)

        show_subtotals = d.pop("showSubtotals", UNSET)

        show_results_total = d.pop("showResultsTotal", UNSET)

        hide_row_numbers = d.pop("hideRowNumbers", UNSET)

        show_table_names = d.pop("showTableNames", UNSET)

        show_row_calculation = d.pop("showRowCalculation", UNSET)

        show_column_calculation = d.pop("showColumnCalculation", UNSET)

        table_chart = cls(
            metrics_as_rows=metrics_as_rows,
            conditional_formattings=conditional_formattings,
            columns=columns,
            show_subtotals=show_subtotals,
            show_results_total=show_results_total,
            hide_row_numbers=hide_row_numbers,
            show_table_names=show_table_names,
            show_row_calculation=show_row_calculation,
            show_column_calculation=show_column_calculation,
        )

        table_chart.additional_properties = d
        return table_chart

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
