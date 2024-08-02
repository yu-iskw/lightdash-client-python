import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
    from ..models.pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_pivot_config import (
        PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig,
    )
    from ..models.pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_table_config import (
        PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessTableConfig,
    )
    from ..models.pie_chart_config import PieChartConfig
    from ..models.table_chart_config import TableChartConfig
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="PromotedChart")


@_attrs_define
class PromotedChart:
    """
    Attributes:
        name (str):
        uuid (str):
        space_name (str):
        space_uuid (str):
        project_uuid (str):
        organization_uuid (str):
        pinned_list_uuid (Union[None, str]):
        dashboard_uuid (Union[None, str]):
        dashboard_name (Union[None, str]):
        updated_at (datetime.datetime):
        pinned_list_order (Union[None, float]):
        slug (str):
        table_name (str):
        metric_query (MetricQuery):
        chart_config (Union['BigNumberConfig', 'CartesianChartConfig', 'CustomVisConfig', 'FunnelChartConfig',
            'PieChartConfig', 'TableChartConfig']):
        table_config (PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessTableConfig):
        color_palette (List[str]):
        old_uuid (str):
        space_slug (str):
        description (Union[Unset, str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
        pivot_config (Union[Unset, PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig]):
    """

    name: str
    uuid: str
    space_name: str
    space_uuid: str
    project_uuid: str
    organization_uuid: str
    pinned_list_uuid: Union[None, str]
    dashboard_uuid: Union[None, str]
    dashboard_name: Union[None, str]
    updated_at: datetime.datetime
    pinned_list_order: Union[None, float]
    slug: str
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
    table_config: "PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessTableConfig"
    color_palette: List[str]
    old_uuid: str
    space_slug: str
    description: Union[Unset, str] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    pivot_config: Union[Unset, "PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.pie_chart_config import PieChartConfig

        name = self.name

        uuid = self.uuid

        space_name = self.space_name

        space_uuid = self.space_uuid

        project_uuid = self.project_uuid

        organization_uuid = self.organization_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        dashboard_name: Union[None, str]
        dashboard_name = self.dashboard_name

        updated_at = self.updated_at.isoformat()

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        slug = self.slug

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

        color_palette = self.color_palette

        old_uuid = self.old_uuid

        space_slug = self.space_slug

        description = self.description

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        pivot_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pivot_config, Unset):
            pivot_config = self.pivot_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "spaceName": space_name,
                "spaceUuid": space_uuid,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "dashboardUuid": dashboard_uuid,
                "dashboardName": dashboard_name,
                "updatedAt": updated_at,
                "pinnedListOrder": pinned_list_order,
                "slug": slug,
                "tableName": table_name,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
                "tableConfig": table_config,
                "colorPalette": color_palette,
                "oldUuid": old_uuid,
                "spaceSlug": space_slug,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if pivot_config is not UNSET:
            field_dict["pivotConfig"] = pivot_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.metric_query import MetricQuery
        from ..models.pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_pivot_config import (
            PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig,
        )
        from ..models.pick_saved_chart_exclude_keyof_saved_chart_is_private_or_access_table_config import (
            PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessTableConfig,
        )
        from ..models.pie_chart_config import PieChartConfig
        from ..models.table_chart_config import TableChartConfig
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        def _parse_dashboard_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_name = _parse_dashboard_name(d.pop("dashboardName"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        slug = d.pop("slug")

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

        table_config = PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessTableConfig.from_dict(d.pop("tableConfig"))

        color_palette = cast(List[str], d.pop("colorPalette"))

        old_uuid = d.pop("oldUuid")

        space_slug = d.pop("spaceSlug")

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        _pivot_config = d.pop("pivotConfig", UNSET)
        pivot_config: Union[Unset, PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig]
        if isinstance(_pivot_config, Unset):
            pivot_config = UNSET
        else:
            pivot_config = PickSavedChartExcludeKeyofSavedChartIsPrivateOrAccessPivotConfig.from_dict(_pivot_config)

        promoted_chart = cls(
            name=name,
            uuid=uuid,
            space_name=space_name,
            space_uuid=space_uuid,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            pinned_list_uuid=pinned_list_uuid,
            dashboard_uuid=dashboard_uuid,
            dashboard_name=dashboard_name,
            updated_at=updated_at,
            pinned_list_order=pinned_list_order,
            slug=slug,
            table_name=table_name,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            color_palette=color_palette,
            old_uuid=old_uuid,
            space_slug=space_slug,
            description=description,
            updated_by_user=updated_by_user,
            pivot_config=pivot_config,
        )

        promoted_chart.additional_properties = d
        return promoted_chart

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
