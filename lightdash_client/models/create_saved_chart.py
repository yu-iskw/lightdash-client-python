from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.chart_config import ChartConfig
    from ..models.create_saved_chart_metric_query import CreateSavedChartMetricQuery
    from ..models.create_saved_chart_pivot_config import CreateSavedChartPivotConfig
    from ..models.create_saved_chart_table_config import CreateSavedChartTableConfig


T = TypeVar("T", bound="CreateSavedChart")


@attr.s(auto_attribs=True)
class CreateSavedChart:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        table_name (Union[Unset, str]):
        metric_query (Union[Unset, CreateSavedChartMetricQuery]):
        chart_config (Union[Unset, ChartConfig]):
        table_config (Union[Unset, CreateSavedChartTableConfig]):
        pivot_config (Union[Unset, CreateSavedChartPivotConfig]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    table_name: Union[Unset, str] = UNSET
    metric_query: Union[Unset, "CreateSavedChartMetricQuery"] = UNSET
    chart_config: Union[Unset, "ChartConfig"] = UNSET
    table_config: Union[Unset, "CreateSavedChartTableConfig"] = UNSET
    pivot_config: Union[Unset, "CreateSavedChartPivotConfig"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        table_name = self.table_name
        metric_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metric_query, Unset):
            metric_query = self.metric_query.to_dict()

        chart_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chart_config, Unset):
            chart_config = self.chart_config.to_dict()

        table_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.table_config, Unset):
            table_config = self.table_config.to_dict()

        pivot_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pivot_config, Unset):
            pivot_config = self.pivot_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if metric_query is not UNSET:
            field_dict["metricQuery"] = metric_query
        if chart_config is not UNSET:
            field_dict["chartConfig"] = chart_config
        if table_config is not UNSET:
            field_dict["tableConfig"] = table_config
        if pivot_config is not UNSET:
            field_dict["pivotConfig"] = pivot_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_config import ChartConfig
        from ..models.create_saved_chart_metric_query import CreateSavedChartMetricQuery
        from ..models.create_saved_chart_pivot_config import CreateSavedChartPivotConfig
        from ..models.create_saved_chart_table_config import CreateSavedChartTableConfig

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        table_name = d.pop("tableName", UNSET)

        _metric_query = d.pop("metricQuery", UNSET)
        metric_query: Union[Unset, CreateSavedChartMetricQuery]
        if isinstance(_metric_query, Unset):
            metric_query = UNSET
        else:
            metric_query = CreateSavedChartMetricQuery.from_dict(_metric_query)

        _chart_config = d.pop("chartConfig", UNSET)
        chart_config: Union[Unset, ChartConfig]
        if isinstance(_chart_config, Unset):
            chart_config = UNSET
        else:
            chart_config = ChartConfig.from_dict(_chart_config)

        _table_config = d.pop("tableConfig", UNSET)
        table_config: Union[Unset, CreateSavedChartTableConfig]
        if isinstance(_table_config, Unset):
            table_config = UNSET
        else:
            table_config = CreateSavedChartTableConfig.from_dict(_table_config)

        _pivot_config = d.pop("pivotConfig", UNSET)
        pivot_config: Union[Unset, CreateSavedChartPivotConfig]
        if isinstance(_pivot_config, Unset):
            pivot_config = UNSET
        else:
            pivot_config = CreateSavedChartPivotConfig.from_dict(_pivot_config)

        create_saved_chart = cls(
            name=name,
            description=description,
            table_name=table_name,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            pivot_config=pivot_config,
        )

        create_saved_chart.additional_properties = d
        return create_saved_chart

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
