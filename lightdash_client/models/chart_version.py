import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
        PickLightdashUserUserUuidOrFirstNameOrLastName,
    )
    from ..models.saved_chart import SavedChart


T = TypeVar("T", bound="ChartVersion")


@attr.s(auto_attribs=True)
class ChartVersion:
    """
    Attributes:
        chart (SavedChart):
        created_at (datetime.datetime):
        version_uuid (str):
        chart_uuid (str):
        created_by (Optional[PickLightdashUserUserUuidOrFirstNameOrLastName]): From T, pick a set of properties whose
            keys are in the union K
    """

    chart: "SavedChart"
    created_at: datetime.datetime
    version_uuid: str
    chart_uuid: str
    created_by: Optional["PickLightdashUserUserUuidOrFirstNameOrLastName"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chart = self.chart.to_dict()

        created_at = self.created_at.isoformat()

        version_uuid = self.version_uuid
        chart_uuid = self.chart_uuid
        created_by = self.created_by.to_dict() if self.created_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chart": chart,
                "createdAt": created_at,
                "versionUuid": version_uuid,
                "chartUuid": chart_uuid,
                "createdBy": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )
        from ..models.saved_chart import SavedChart

        d = src_dict.copy()
        chart = SavedChart.from_dict(d.pop("chart"))

        created_at = isoparse(d.pop("createdAt"))

        version_uuid = d.pop("versionUuid")

        chart_uuid = d.pop("chartUuid")

        _created_by = d.pop("createdBy")
        created_by: Optional[PickLightdashUserUserUuidOrFirstNameOrLastName]
        if _created_by is None:
            created_by = None
        else:
            created_by = PickLightdashUserUserUuidOrFirstNameOrLastName.from_dict(_created_by)

        chart_version = cls(
            chart=chart,
            created_at=created_at,
            version_uuid=version_uuid,
            chart_uuid=chart_uuid,
            created_by=created_by,
        )

        chart_version.additional_properties = d
        return chart_version

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
