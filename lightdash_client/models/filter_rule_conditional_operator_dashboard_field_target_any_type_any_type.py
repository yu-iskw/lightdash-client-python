from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conditional_operator import ConditionalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_field_target import DashboardFieldTarget


T = TypeVar("T", bound="FilterRuleConditionalOperatorDashboardFieldTargetAnyTypeAnyType")


@_attrs_define
class FilterRuleConditionalOperatorDashboardFieldTargetAnyTypeAnyType:
    """
    Attributes:
        operator (ConditionalOperator):
        id (str):
        target (DashboardFieldTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.
        disabled (Union[Unset, bool]):
        required (Union[Unset, bool]):
    """

    operator: ConditionalOperator
    id: str
    target: "DashboardFieldTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET
    disabled: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_field_target import DashboardFieldTarget

        operator = self.operator.value

        id = self.id

        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings

        disabled = self.disabled

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_field_target import DashboardFieldTarget

        d = src_dict.copy()
        operator = ConditionalOperator(d.pop("operator"))

        id = d.pop("id")

        target = DashboardFieldTarget.from_dict(d.pop("target"))

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        disabled = d.pop("disabled", UNSET)

        required = d.pop("required", UNSET)

        filter_rule_conditional_operator_dashboard_field_target_any_type_any_type = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
            disabled=disabled,
            required=required,
        )

        filter_rule_conditional_operator_dashboard_field_target_any_type_any_type.additional_properties = d
        return filter_rule_conditional_operator_dashboard_field_target_any_type_any_type

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
