import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description_table_config import (
        PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig,
    )


T = TypeVar("T", bound="PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescription")


@_attrs_define
class PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescription:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        slug (str):
        updated_at (datetime.datetime):
        table_name (str):
        table_config (PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig):
        version (float):
        space_slug (str):
        dashboard_slug (Union[Unset, str]):
        downloaded_at (Union[Unset, datetime.datetime]):
    """

    name: str
    slug: str
    updated_at: datetime.datetime
    table_name: str
    table_config: "PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig"
    version: float
    space_slug: str
    dashboard_slug: Union[Unset, str] = UNSET
    downloaded_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description_table_config import (
            PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig,
        )

        name = self.name

        slug = self.slug

        updated_at = self.updated_at.isoformat()

        table_name = self.table_name

        table_config = self.table_config.to_dict()

        version = self.version

        space_slug = self.space_slug

        dashboard_slug = self.dashboard_slug

        downloaded_at: Union[Unset, str] = UNSET
        if not isinstance(self.downloaded_at, Unset):
            downloaded_at = self.downloaded_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "updatedAt": updated_at,
                "tableName": table_name,
                "tableConfig": table_config,
                "version": version,
                "spaceSlug": space_slug,
            }
        )
        if dashboard_slug is not UNSET:
            field_dict["dashboardSlug"] = dashboard_slug
        if downloaded_at is not UNSET:
            field_dict["downloadedAt"] = downloaded_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description_table_config import (
            PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig,
        )

        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        table_name = d.pop("tableName")

        table_config = PickChartAsCodeExcludeKeyofChartAsCodeMetricQueryOrChartConfigOrDescriptionTableConfig.from_dict(
            d.pop("tableConfig")
        )

        version = d.pop("version")

        space_slug = d.pop("spaceSlug")

        dashboard_slug = d.pop("dashboardSlug", UNSET)

        _downloaded_at = d.pop("downloadedAt", UNSET)
        downloaded_at: Union[Unset, datetime.datetime]
        if isinstance(_downloaded_at, Unset):
            downloaded_at = UNSET
        else:
            downloaded_at = isoparse(_downloaded_at)

        pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description = cls(
            name=name,
            slug=slug,
            updated_at=updated_at,
            table_name=table_name,
            table_config=table_config,
            version=version,
            space_slug=space_slug,
            dashboard_slug=dashboard_slug,
            downloaded_at=downloaded_at,
        )

        pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description.additional_properties = d
        return pick_chart_as_code_exclude_keyof_chart_as_code_metric_query_or_chart_config_or_description

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
