import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.scheduler_format import SchedulerFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduler_csv_options import SchedulerCsvOptions
    from ..models.scheduler_gsheets_options import SchedulerGsheetsOptions
    from ..models.scheduler_image_options import SchedulerImageOptions


T = TypeVar("T", bound="SchedulerBase")


@attr.s(auto_attribs=True)
class SchedulerBase:
    """
    Attributes:
        options (Union['SchedulerCsvOptions', 'SchedulerGsheetsOptions', 'SchedulerImageOptions']):
        cron (str):
        format_ (SchedulerFormat):
        created_by (str):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        name (str):
        scheduler_uuid (str):
        dashboard_uuid (Optional[str]):
        saved_chart_uuid (Optional[str]):
        message (Union[Unset, str]):
    """

    options: Union["SchedulerCsvOptions", "SchedulerGsheetsOptions", "SchedulerImageOptions"]
    cron: str
    format_: SchedulerFormat
    created_by: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    name: str
    scheduler_uuid: str
    dashboard_uuid: Optional[str]
    saved_chart_uuid: Optional[str]
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scheduler_csv_options import SchedulerCsvOptions
        from ..models.scheduler_image_options import SchedulerImageOptions

        options: Dict[str, Any]

        if isinstance(self.options, SchedulerCsvOptions):
            options = self.options.to_dict()

        elif isinstance(self.options, SchedulerImageOptions):
            options = self.options.to_dict()

        else:
            options = self.options.to_dict()

        cron = self.cron
        format_ = self.format_.value

        created_by = self.created_by
        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        name = self.name
        scheduler_uuid = self.scheduler_uuid
        dashboard_uuid = self.dashboard_uuid
        saved_chart_uuid = self.saved_chart_uuid
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "cron": cron,
                "format": format_,
                "createdBy": created_by,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "name": name,
                "schedulerUuid": scheduler_uuid,
                "dashboardUuid": dashboard_uuid,
                "savedChartUuid": saved_chart_uuid,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduler_csv_options import SchedulerCsvOptions
        from ..models.scheduler_gsheets_options import SchedulerGsheetsOptions
        from ..models.scheduler_image_options import SchedulerImageOptions

        d = src_dict.copy()

        def _parse_options(
            data: object,
        ) -> Union["SchedulerCsvOptions", "SchedulerGsheetsOptions", "SchedulerImageOptions"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_scheduler_options_type_0 = SchedulerCsvOptions.from_dict(data)

                return componentsschemas_scheduler_options_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_scheduler_options_type_1 = SchedulerImageOptions.from_dict(data)

                return componentsschemas_scheduler_options_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_scheduler_options_type_2 = SchedulerGsheetsOptions.from_dict(data)

            return componentsschemas_scheduler_options_type_2

        options = _parse_options(d.pop("options"))

        cron = d.pop("cron")

        format_ = SchedulerFormat(d.pop("format"))

        created_by = d.pop("createdBy")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        scheduler_uuid = d.pop("schedulerUuid")

        dashboard_uuid = d.pop("dashboardUuid")

        saved_chart_uuid = d.pop("savedChartUuid")

        message = d.pop("message", UNSET)

        scheduler_base = cls(
            options=options,
            cron=cron,
            format_=format_,
            created_by=created_by,
            updated_at=updated_at,
            created_at=created_at,
            name=name,
            scheduler_uuid=scheduler_uuid,
            dashboard_uuid=dashboard_uuid,
            saved_chart_uuid=saved_chart_uuid,
            message=message,
        )

        scheduler_base.additional_properties = d
        return scheduler_base

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
