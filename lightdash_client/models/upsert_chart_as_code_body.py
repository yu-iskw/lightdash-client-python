import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_table_config import (
        PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig,
    )


T = TypeVar("T", bound="UpsertChartAsCodeBody")


@_attrs_define
class UpsertChartAsCodeBody:
    """
    Attributes:
        name (str):
        dashboard_uuid (Union[None, str]):
        slug (str):
        table_name (str):
        updated_at (datetime.datetime):
        table_config (PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig):
        version (float):
        space_slug (str):
        metric_query (Any):
        chart_config (Any):
        description (Union[Unset, str]):
        downloaded_at (Union[Unset, datetime.datetime]):
    """

    name: str
    dashboard_uuid: Union[None, str]
    slug: str
    table_name: str
    updated_at: datetime.datetime
    table_config: "PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig"
    version: float
    space_slug: str
    metric_query: Any
    chart_config: Any
    description: Union[Unset, str] = UNSET
    downloaded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_table_config import (
            PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig,
        )

        name = self.name

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        slug = self.slug

        table_name = self.table_name

        updated_at = self.updated_at.isoformat()

        table_config = self.table_config.to_dict()

        version = self.version

        space_slug = self.space_slug

        metric_query = self.metric_query

        chart_config = self.chart_config

        description = self.description

        downloaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.downloaded_at, Unset):
            downloaded_at = self.downloaded_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dashboardUuid": dashboard_uuid,
                "slug": slug,
                "tableName": table_name,
                "updatedAt": updated_at,
                "tableConfig": table_config,
                "version": version,
                "spaceSlug": space_slug,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if downloaded_at is not UNSET:
            field_dict["downloadedAt"] = downloaded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_table_config import (
            PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig,
        )

        d = src_dict.copy()
        name = d.pop("name")

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        slug = d.pop("slug")

        table_name = d.pop("tableName")

        updated_at = isoparse(d.pop("updatedAt"))

        table_config = PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigTableConfig.from_dict(
            d.pop("tableConfig")
        )

        version = d.pop("version")

        space_slug = d.pop("spaceSlug")

        metric_query = d.pop("metricQuery")

        chart_config = d.pop("chartConfig")

        description = d.pop("description", UNSET)

        _downloaded_at = d.pop("downloadedAt", UNSET)
        downloaded_at: Union[Unset, datetime.datetime]
        if isinstance(_downloaded_at, Unset):
            downloaded_at = UNSET
        else:
            downloaded_at = isoparse(_downloaded_at)

        upsert_chart_as_code_body = cls(
            name=name,
            dashboard_uuid=dashboard_uuid,
            slug=slug,
            table_name=table_name,
            updated_at=updated_at,
            table_config=table_config,
            version=version,
            space_slug=space_slug,
            metric_query=metric_query,
            chart_config=chart_config,
            description=description,
            downloaded_at=downloaded_at,
        )

        upsert_chart_as_code_body.additional_properties = d
        return upsert_chart_as_code_body

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
