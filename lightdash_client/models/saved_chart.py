import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.big_number_config import BigNumberConfig
    from ..models.cartesian_chart_config import CartesianChartConfig
    from ..models.custom_vis_config import CustomVisConfig
    from ..models.metric_query import MetricQuery
    from ..models.pie_chart_config import PieChartConfig
    from ..models.saved_chart_pivot_config import SavedChartPivotConfig
    from ..models.saved_chart_table_config import SavedChartTableConfig
    from ..models.table_chart_config import TableChartConfig
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="SavedChart")


@attr.s(auto_attribs=True)
class SavedChart:
    """
    Attributes:
        space_name (str):
        space_uuid (str):
        organization_uuid (str):
        updated_at (datetime.datetime):
        table_config (SavedChartTableConfig):
        chart_config (Union['BigNumberConfig', 'CartesianChartConfig', 'CustomVisConfig', 'PieChartConfig',
            'TableChartConfig']):
        metric_query (MetricQuery):
        table_name (str):
        name (str):
        project_uuid (str):
        uuid (str):
        dashboard_name (Optional[str]):
        dashboard_uuid (Optional[str]):
        pinned_list_order (Optional[float]):
        pinned_list_uuid (Optional[str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
        pivot_config (Union[Unset, SavedChartPivotConfig]):
        description (Union[Unset, str]):
    """

    space_name: str
    space_uuid: str
    organization_uuid: str
    updated_at: datetime.datetime
    table_config: "SavedChartTableConfig"
    chart_config: Union[
        "BigNumberConfig", "CartesianChartConfig", "CustomVisConfig", "PieChartConfig", "TableChartConfig"
    ]
    metric_query: "MetricQuery"
    table_name: str
    name: str
    project_uuid: str
    uuid: str
    dashboard_name: Optional[str]
    dashboard_uuid: Optional[str]
    pinned_list_order: Optional[float]
    pinned_list_uuid: Optional[str]
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    pivot_config: Union[Unset, "SavedChartPivotConfig"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.big_number_config import BigNumberConfig
        from ..models.cartesian_chart_config import CartesianChartConfig
        from ..models.custom_vis_config import CustomVisConfig
        from ..models.pie_chart_config import PieChartConfig

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

        else:
            chart_config = self.chart_config.to_dict()

        metric_query = self.metric_query.to_dict()

        table_name = self.table_name
        name = self.name
        project_uuid = self.project_uuid
        uuid = self.uuid
        dashboard_name = self.dashboard_name
        dashboard_uuid = self.dashboard_uuid
        pinned_list_order = self.pinned_list_order
        pinned_list_uuid = self.pinned_list_uuid
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
                "dashboardName": dashboard_name,
                "dashboardUuid": dashboard_uuid,
                "pinnedListOrder": pinned_list_order,
                "pinnedListUuid": pinned_list_uuid,
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
        from ..models.metric_query import MetricQuery
        from ..models.pie_chart_config import PieChartConfig
        from ..models.saved_chart_pivot_config import SavedChartPivotConfig
        from ..models.saved_chart_table_config import SavedChartTableConfig
        from ..models.table_chart_config import TableChartConfig
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        space_name = d.pop("spaceName")

        space_uuid = d.pop("spaceUuid")

        organization_uuid = d.pop("organizationUuid")

        updated_at = isoparse(d.pop("updatedAt"))

        table_config = SavedChartTableConfig.from_dict(d.pop("tableConfig"))

        def _parse_chart_config(
            data: object,
        ) -> Union["BigNumberConfig", "CartesianChartConfig", "CustomVisConfig", "PieChartConfig", "TableChartConfig"]:
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
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_chart_config_type_4 = TableChartConfig.from_dict(data)

            return componentsschemas_chart_config_type_4

        chart_config = _parse_chart_config(d.pop("chartConfig"))

        metric_query = MetricQuery.from_dict(d.pop("metricQuery"))

        table_name = d.pop("tableName")

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        uuid = d.pop("uuid")

        dashboard_name = d.pop("dashboardName")

        dashboard_uuid = d.pop("dashboardUuid")

        pinned_list_order = d.pop("pinnedListOrder")

        pinned_list_uuid = d.pop("pinnedListUuid")

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
            dashboard_name=dashboard_name,
            dashboard_uuid=dashboard_uuid,
            pinned_list_order=pinned_list_order,
            pinned_list_uuid=pinned_list_uuid,
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
