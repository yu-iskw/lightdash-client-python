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
    from ..models.pie_chart_config import PieChartConfig
    from ..models.saved_chart_pivot_config import SavedChartPivotConfig
    from ..models.saved_chart_table_config import SavedChartTableConfig
    from ..models.space_share import SpaceShare
    from ..models.table_chart_config import TableChartConfig
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="SavedChart")


@_attrs_define
class SavedChart:
    """
    Attributes:
        slug (str):
        access (List['SpaceShare']):
        is_private (bool):
        color_palette (List[str]):
        dashboard_name (Union[None, str]):
        dashboard_uuid (Union[None, str]):
        pinned_list_order (Union[None, float]):
        pinned_list_uuid (Union[None, str]):
        space_name (str):
        space_uuid (str):
        organization_uuid (str):
        updated_at (datetime.datetime):
        table_config (SavedChartTableConfig):
        chart_config (Union['BigNumberConfig', 'CartesianChartConfig', 'CustomVisConfig', 'FunnelChartConfig',
            'PieChartConfig', 'TableChartConfig']):
        metric_query (MetricQuery):
        table_name (str):
        name (str):
        project_uuid (str):
        uuid (str):
        updated_by_user (Union[Unset, UpdatedByUser]):
        pivot_config (Union[Unset, SavedChartPivotConfig]):
        description (Union[Unset, str]):
    """

    slug: str
    access: List["SpaceShare"]
    is_private: bool
    color_palette: List[str]
    dashboard_name: Union[None, str]
    dashboard_uuid: Union[None, str]
    pinned_list_order: Union[None, float]
    pinned_list_uuid: Union[None, str]
    space_name: str
    space_uuid: str
    organization_uuid: str
    updated_at: datetime.datetime
    table_config: "SavedChartTableConfig"
    chart_config: Union[
        "BigNumberConfig",
        "CartesianChartConfig",
        "CustomVisConfig",
        "FunnelChartConfig",
        "PieChartConfig",
        "TableChartConfig",
    ]
    metric_query: "MetricQuery"
    table_name: str
    name: str
    project_uuid: str
    uuid: str
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    pivot_config: Union[Unset, "SavedChartPivotConfig"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.funnel_chart_config import FunnelChartConfig
        from ..models.pie_chart_config import PieChartConfig

        slug = self.slug

        access = []
        for access_item_data in self.access:
            access_item = access_item_data.to_dict()
            access.append(access_item)

        is_private = self.is_private

        color_palette = self.color_palette

        dashboard_name: Union[None, str]
        dashboard_name = self.dashboard_name

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        space_name = self.space_name

        space_uuid = self.space_uuid

        organization_uuid = self.organization_uuid

        updated_at = self.updated_at.isoformat()

        table_config = self.table_config.to_dict()

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

        metric_query = self.metric_query.to_dict()

        table_name = self.table_name

        name = self.name

        project_uuid = self.project_uuid

        uuid = self.uuid

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        pivot_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pivot_config, Unset):
            pivot_config = self.pivot_config.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "access": access,
                "isPrivate": is_private,
                "colorPalette": color_palette,
                "dashboardName": dashboard_name,
                "dashboardUuid": dashboard_uuid,
                "pinnedListOrder": pinned_list_order,
                "pinnedListUuid": pinned_list_uuid,
                "spaceName": space_name,
                "spaceUuid": space_uuid,
                "organizationUuid": organization_uuid,
                "updatedAt": updated_at,
                "tableConfig": table_config,
                "chartConfig": chart_config,
                "metricQuery": metric_query,
                "tableName": table_name,
                "name": name,
                "projectUuid": project_uuid,
                "uuid": uuid,
            }
        )
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if pivot_config is not UNSET:
            field_dict["pivotConfig"] = pivot_config
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
        from ..models.pie_chart_config import PieChartConfig
        from ..models.saved_chart_pivot_config import SavedChartPivotConfig
        from ..models.saved_chart_table_config import SavedChartTableConfig
        from ..models.space_share import SpaceShare
        from ..models.table_chart_config import TableChartConfig
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        slug = d.pop("slug")

        access = []
        _access = d.pop("access")
        for access_item_data in _access:
            access_item = SpaceShare.from_dict(access_item_data)

            access.append(access_item)

        is_private = d.pop("isPrivate")

        color_palette = cast(List[str], d.pop("colorPalette"))

        def _parse_dashboard_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_name = _parse_dashboard_name(d.pop("dashboardName"))

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        organization_uuid = d.pop("organizationUuid")

        updated_at = isoparse(d.pop("updatedAt"))

        table_config = SavedChartTableConfig.from_dict(d.pop("tableConfig"))

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

        metric_query = MetricQuery.from_dict(d.pop("metricQuery"))

        table_name = d.pop("tableName")

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        uuid = d.pop("uuid")

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        _pivot_config = d.pop("pivotConfig", UNSET)
        pivot_config: Union[Unset, SavedChartPivotConfig]
        if isinstance(_pivot_config, Unset):
            pivot_config = UNSET
        else:
            pivot_config = SavedChartPivotConfig.from_dict(_pivot_config)

        description = d.pop("description", UNSET)

        saved_chart = cls(
            slug=slug,
            access=access,
            is_private=is_private,
            color_palette=color_palette,
            dashboard_name=dashboard_name,
            dashboard_uuid=dashboard_uuid,
            pinned_list_order=pinned_list_order,
            pinned_list_uuid=pinned_list_uuid,
            space_name=space_name,
            space_uuid=space_uuid,
            organization_uuid=organization_uuid,
            updated_at=updated_at,
            table_config=table_config,
            chart_config=chart_config,
            metric_query=metric_query,
            table_name=table_name,
            name=name,
            project_uuid=project_uuid,
            uuid=uuid,
            updated_by_user=updated_by_user,
            pivot_config=pivot_config,
            description=description,
        )

        saved_chart.additional_properties = d
        return saved_chart

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
