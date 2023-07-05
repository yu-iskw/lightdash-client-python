from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.scheduler_with_logs_charts_item import SchedulerWithLogsChartsItem
    from ..models.scheduler_with_logs_dashboards_item import (
        SchedulerWithLogsDashboardsItem,
    )
    from ..models.scheduler_with_logs_logs_item import SchedulerWithLogsLogsItem
    from ..models.scheduler_with_logs_schedulers_item import (
        SchedulerWithLogsSchedulersItem,
    )
    from ..models.scheduler_with_logs_users_item import SchedulerWithLogsUsersItem


T = TypeVar("T", bound="SchedulerWithLogs")


@attr.s(auto_attribs=True)
class SchedulerWithLogs:
    """
    Attributes:
        logs (List['SchedulerWithLogsLogsItem']):
        dashboards (List['SchedulerWithLogsDashboardsItem']):
        charts (List['SchedulerWithLogsChartsItem']):
        users (List['SchedulerWithLogsUsersItem']):
        schedulers (List['SchedulerWithLogsSchedulersItem']):
    """

    logs: List["SchedulerWithLogsLogsItem"]
    dashboards: List["SchedulerWithLogsDashboardsItem"]
    charts: List["SchedulerWithLogsChartsItem"]
    users: List["SchedulerWithLogsUsersItem"]
    schedulers: List["SchedulerWithLogsSchedulersItem"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()

            logs.append(logs_item)

        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()

            dashboards.append(dashboards_item)

        charts = []
        for charts_item_data in self.charts:
            charts_item = charts_item_data.to_dict()

            charts.append(charts_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        schedulers = []
        for schedulers_item_data in self.schedulers:
            schedulers_item = schedulers_item_data.to_dict()

            schedulers.append(schedulers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logs": logs,
                "dashboards": dashboards,
                "charts": charts,
                "users": users,
                "schedulers": schedulers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduler_with_logs_charts_item import SchedulerWithLogsChartsItem
        from ..models.scheduler_with_logs_dashboards_item import (
            SchedulerWithLogsDashboardsItem,
        )
        from ..models.scheduler_with_logs_logs_item import SchedulerWithLogsLogsItem
        from ..models.scheduler_with_logs_schedulers_item import (
            SchedulerWithLogsSchedulersItem,
        )
        from ..models.scheduler_with_logs_users_item import SchedulerWithLogsUsersItem

        d = src_dict.copy()
        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = SchedulerWithLogsLogsItem.from_dict(logs_item_data)

            logs.append(logs_item)

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = SchedulerWithLogsDashboardsItem.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = SchedulerWithLogsChartsItem.from_dict(charts_item_data)

            charts.append(charts_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = SchedulerWithLogsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        schedulers = []
        _schedulers = d.pop("schedulers")
        for schedulers_item_data in _schedulers:
            schedulers_item = SchedulerWithLogsSchedulersItem.from_dict(schedulers_item_data)

            schedulers.append(schedulers_item)

        scheduler_with_logs = cls(
            logs=logs,
            dashboards=dashboards,
            charts=charts,
            users=users,
            schedulers=schedulers,
        )

        scheduler_with_logs.additional_properties = d
        return scheduler_with_logs

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
