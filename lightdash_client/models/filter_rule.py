from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.conditional_operator import ConditionalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_target import FieldTarget


T = TypeVar("T", bound="FilterRule")


@attr.s(auto_attribs=True)
class FilterRule:
    """
    Attributes:
        operator (ConditionalOperator):
        id (str):
        target (FieldTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
        disabled (Union[Unset, bool]):
    """

    operator: ConditionalOperator
    id: str
    target: "FieldTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id
        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings
        disabled = self.disabled

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
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_target import FieldTarget

        d = src_dict.copy()
        operator = ConditionalOperator(d.pop("operator"))

        id = d.pop("id")

        target = FieldTarget.from_dict(d.pop("target"))

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        disabled = d.pop("disabled", UNSET)

        filter_rule = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
            disabled=disabled,
        )

        return filter_rule
