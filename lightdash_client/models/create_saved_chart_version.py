from typing import Any
from typing import Dict
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.chart_config import ChartConfig
    from ..models.create_saved_chart_version_metric_query import CreateSavedChartVersionMetricQuery
    from ..models.create_saved_chart_version_pivot_config import CreateSavedChartVersionPivotConfig
    from ..models.create_saved_chart_version_table_config import CreateSavedChartVersionTableConfig


T = TypeVar("T", bound="CreateSavedChartVersion")


@attr.s(auto_attribs=True)
class CreateSavedChartVersion:
    """
    Attributes:
        table_name (str):
        metric_query (CreateSavedChartVersionMetricQuery):
        chart_config (ChartConfig):
        table_config (CreateSavedChartVersionTableConfig):
        pivot_config (Union[Unset, CreateSavedChartVersionPivotConfig]):
    """

    table_name: str
    metric_query: "CreateSavedChartVersionMetricQuery"
    chart_config: "ChartConfig"
    table_config: "CreateSavedChartVersionTableConfig"
    pivot_config: Union[Unset, "CreateSavedChartVersionPivotConfig"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        table_name = self.table_name
        metric_query = self.metric_query.to_dict()

        chart_config = self.chart_config.to_dict()

        table_config = self.table_config.to_dict()

        pivot_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pivot_config, Unset):
            pivot_config = self.pivot_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "tableName": table_name,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
                "tableConfig": table_config,
            }
        )
        if pivot_config is not UNSET:
            field_dict["pivotConfig"] = pivot_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_config import ChartConfig
        from ..models.create_saved_chart_version_metric_query import CreateSavedChartVersionMetricQuery
        from ..models.create_saved_chart_version_pivot_config import CreateSavedChartVersionPivotConfig
        from ..models.create_saved_chart_version_table_config import CreateSavedChartVersionTableConfig

        d = src_dict.copy()
        table_name = d.pop("tableName")

        metric_query = CreateSavedChartVersionMetricQuery.from_dict(d.pop("metricQuery"))

        chart_config = ChartConfig.from_dict(d.pop("chartConfig"))

        table_config = CreateSavedChartVersionTableConfig.from_dict(d.pop("tableConfig"))

        _pivot_config = d.pop("pivotConfig", UNSET)
        pivot_config: Union[Unset, CreateSavedChartVersionPivotConfig]
        if isinstance(_pivot_config, Unset):
            pivot_config = UNSET
        else:
            pivot_config = CreateSavedChartVersionPivotConfig.from_dict(_pivot_config)

        create_saved_chart_version = cls(
            table_name=table_name,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            pivot_config=pivot_config,
        )

        return create_saved_chart_version
