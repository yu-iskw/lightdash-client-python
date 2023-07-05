from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.metric_filter_rule_operator import MetricFilterRuleOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_filter_rule_target import MetricFilterRuleTarget


T = TypeVar("T", bound="MetricFilterRule")


@attr.s(auto_attribs=True)
class MetricFilterRule:
    """
    Attributes:
        operator (MetricFilterRuleOperator):
        id (str):
        target (MetricFilterRuleTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
    """

    operator: MetricFilterRuleOperator
    id: str
    target: "MetricFilterRuleTarget"
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
        from ..models.metric_filter_rule_target import MetricFilterRuleTarget

        d = src_dict.copy()
        operator = MetricFilterRuleOperator(d.pop("operator"))

        id = d.pop("id")

        target = MetricFilterRuleTarget.from_dict(d.pop("target"))

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        metric_filter_rule = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
        )

        return metric_filter_rule
