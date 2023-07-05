from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.api_scheduler_logs_response_results_charts_item import (
        ApiSchedulerLogsResponseResultsChartsItem,
    )
    from ..models.api_scheduler_logs_response_results_dashboards_item import (
        ApiSchedulerLogsResponseResultsDashboardsItem,
    )
    from ..models.api_scheduler_logs_response_results_logs_item import (
        ApiSchedulerLogsResponseResultsLogsItem,
    )
    from ..models.api_scheduler_logs_response_results_schedulers_item import (
        ApiSchedulerLogsResponseResultsSchedulersItem,
    )
    from ..models.api_scheduler_logs_response_results_users_item import (
        ApiSchedulerLogsResponseResultsUsersItem,
    )


T = TypeVar("T", bound="ApiSchedulerLogsResponseResults")


@attr.s(auto_attribs=True)
class ApiSchedulerLogsResponseResults:
    """
    Attributes:
        logs (List['ApiSchedulerLogsResponseResultsLogsItem']):
        dashboards (List['ApiSchedulerLogsResponseResultsDashboardsItem']):
        charts (List['ApiSchedulerLogsResponseResultsChartsItem']):
        users (List['ApiSchedulerLogsResponseResultsUsersItem']):
        schedulers (List['ApiSchedulerLogsResponseResultsSchedulersItem']):
    """

    logs: List["ApiSchedulerLogsResponseResultsLogsItem"]
    dashboards: List["ApiSchedulerLogsResponseResultsDashboardsItem"]
    charts: List["ApiSchedulerLogsResponseResultsChartsItem"]
    users: List["ApiSchedulerLogsResponseResultsUsersItem"]
    schedulers: List["ApiSchedulerLogsResponseResultsSchedulersItem"]
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
        from ..models.api_scheduler_logs_response_results_charts_item import (
            ApiSchedulerLogsResponseResultsChartsItem,
        )
        from ..models.api_scheduler_logs_response_results_dashboards_item import (
            ApiSchedulerLogsResponseResultsDashboardsItem,
        )
        from ..models.api_scheduler_logs_response_results_logs_item import (
            ApiSchedulerLogsResponseResultsLogsItem,
        )
        from ..models.api_scheduler_logs_response_results_schedulers_item import (
            ApiSchedulerLogsResponseResultsSchedulersItem,
        )
        from ..models.api_scheduler_logs_response_results_users_item import (
            ApiSchedulerLogsResponseResultsUsersItem,
        )

        d = src_dict.copy()
        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = ApiSchedulerLogsResponseResultsLogsItem.from_dict(logs_item_data)

            logs.append(logs_item)

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = ApiSchedulerLogsResponseResultsDashboardsItem.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        charts = []
        _charts = d.pop("charts")
        for charts_item_data in _charts:
            charts_item = ApiSchedulerLogsResponseResultsChartsItem.from_dict(charts_item_data)

            charts.append(charts_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = ApiSchedulerLogsResponseResultsUsersItem.from_dict(users_item_data)

            users.append(users_item)

        schedulers = []
        _schedulers = d.pop("schedulers")
        for schedulers_item_data in _schedulers:
            schedulers_item = ApiSchedulerLogsResponseResultsSchedulersItem.from_dict(schedulers_item_data)

            schedulers.append(schedulers_item)

        api_scheduler_logs_response_results = cls(
            logs=logs,
            dashboards=dashboards,
            charts=charts,
            users=users,
            schedulers=schedulers,
        )

        api_scheduler_logs_response_results.additional_properties = d
        return api_scheduler_logs_response_results

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
