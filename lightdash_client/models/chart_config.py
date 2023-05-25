from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..models.chart_config_chart_type import ChartConfigChartType
from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.chart_config_config import ChartConfigConfig


T = TypeVar("T", bound="ChartConfig")


@attr.s(auto_attribs=True)
class ChartConfig:
    """
    Attributes:
        chart_type (Union[Unset, ChartConfigChartType]):
        config (Union[Unset, None, ChartConfigConfig]):
    """

    chart_type: Union[Unset, ChartConfigChartType] = UNSET
    config: Union[Unset, None, "ChartConfigConfig"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        config: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict() if self.config else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_config_config import ChartConfigConfig

        d = src_dict.copy()
        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, ChartConfigChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ChartConfigChartType(_chart_type)

        _config = d.pop("config", UNSET)
        config: Union[Unset, None, ChartConfigConfig]
        if _config is None:
            config = None
        elif isinstance(_config, Unset):
            config = UNSET
        else:
            config = ChartConfigConfig.from_dict(_config)

        chart_config = cls(
            chart_type=chart_type,
            config=config,
        )

        chart_config.additional_properties = d
        return chart_config

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
