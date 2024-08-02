from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.and_filter_group import AndFilterGroup
    from ..models.or_filter_group import OrFilterGroup


T = TypeVar("T", bound="Filters")


@_attrs_define
class Filters:
    """
    Attributes:
        table_calculations (Union['AndFilterGroup', 'OrFilterGroup', Unset]):
        metrics (Union['AndFilterGroup', 'OrFilterGroup', Unset]):
        dimensions (Union['AndFilterGroup', 'OrFilterGroup', Unset]):
    """

    table_calculations: Union["AndFilterGroup", "OrFilterGroup", Unset] = UNSET
    metrics: Union["AndFilterGroup", "OrFilterGroup", Unset] = UNSET
    dimensions: Union["AndFilterGroup", "OrFilterGroup", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.or_filter_group import OrFilterGroup

        table_calculations: Union[Dict[str, Any], Unset]
        if isinstance(self.table_calculations, Unset):
            table_calculations = UNSET
        elif isinstance(self.table_calculations, OrFilterGroup):
            table_calculations = self.table_calculations.to_dict()
        else:
            table_calculations = self.table_calculations.to_dict()

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, OrFilterGroup):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics.to_dict()

        dimensions: Union[Dict[str, Any], Unset]
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET
        elif isinstance(self.dimensions, OrFilterGroup):
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
        from ..models.and_filter_group import AndFilterGroup
        from ..models.or_filter_group import OrFilterGroup

        d = src_dict.copy()

        def _parse_table_calculations(data: object) -> Union["AndFilterGroup", "OrFilterGroup", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_type_0 = OrFilterGroup.from_dict(data)

                return componentsschemas_filter_group_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_type_1 = AndFilterGroup.from_dict(data)

            return componentsschemas_filter_group_type_1

        table_calculations = _parse_table_calculations(d.pop("tableCalculations", UNSET))

        def _parse_metrics(data: object) -> Union["AndFilterGroup", "OrFilterGroup", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_type_0 = OrFilterGroup.from_dict(data)

                return componentsschemas_filter_group_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_type_1 = AndFilterGroup.from_dict(data)

            return componentsschemas_filter_group_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(data: object) -> Union["AndFilterGroup", "OrFilterGroup", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_type_0 = OrFilterGroup.from_dict(data)

                return componentsschemas_filter_group_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_type_1 = AndFilterGroup.from_dict(data)

            return componentsschemas_filter_group_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        filters = cls(
            table_calculations=table_calculations,
            metrics=metrics,
            dimensions=dimensions,
        )

        filters.additional_properties = d
        return filters

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
