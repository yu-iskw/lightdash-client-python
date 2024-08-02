import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
        PickLightdashUserUserUuidOrFirstNameOrLastName,
    )


T = TypeVar("T", bound="PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy")


@_attrs_define
class PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        created_at (datetime.datetime):
        chart_uuid (str):
        version_uuid (str):
        created_by (Union['PickLightdashUserUserUuidOrFirstNameOrLastName', None]):
    """

    created_at: datetime.datetime
    chart_uuid: str
    version_uuid: str
    created_by: Union["PickLightdashUserUserUuidOrFirstNameOrLastName", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )

        created_at = self.created_at.isoformat()

        chart_uuid = self.chart_uuid

        version_uuid = self.version_uuid

        created_by: Union[Dict[str, Any], None]
        if isinstance(self.created_by, PickLightdashUserUserUuidOrFirstNameOrLastName):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "chartUuid": chart_uuid,
                "versionUuid": version_uuid,
                "createdBy": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_lightdash_user_user_uuid_or_first_name_or_last_name import (
            PickLightdashUserUserUuidOrFirstNameOrLastName,
        )

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        chart_uuid = d.pop("chartUuid")

        version_uuid = d.pop("versionUuid")

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

        pick_chart_version_chart_uuid_or_version_uuid_or_created_at_or_created_by = cls(
            created_at=created_at,
            chart_uuid=chart_uuid,
            version_uuid=version_uuid,
            created_by=created_by,
        )

        pick_chart_version_chart_uuid_or_version_uuid_or_created_at_or_created_by.additional_properties = d
        return pick_chart_version_chart_uuid_or_version_uuid_or_created_at_or_created_by

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
