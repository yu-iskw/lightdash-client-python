from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type_cartesian import ChartTypeCARTESIAN
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cartesian_chart import CartesianChart


T = TypeVar("T", bound="CartesianChartConfig")


@_attrs_define
class CartesianChartConfig:
    """
    Attributes:
        type (ChartTypeCARTESIAN):
        config (Union[Unset, CartesianChart]):
    """

    type: ChartTypeCARTESIAN
    config: Union[Unset, "CartesianChart"] = UNSET
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
        from ..models.cartesian_chart import CartesianChart

        d = src_dict.copy()
        type = ChartTypeCARTESIAN(d.pop("type"))

        _config = d.pop("config", UNSET)
        config: Union[Unset, CartesianChart]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = CartesianChart.from_dict(_config)

        cartesian_chart_config = cls(
            type=type,
            config=config,
        )

        cartesian_chart_config.additional_properties = d
        return cartesian_chart_config

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
