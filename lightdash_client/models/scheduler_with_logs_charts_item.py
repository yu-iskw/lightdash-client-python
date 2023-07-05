from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SchedulerWithLogsChartsItem")


@attr.s(auto_attribs=True)
class SchedulerWithLogsChartsItem:
    """
    Attributes:
        saved_chart_uuid (str):
        name (str):
    """

    saved_chart_uuid: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_chart_uuid = self.saved_chart_uuid
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "savedChartUuid": saved_chart_uuid,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_chart_uuid = d.pop("savedChartUuid")

        name = d.pop("name")

        scheduler_with_logs_charts_item = cls(
            saved_chart_uuid=saved_chart_uuid,
            name=name,
        )

        scheduler_with_logs_charts_item.additional_properties = d
        return scheduler_with_logs_charts_item

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
