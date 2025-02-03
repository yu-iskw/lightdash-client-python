from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_kind import ChartKind
from ..models.chart_source_type import ChartSourceType
from ..models.chart_type import ChartType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChartSummary")


@_attrs_define
class ChartSummary:
    """
    Attributes:
        name (str):
        project_uuid (str):
        uuid (str):
        space_uuid (str):
        organization_uuid (str):
        pinned_list_uuid (Union[None, str]):
        slug (str):
        space_name (str):
        dashboard_uuid (Union[None, str]):
        dashboard_name (Union[None, str]):
        description (Union[Unset, str]):
        source (Union[Unset, ChartSourceType]):
        chart_kind (Union[Unset, ChartKind]):
        chart_type (Union[Unset, ChartType]):
    """

    name: str
    project_uuid: str
    uuid: str
    space_uuid: str
    organization_uuid: str
    pinned_list_uuid: Union[None, str]
    slug: str
    space_name: str
    dashboard_uuid: Union[None, str]
    dashboard_name: Union[None, str]
    description: Union[Unset, str] = UNSET
    source: Union[Unset, ChartSourceType] = UNSET
    chart_kind: Union[Unset, ChartKind] = UNSET
    chart_type: Union[Unset, ChartType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        project_uuid = self.project_uuid

        uuid = self.uuid

        space_uuid = self.space_uuid

        organization_uuid = self.organization_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        slug = self.slug

        space_name = self.space_name

        dashboard_uuid: Union[None, str]
        dashboard_uuid = self.dashboard_uuid

        dashboard_name: Union[None, str]
        dashboard_name = self.dashboard_name

        description = self.description

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        chart_kind: Union[Unset, str] = UNSET
        if not isinstance(self.chart_kind, Unset):
            chart_kind = self.chart_kind.value

        chart_type: Union[Unset, str] = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectUuid": project_uuid,
                "uuid": uuid,
                "spaceUuid": space_uuid,
                "organizationUuid": organization_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "slug": slug,
                "spaceName": space_name,
                "dashboardUuid": dashboard_uuid,
                "dashboardName": dashboard_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if chart_kind is not UNSET:
            field_dict["chartKind"] = chart_kind
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        uuid = d.pop("uuid")

        space_uuid = d.pop("spaceUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        slug = d.pop("slug")

        space_name = d.pop("spaceName")

        def _parse_dashboard_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_uuid = _parse_dashboard_uuid(d.pop("dashboardUuid"))

        def _parse_dashboard_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dashboard_name = _parse_dashboard_name(d.pop("dashboardName"))

        description = d.pop("description", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ChartSourceType]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ChartSourceType(_source)

        _chart_kind = d.pop("chartKind", UNSET)
        chart_kind: Union[Unset, ChartKind]
        if isinstance(_chart_kind, Unset):
            chart_kind = UNSET
        else:
            chart_kind = ChartKind(_chart_kind)

        _chart_type = d.pop("chartType", UNSET)
        chart_type: Union[Unset, ChartType]
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ChartType(_chart_type)

        chart_summary = cls(
            name=name,
            project_uuid=project_uuid,
            uuid=uuid,
            space_uuid=space_uuid,
            organization_uuid=organization_uuid,
            pinned_list_uuid=pinned_list_uuid,
            slug=slug,
            space_name=space_name,
            dashboard_uuid=dashboard_uuid,
            dashboard_name=dashboard_name,
            description=description,
            source=source,
            chart_kind=chart_kind,
            chart_type=chart_type,
        )

        chart_summary.additional_properties = d
        return chart_summary

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
