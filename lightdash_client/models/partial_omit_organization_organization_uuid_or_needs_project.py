from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialOmitOrganizationOrganizationUuidOrNeedsProject")


@attr.s(auto_attribs=True)
class PartialOmitOrganizationOrganizationUuidOrNeedsProject:
    """Make all properties in T optional

    Attributes:
        name (Union[Unset, str]): The name of the organization
        chart_colors (Union[Unset, List[str]]): The default color palette for all projects in the organization
        default_project_uuid (Union[Unset, str]): The project a user sees when they first log in to the organization
    """

    name: Union[Unset, str] = UNSET
    chart_colors: Union[Unset, List[str]] = UNSET
    default_project_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        chart_colors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.chart_colors, Unset):
            chart_colors = self.chart_colors

        default_project_uuid = self.default_project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if chart_colors is not UNSET:
            field_dict["chartColors"] = chart_colors
        if default_project_uuid is not UNSET:
            field_dict["defaultProjectUuid"] = default_project_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        chart_colors = cast(List[str], d.pop("chartColors", UNSET))

        default_project_uuid = d.pop("defaultProjectUuid", UNSET)

        partial_omit_organization_organization_uuid_or_needs_project = cls(
            name=name,
            chart_colors=chart_colors,
            default_project_uuid=default_project_uuid,
        )

        partial_omit_organization_organization_uuid_or_needs_project.additional_properties = d
        return partial_omit_organization_organization_uuid_or_needs_project

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
