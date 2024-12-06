import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.big_number_config import BigNumberConfig
    from ..models.cartesian_chart_config import CartesianChartConfig
    from ..models.custom_vis_config import CustomVisConfig
    from ..models.funnel_chart_config import FunnelChartConfig
    from ..models.metric_query import MetricQuery
    from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at_table_config import (
        PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAtTableConfig,
    )
    from ..models.pie_chart_config import PieChartConfig
    from ..models.table_chart_config import TableChartConfig


T = TypeVar(
    "T",
    bound="PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAt",
)


@_attrs_define
class PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAt:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        dashboard_uuid (Union[None, str]):
        slug (str):
        table_name (str):
        updated_at (datetime.datetime):
        metric_query (MetricQuery):
        chart_config (Union['BigNumberConfig', 'CartesianChartConfig', 'CustomVisConfig', 'FunnelChartConfig',
            'PieChartConfig', 'TableChartConfig']):
        table_config (PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboard
            UuidOrUpdatedAtTableConfig):
        description (Union[Unset, str]):
    """

    name: str
    dashboard_uuid: Union[None, str]
    slug: str
    table_name: str
    updated_at: datetime.datetime
    metric_query: "MetricQuery"
    chart_config: Union[
        "BigNumberConfig",
        "CartesianChartConfig",
        "CustomVisConfig",
        "FunnelChartConfig",
        "PieChartConfig",
        "TableChartConfig",
    ]
    table_config: "PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAtTableConfig"
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.metric_query import MetricQuery
        from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at_table_config import (
            PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAtTableConfig,
        )
        from ..models.pie_chart_config import PieChartConfig
        from ..models.table_chart_config import TableChartConfig

        name = self.name

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        slug = self.slug

        table_name = self.table_name

        updated_at = self.updated_at.isoformat()

        metric_query = self.metric_query.to_dict()

        chart_config: Dict[str, Any]
        if isinstance(self.chart_config, BigNumberConfig):
            chart_config = self.chart_config.to_dict()
        elif isinstance(self.chart_config, CartesianChartConfig):
            chart_config = self.chart_config.to_dict()
        elif isinstance(self.chart_config, CustomVisConfig):
            chart_config = self.chart_config.to_dict()
        elif isinstance(self.chart_config, PieChartConfig):
            chart_config = self.chart_config.to_dict()
        elif isinstance(self.chart_config, FunnelChartConfig):
            chart_config = self.chart_config.to_dict()
        else:
            chart_config = self.chart_config.to_dict()

        table_config = self.table_config.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dashboardUuid": dashboard_uuid,
                "slug": slug,
                "tableName": table_name,
                "updatedAt": updated_at,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
                "tableConfig": table_config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.metric_query import MetricQuery
        from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at_table_config import (
            PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAtTableConfig,
        )
        from ..models.pie_chart_config import PieChartConfig
        from ..models.table_chart_config import TableChartConfig

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        slug = d.pop("slug")

        table_name = d.pop("tableName")

        updated_at = isoparse(d.pop("updatedAt"))

        metric_query = MetricQuery.from_dict(d.pop("metricQuery"))

        def _parse_chart_config(
            data: object,
        ) -> Union[
            "BigNumberConfig",
            "CartesianChartConfig",
            "CustomVisConfig",
            "FunnelChartConfig",
            "PieChartConfig",
            "TableChartConfig",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_config_type_0 = BigNumberConfig.from_dict(data)

                return componentsschemas_chart_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_config_type_1 = CartesianChartConfig.from_dict(data)

                return componentsschemas_chart_config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_config_type_2 = CustomVisConfig.from_dict(data)

                return componentsschemas_chart_config_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_config_type_3 = PieChartConfig.from_dict(data)

                return componentsschemas_chart_config_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_chart_config_type_4 = FunnelChartConfig.from_dict(data)

                return componentsschemas_chart_config_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_chart_config_type_5 = TableChartConfig.from_dict(data)

            return componentsschemas_chart_config_type_5

        chart_config = _parse_chart_config(d.pop("chartConfig"))

        table_config = PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrDashboardUuidOrUpdatedAtTableConfig.from_dict(
            d.pop("tableConfig")
        )

        description = d.pop("description", UNSET)

        pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at = cls(
            name=name,
            dashboard_uuid=dashboard_uuid,
            slug=slug,
            table_name=table_name,
            updated_at=updated_at,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            description=description,
        )

        pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at.additional_properties = d
        return pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_dashboard_uuid_or_updated_at

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
