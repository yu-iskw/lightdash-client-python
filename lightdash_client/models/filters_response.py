from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_group_response_type_0 import FilterGroupResponseType0
    from ..models.filter_group_response_type_1 import FilterGroupResponseType1


T = TypeVar("T", bound="FiltersResponse")


@_attrs_define
class FiltersResponse:
    """
    Attributes:
        table_calculations (Union['FilterGroupResponseType0', 'FilterGroupResponseType1', Unset]):
        metrics (Union['FilterGroupResponseType0', 'FilterGroupResponseType1', Unset]):
        dimensions (Union['FilterGroupResponseType0', 'FilterGroupResponseType1', Unset]):
    """

    table_calculations: Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset] = UNSET
    metrics: Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset] = UNSET
    dimensions: Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.filter_group_response_type_0 import FilterGroupResponseType0

        table_calculations: Union[Dict[str, Any], Unset]
        if isinstance(self.table_calculations, Unset):
            table_calculations = UNSET
        elif isinstance(self.table_calculations, FilterGroupResponseType0):
            table_calculations = self.table_calculations.to_dict()
        else:
            table_calculations = self.table_calculations.to_dict()

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, FilterGroupResponseType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics.to_dict()

        dimensions: Union[Dict[str, Any], Unset]
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET
        elif isinstance(self.dimensions, FilterGroupResponseType0):
            dimensions = self.dimensions.to_dict()
        else:
            dimensions = self.dimensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_calculations is not UNSET:
            field_dict["tableCalculations"] = table_calculations
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_group_response_type_0 import FilterGroupResponseType0
        from ..models.filter_group_response_type_1 import FilterGroupResponseType1

        d = src_dict.copy()

        def _parse_table_calculations(
            data: object,
        ) -> Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_response_type_0 = FilterGroupResponseType0.from_dict(data)

                return componentsschemas_filter_group_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_response_type_1 = FilterGroupResponseType1.from_dict(data)

            return componentsschemas_filter_group_response_type_1

        table_calculations = _parse_table_calculations(d.pop("tableCalculations", UNSET))

        def _parse_metrics(data: object) -> Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_response_type_0 = FilterGroupResponseType0.from_dict(data)

                return componentsschemas_filter_group_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_response_type_1 = FilterGroupResponseType1.from_dict(data)

            return componentsschemas_filter_group_response_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(data: object) -> Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_response_type_0 = FilterGroupResponseType0.from_dict(data)

                return componentsschemas_filter_group_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_response_type_1 = FilterGroupResponseType1.from_dict(data)

            return componentsschemas_filter_group_response_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        filters_response = cls(
            table_calculations=table_calculations,
            metrics=metrics,
            dimensions=dimensions,
        )

        filters_response.additional_properties = d
        return filters_response

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
