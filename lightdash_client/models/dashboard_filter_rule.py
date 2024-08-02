from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conditional_operator import ConditionalOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_field_target import DashboardFieldTarget
    from ..models.record_string_dashboard_tile_target import (
        RecordStringDashboardTileTarget,
    )


T = TypeVar("T", bound="DashboardFilterRule")


@_attrs_define
class DashboardFilterRule:
    """
    Attributes:
        operator (ConditionalOperator):
        id (str):
        target (DashboardFieldTarget):
        values (Union[Unset, List[Any]]):
        settings (Union[Unset, Any]):
        disabled (Union[Unset, bool]):
        required (Union[Unset, bool]):
        label (Union[Unset, str]):
        tile_targets (Union[Unset, RecordStringDashboardTileTarget]): Construct a type with a set of properties K of
            type T
    """

    operator: ConditionalOperator
    id: str
    target: "DashboardFieldTarget"
    values: Union[Unset, List[Any]] = UNSET
    settings: Union[Unset, Any] = UNSET
    disabled: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    tile_targets: Union[Unset, "RecordStringDashboardTileTarget"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator = self.operator.value

        id = self.id

        target = self.target.to_dict()

        values: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        settings = self.settings

        disabled = self.disabled

        required = self.required

        label = self.label

        tile_targets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tile_targets, Unset):
            tile_targets = self.tile_targets.to_dict()

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
        if label is not UNSET:
            field_dict["label"] = label
        if tile_targets is not UNSET:
            field_dict["tileTargets"] = tile_targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_field_target import DashboardFieldTarget
        from ..models.record_string_dashboard_tile_target import (
            RecordStringDashboardTileTarget,
        )

        d = src_dict.copy()
        operator = ConditionalOperator(d.pop("operator"))

        id = d.pop("id")

        target = DashboardFieldTarget.from_dict(d.pop("target"))

        values = cast(List[Any], d.pop("values", UNSET))

        settings = d.pop("settings", UNSET)

        disabled = d.pop("disabled", UNSET)

        required = d.pop("required", UNSET)

        label = d.pop("label", UNSET)

        _tile_targets = d.pop("tileTargets", UNSET)
        tile_targets: Union[Unset, RecordStringDashboardTileTarget]
        if isinstance(_tile_targets, Unset):
            tile_targets = UNSET
        else:
            tile_targets = RecordStringDashboardTileTarget.from_dict(_tile_targets)

        dashboard_filter_rule = cls(
            operator=operator,
            id=id,
            target=target,
            values=values,
            settings=settings,
            disabled=disabled,
            required=required,
            label=label,
            tile_targets=tile_targets,
        )

        dashboard_filter_rule.additional_properties = d
        return dashboard_filter_rule

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
