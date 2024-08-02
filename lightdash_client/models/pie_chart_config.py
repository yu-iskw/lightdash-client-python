from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type_pie import ChartTypePIE
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pie_chart import PieChart


T = TypeVar("T", bound="PieChartConfig")


@_attrs_define
class PieChartConfig:
    """
    Attributes:
        type (ChartTypePIE):
        config (Union[Unset, PieChart]):
    """

    type: ChartTypePIE
    config: Union[Unset, "PieChart"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pie_chart import PieChart

        d = src_dict.copy()
        type = ChartTypePIE(d.pop("type"))

        _config = d.pop("config", UNSET)
        config: Union[Unset, PieChart]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PieChart.from_dict(_config)

        pie_chart_config = cls(
            type=type,
            config=config,
        )

        pie_chart_config.additional_properties = d
        return pie_chart_config

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
