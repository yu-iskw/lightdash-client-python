import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_frequency import NotificationFrequency
from ..models.scheduler_format import SchedulerFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduler_csv_options import SchedulerCsvOptions
    from ..models.scheduler_gsheets_options import SchedulerGsheetsOptions
    from ..models.scheduler_image_options import SchedulerImageOptions
    from ..models.threshold_options import ThresholdOptions


T = TypeVar("T", bound="SchedulerBase")


@_attrs_define
class SchedulerBase:
    """
    Attributes:
        enabled (bool):
        options (Union['SchedulerCsvOptions', 'SchedulerGsheetsOptions', 'SchedulerImageOptions']):
        dashboard_uuid (Union[None, str]):
        saved_chart_uuid (Union[None, str]):
        cron (str):
        format_ (SchedulerFormat):
        created_by (str):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        name (str):
        scheduler_uuid (str):
        notification_frequency (Union[Unset, NotificationFrequency]):
        thresholds (Union[Unset, List['ThresholdOptions']]):
        message (Union[Unset, str]):
    """

    enabled: bool
    options: Union["SchedulerCsvOptions", "SchedulerGsheetsOptions", "SchedulerImageOptions"]
    dashboard_uuid: Union[None, str]
    saved_chart_uuid: Union[None, str]
    cron: str
    format_: SchedulerFormat
    created_by: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    name: str
    scheduler_uuid: str
    notification_frequency: Union[Unset, NotificationFrequency] = UNSET
    thresholds: Union[Unset, List["ThresholdOptions"]] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scheduler_csv_options import SchedulerCsvOptions
        from ..models.scheduler_image_options import SchedulerImageOptions

        enabled = self.enabled

        options: Dict[str, Any]
        if isinstance(self.options, SchedulerCsvOptions):
            options = self.options.to_dict()
        elif isinstance(self.options, SchedulerImageOptions):
            options = self.options.to_dict()
        else:
            options = self.options.to_dict()

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        saved_chart_uuid: Union[None, str]
        saved_chart_uuid = self.saved_chart_uuid

        cron = self.cron

        format_ = self.format_.value

        created_by = self.created_by

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        name = self.name

        scheduler_uuid = self.scheduler_uuid

        notification_frequency: Union[Unset, str] = UNSET
        if not isinstance(self.notification_frequency, Unset):
            notification_frequency = self.notification_frequency.value

        thresholds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = []
            for thresholds_item_data in self.thresholds:
                thresholds_item = thresholds_item_data.to_dict()
                thresholds.append(thresholds_item)

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
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
        if notification_frequency is not UNSET:
            field_dict["notificationFrequency"] = notification_frequency
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduler_csv_options import SchedulerCsvOptions
        from ..models.scheduler_gsheets_options import SchedulerGsheetsOptions
        from ..models.scheduler_image_options import SchedulerImageOptions
        from ..models.threshold_options import ThresholdOptions

        d = src_dict.copy()
        enabled = d.pop("enabled")

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

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        def _parse_saved_chart_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        saved_chart_uuid = _parse_saved_chart_uuid(d.pop("savedChartUuid"))

        cron = d.pop("cron")

        format_ = SchedulerFormat(d.pop("format"))

        created_by = d.pop("createdBy")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        scheduler_uuid = d.pop("schedulerUuid")

        _notification_frequency = d.pop("notificationFrequency", UNSET)
        notification_frequency: Union[Unset, NotificationFrequency]
        if isinstance(_notification_frequency, Unset):
            notification_frequency = UNSET
        else:
            notification_frequency = NotificationFrequency(_notification_frequency)

        thresholds = []
        _thresholds = d.pop("thresholds", UNSET)
        for thresholds_item_data in _thresholds or []:
            thresholds_item = ThresholdOptions.from_dict(thresholds_item_data)

            thresholds.append(thresholds_item)

        message = d.pop("message", UNSET)

        scheduler_base = cls(
            enabled=enabled,
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
            notification_frequency=notification_frequency,
            thresholds=thresholds,
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
