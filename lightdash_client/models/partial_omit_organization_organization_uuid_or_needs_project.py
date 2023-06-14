from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="PartialOmitOrganizationOrganizationUuidOrNeedsProject")


@attr.s(auto_attribs=True)
class PartialOmitOrganizationOrganizationUuidOrNeedsProject:
    """Make all properties in T optional

    Attributes:
        name (Union[Unset, str]): The name of the organization
        chart_colors (Union[Unset, List[str]]): The default color palette for all projects in the organization
    """

    name: Union[Unset, str] = UNSET
    chart_colors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        chart_colors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.chart_colors, Unset):
            chart_colors = self.chart_colors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if chart_colors is not UNSET:
            field_dict["chartColors"] = chart_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        chart_colors = cast(List[str], d.pop("chartColors", UNSET))

        partial_omit_organization_organization_uuid_or_needs_project = cls(
            name=name,
            chart_colors=chart_colors,
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
