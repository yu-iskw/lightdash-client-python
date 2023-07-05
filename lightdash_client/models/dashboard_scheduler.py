import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.dashboard_scheduler_format import DashboardSchedulerFormat

if TYPE_CHECKING:
    from ..models.dashboard_scheduler_options_type_0 import (
        DashboardSchedulerOptionsType0,
    )
    from ..models.dashboard_scheduler_options_type_1 import (
        DashboardSchedulerOptionsType1,
    )


T = TypeVar("T", bound="DashboardScheduler")


@attr.s(auto_attribs=True)
class DashboardScheduler:
    """
    Attributes:
        options (Union['DashboardSchedulerOptionsType0', 'DashboardSchedulerOptionsType1']):
        dashboard_uuid (str):
        saved_chart_uuid (None):  Default: None.
        cron (str):
        format_ (DashboardSchedulerFormat):
        created_by (str):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        name (str):
        scheduler_uuid (str):
    """

    options: Union["DashboardSchedulerOptionsType0", "DashboardSchedulerOptionsType1"]
    dashboard_uuid: str
    cron: str
    format_: DashboardSchedulerFormat
    created_by: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    name: str
    scheduler_uuid: str
    saved_chart_uuid: None = None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_scheduler_options_type_0 import (
            DashboardSchedulerOptionsType0,
        )

        options: Dict[str, Any]

        if isinstance(self.options, DashboardSchedulerOptionsType0):
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
        from ..models.dashboard_scheduler_options_type_0 import (
            DashboardSchedulerOptionsType0,
        )
        from ..models.dashboard_scheduler_options_type_1 import (
            DashboardSchedulerOptionsType1,
        )

        d = src_dict.copy()

        def _parse_options(data: object) -> Union["DashboardSchedulerOptionsType0", "DashboardSchedulerOptionsType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = DashboardSchedulerOptionsType0.from_dict(data)

                return options_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            options_type_1 = DashboardSchedulerOptionsType1.from_dict(data)

            return options_type_1

        options = _parse_options(d.pop("options"))

        dashboard_uuid = d.pop("dashboardUuid")

        saved_chart_uuid = d.pop("savedChartUuid")

        cron = d.pop("cron")

        format_ = DashboardSchedulerFormat(d.pop("format"))

        created_by = d.pop("createdBy")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        scheduler_uuid = d.pop("schedulerUuid")

        dashboard_scheduler = cls(
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

        dashboard_scheduler.additional_properties = d
        return dashboard_scheduler

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
