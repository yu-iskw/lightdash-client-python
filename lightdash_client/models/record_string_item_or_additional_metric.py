from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metric import AdditionalMetric
    from ..models.custom_bin_dimension import CustomBinDimension
    from ..models.custom_sql_dimension import CustomSqlDimension
    from ..models.field import Field
    from ..models.metric import Metric
    from ..models.table_calculation import TableCalculation


T = TypeVar("T", bound="RecordStringItemOrAdditionalMetric")


@_attrs_define
class RecordStringItemOrAdditionalMetric:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[
        str,
        Union["AdditionalMetric", "CustomBinDimension", "CustomSqlDimension", "Field", "Metric", "TableCalculation"],
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.additional_metric import AdditionalMetric
        from ..models.custom_bin_dimension import CustomBinDimension
        from ..models.custom_sql_dimension import CustomSqlDimension
        from ..models.field import Field
        from ..models.metric import Metric
        from ..models.table_calculation import TableCalculation

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, Field):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, TableCalculation):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, AdditionalMetric):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CustomBinDimension):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, CustomSqlDimension):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_metric import AdditionalMetric
        from ..models.custom_bin_dimension import CustomBinDimension
        from ..models.custom_sql_dimension import CustomSqlDimension
        from ..models.field import Field
        from ..models.metric import Metric
        from ..models.table_calculation import TableCalculation

        d = src_dict.copy()
        record_string_item_or_additional_metric = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[
                "AdditionalMetric", "CustomBinDimension", "CustomSqlDimension", "Field", "Metric", "TableCalculation"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = Field.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = TableCalculation.from_dict(data)

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = AdditionalMetric.from_dict(data)

                    return additional_property_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_dimension_type_0 = CustomBinDimension.from_dict(data)

                    return componentsschemas_custom_dimension_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_dimension_type_1 = CustomSqlDimension.from_dict(data)

                    return componentsschemas_custom_dimension_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_4 = Metric.from_dict(data)

                return additional_property_type_4

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        record_string_item_or_additional_metric.additional_properties = additional_properties
        return record_string_item_or_additional_metric

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union["AdditionalMetric", "CustomBinDimension", "CustomSqlDimension", "Field", "Metric", "TableCalculation"]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: Union[
            "AdditionalMetric", "CustomBinDimension", "CustomSqlDimension", "Field", "Metric", "TableCalculation"
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
