from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_as_code import DashboardAsCode


T = TypeVar("T", bound="ApiDashboardAsCodeListResponseResults")


@_attrs_define
class ApiDashboardAsCodeListResponseResults:
    """
    Attributes:
        offset (float):
        total (float):
        missing_ids (List[str]):
        dashboards (List['DashboardAsCode']):
    """

    offset: float
    total: float
    missing_ids: List[str]
    dashboards: List["DashboardAsCode"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.dashboard_as_code import DashboardAsCode

        offset = self.offset

        total = self.total

        missing_ids = self.missing_ids

        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()
            dashboards.append(dashboards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "total": total,
                "missingIds": missing_ids,
                "dashboards": dashboards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_as_code import DashboardAsCode

        d = src_dict.copy()
        offset = d.pop("offset")

        total = d.pop("total")

        missing_ids = cast(List[str], d.pop("missingIds"))

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = DashboardAsCode.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        api_dashboard_as_code_list_response_results = cls(
            offset=offset,
            total=total,
            missing_ids=missing_ids,
            dashboards=dashboards,
        )

        api_dashboard_as_code_list_response_results.additional_properties = d
        return api_dashboard_as_code_list_response_results

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
