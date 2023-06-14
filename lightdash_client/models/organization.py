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

T = TypeVar("T", bound="Organization")


@attr.s(auto_attribs=True)
class Organization:
    """Details of a user's Organization

    Attributes:
        name (str): The name of the organization
        organization_uuid (str): The unique identifier of the organization
        needs_project (Union[Unset, bool]): The organization needs a project if it doesn't have at least one project.
        chart_colors (Union[Unset, List[str]]): The default color palette for all projects in the organization
    """

    name: str
    organization_uuid: str
    needs_project: Union[Unset, bool] = UNSET
    chart_colors: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        organization_uuid = self.organization_uuid
        needs_project = self.needs_project
        chart_colors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.chart_colors, Unset):
            chart_colors = self.chart_colors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "organizationUuid": organization_uuid,
            }
        )
        if needs_project is not UNSET:
            field_dict["needsProject"] = needs_project
        if chart_colors is not UNSET:
            field_dict["chartColors"] = chart_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        organization_uuid = d.pop("organizationUuid")

        needs_project = d.pop("needsProject", UNSET)

        chart_colors = cast(List[str], d.pop("chartColors", UNSET))

        organization = cls(
            name=name,
            organization_uuid=organization_uuid,
            needs_project=needs_project,
            chart_colors=chart_colors,
        )

        organization.additional_properties = d
        return organization

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
