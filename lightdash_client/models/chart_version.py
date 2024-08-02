import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
        PickLightdashUserUserUuidOrFirstNameOrLastName,
    )
    from ..models.saved_chart import SavedChart


T = TypeVar("T", bound="ChartVersion")


@_attrs_define
class ChartVersion:
    """
    Attributes:
        chart (SavedChart):
        created_by (Union['PickLightdashUserUserUuidOrFirstNameOrLastName', None]):
        created_at (datetime.datetime):
        version_uuid (str):
        chart_uuid (str):
    """

    chart: "SavedChart"
    created_by: Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None]
    created_at: datetime.datetime
    version_uuid: str
    chart_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )

        chart = self.chart.to_dict()

        created_by: Union[Dict[str, Any], None]
        if isinstance(self.created_by, PickLightdashUserUserUuidOrFirstNameOrLastName):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        created_at = self.created_at.isoformat()

        version_uuid = self.version_uuid

        chart_uuid = self.chart_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chart": chart,
                "createdBy": created_by,
                "createdAt": created_at,
                "versionUuid": version_uuid,
                "chartUuid": chart_uuid,
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

        def _parse_created_by(data: object) -> Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_1 = PickLightdashUserUserUuidOrFirstNameOrLastName.from_dict(data)

                return created_by_type_1
            except:  # noqa: E722
                pass
            return cast(Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None], data)

        created_by = _parse_created_by(d.pop("createdBy"))

        created_at = isoparse(d.pop("createdAt"))

        version_uuid = d.pop("versionUuid")

        chart_uuid = d.pop("chartUuid")

        chart_version = cls(
            chart=chart,
            created_by=created_by,
            created_at=created_at,
            version_uuid=version_uuid,
            chart_uuid=chart_uuid,
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
