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
    from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config import (
        PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig,
    )
    from ..models.pie_chart_config import PieChartConfig
    from ..models.table_chart_config import TableChartConfig


T = TypeVar("T", bound="ChartAsCode")


@_attrs_define
class ChartAsCode:
    """
    Attributes:
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        table_name (str):
        metric_query (MetricQuery):
        chart_config (Union['BigNumberConfig', 'CartesianChartConfig', 'CustomVisConfig', 'FunnelChartConfig',
            'PieChartConfig', 'TableChartConfig']):
        table_config
            (PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig):
        space_slug (str):
        version (float):
        description (Union[Unset, str]):
        downloaded_at (Union[Unset, datetime.datetime]):
        dashboard_slug (Union[Unset, str]):
    """

    name: str
    slug: str
    updated_at: datetime.datetime
    table_name: str
    metric_query: "MetricQuery"
    chart_config: Union[
        "BigNumberConfig",
        "CartesianChartConfig",
        "CustomVisConfig",
        "FunnelChartConfig",
        "PieChartConfig",
        "TableChartConfig",
    ]
    table_config: (
        "PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig"
    )
    space_slug: str
    version: float
    description: Union[Unset, str] = UNSET
    downloaded_at: Union[Unset, datetime.datetime] = UNSET
    dashboard_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.metric_query import MetricQuery
        from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config import (
            PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig,
        )
        from ..models.pie_chart_config import PieChartConfig
        from ..models.table_chart_config import TableChartConfig

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        table_name = self.table_name

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

        space_slug = self.space_slug

        version = self.version

        description = self.description

        downloaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.downloaded_at, Unset):
            downloaded_at = self.downloaded_at.isoformat()

        dashboard_slug = self.dashboard_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "updatedAt": updated_at,
                "tableName": table_name,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
                "tableConfig": table_config,
                "spaceSlug": space_slug,
                "version": version,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if downloaded_at is not UNSET:
            field_dict["downloadedAt"] = downloaded_at
        if dashboard_slug is not UNSET:
            field_dict["dashboardSlug"] = dashboard_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.metric_query import MetricQuery
        from ..models.pick_saved_chart_name_or_description_or_table_name_or_metric_query_or_chart_config_or_table_config_or_slug_or_updated_at_table_config import (
            PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig,
        )
        from ..models.pie_chart_config import PieChartConfig
        from ..models.table_chart_config import TableChartConfig

        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        table_name = d.pop("tableName")

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

        table_config = PickSavedChartNameOrDescriptionOrTableNameOrMetricQueryOrChartConfigOrTableConfigOrSlugOrUpdatedAtTableConfig.from_dict(
            d.pop("tableConfig")
        )

        space_slug = d.pop("spaceSlug")

        version = d.pop("version")

        description = d.pop("description", UNSET)

        _downloaded_at = d.pop("downloadedAt", UNSET)
        downloaded_at: Union[Unset, datetime.datetime]
        if isinstance(_downloaded_at, Unset):
            downloaded_at = UNSET
        else:
            downloaded_at = isoparse(_downloaded_at)

        dashboard_slug = d.pop("dashboardSlug", UNSET)

        chart_as_code = cls(
            name=name,
            slug=slug,
            updated_at=updated_at,
            table_name=table_name,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            space_slug=space_slug,
            version=version,
            description=description,
            downloaded_at=downloaded_at,
            dashboard_slug=dashboard_slug,
        )

        chart_as_code.additional_properties = d
        return chart_as_code

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
