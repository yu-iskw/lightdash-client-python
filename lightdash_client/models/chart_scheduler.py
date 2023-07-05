import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.chart_scheduler_format import ChartSchedulerFormat

if TYPE_CHECKING:
    from ..models.chart_scheduler_options_type_0 import ChartSchedulerOptionsType0
    from ..models.chart_scheduler_options_type_1 import ChartSchedulerOptionsType1


T = TypeVar("T", bound="ChartScheduler")


@attr.s(auto_attribs=True)
class ChartScheduler:
    """
    Attributes:
        options (Union['ChartSchedulerOptionsType0', 'ChartSchedulerOptionsType1']):
        dashboard_uuid (None):  Default: None.
        saved_chart_uuid (str):
        cron (str):
        format_ (ChartSchedulerFormat):
        created_by (str):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        name (str):
        scheduler_uuid (str):
    """

    options: Union["ChartSchedulerOptionsType0", "ChartSchedulerOptionsType1"]
    saved_chart_uuid: str
    cron: str
    format_: ChartSchedulerFormat
    created_by: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    name: str
    scheduler_uuid: str
    dashboard_uuid: None = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.chart_scheduler_options_type_0 import ChartSchedulerOptionsType0

        options: Dict[str, Any]

        if isinstance(self.options, ChartSchedulerOptionsType0):
            options = self.options.to_dict()

        else:
            options = self.options.to_dict()

        dashboard_uuid = self.dashboard_uuid
        saved_chart_uuid = self.saved_chart_uuid
        cron = self.cron
        format_ = self.format_.value

        created_by = self.created_by
        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        name = self.name
        scheduler_uuid = self.scheduler_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "dashboardUuid": dashboard_uuid,
                "savedChartUuid": saved_chart_uuid,
                "cron": cron,
                "format": format_,
                "createdBy": created_by,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "name": name,
                "schedulerUuid": scheduler_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_scheduler_options_type_0 import ChartSchedulerOptionsType0
        from ..models.chart_scheduler_options_type_1 import ChartSchedulerOptionsType1

        d = src_dict.copy()

        def _parse_options(data: object) -> Union["ChartSchedulerOptionsType0", "ChartSchedulerOptionsType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = ChartSchedulerOptionsType0.from_dict(data)

                return options_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            options_type_1 = ChartSchedulerOptionsType1.from_dict(data)

            return options_type_1

        options = _parse_options(d.pop("options"))

        dashboard_uuid = d.pop("dashboardUuid")

        saved_chart_uuid = d.pop("savedChartUuid")

        cron = d.pop("cron")

        format_ = ChartSchedulerFormat(d.pop("format"))

        created_by = d.pop("createdBy")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        scheduler_uuid = d.pop("schedulerUuid")

        chart_scheduler = cls(
            options=options,
            dashboard_uuid=dashboard_uuid,
            saved_chart_uuid=saved_chart_uuid,
            cron=cron,
            format_=format_,
            created_by=created_by,
            updated_at=updated_at,
            created_at=created_at,
            name=name,
            scheduler_uuid=scheduler_uuid,
        )

        chart_scheduler.additional_properties = d
        return chart_scheduler

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
