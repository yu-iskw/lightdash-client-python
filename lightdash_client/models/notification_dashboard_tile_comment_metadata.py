from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotificationDashboardTileCommentMetadata")


@_attrs_define
class NotificationDashboardTileCommentMetadata:
    """
    Attributes:
        dashboard_uuid (str):
        dashboard_name (str):
        dashboard_tile_uuid (str):
        dashboard_tile_name (str):
    """

    dashboard_uuid: str
    dashboard_name: str
    dashboard_tile_uuid: str
    dashboard_tile_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dashboard_uuid = self.dashboard_uuid

        dashboard_name = self.dashboard_name

        dashboard_tile_uuid = self.dashboard_tile_uuid

        dashboard_tile_name = self.dashboard_tile_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dashboardUuid": dashboard_uuid,
                "dashboardName": dashboard_name,
                "dashboardTileUuid": dashboard_tile_uuid,
                "dashboardTileName": dashboard_tile_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dashboard_uuid = d.pop("dashboardUuid")

        dashboard_name = d.pop("dashboardName")

        dashboard_tile_uuid = d.pop("dashboardTileUuid")

        dashboard_tile_name = d.pop("dashboardTileName")

        notification_dashboard_tile_comment_metadata = cls(
            dashboard_uuid=dashboard_uuid,
            dashboard_name=dashboard_name,
            dashboard_tile_uuid=dashboard_tile_uuid,
            dashboard_tile_name=dashboard_tile_name,
        )

        notification_dashboard_tile_comment_metadata.additional_properties = d
        return notification_dashboard_tile_comment_metadata

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
