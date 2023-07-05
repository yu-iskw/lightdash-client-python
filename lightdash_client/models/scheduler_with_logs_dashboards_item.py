from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SchedulerWithLogsDashboardsItem")


@attr.s(auto_attribs=True)
class SchedulerWithLogsDashboardsItem:
    """
    Attributes:
        dashboard_uuid (str):
        name (str):
    """

    dashboard_uuid: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dashboard_uuid = self.dashboard_uuid
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboardUuid": dashboard_uuid,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dashboard_uuid = d.pop("dashboardUuid")

        name = d.pop("name")

        scheduler_with_logs_dashboards_item = cls(
            dashboard_uuid=dashboard_uuid,
            name=name,
        )

        scheduler_with_logs_dashboards_item.additional_properties = d
        return scheduler_with_logs_dashboards_item

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
