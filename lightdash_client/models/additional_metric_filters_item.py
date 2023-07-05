from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.additional_metric_filters_item_operator import (
    AdditionalMetricFiltersItemOperator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.additional_metric_filters_item_target import (
        AdditionalMetricFiltersItemTarget,
    )


T = TypeVar("T", bound="AdditionalMetricFiltersItem")


@attr.s(auto_attribs=True)
class AdditionalMetricFiltersItem:
    """
    Attributes:
        operator (AdditionalMetricFiltersItemOperator):
        id (str):
        target (AdditionalMetricFiltersItemTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
    """

    operator: AdditionalMetricFiltersItemOperator
    id: str
    target: "AdditionalMetricFiltersItemTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id
        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "operator": operator,
                "id": id,
                "target": target,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.additional_metric_filters_item_target import (
            AdditionalMetricFiltersItemTarget,
        )

        d = src_dict.copy()
        operator = AdditionalMetricFiltersItemOperator(d.pop("operator"))

        id = d.pop("id")

        target = AdditionalMetricFiltersItemTarget.from_dict(d.pop("target"))

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        additional_metric_filters_item = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
        )

        return additional_metric_filters_item
