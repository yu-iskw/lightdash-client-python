from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SchedulerGsheetsOptions")


@_attrs_define
class SchedulerGsheetsOptions:
    """
    Attributes:
        url (str):
        gdrive_organization_name (str):
        gdrive_name (str):
        gdrive_id (str):
    """

    url: str
    gdrive_organization_name: str
    gdrive_name: str
    gdrive_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        gdrive_organization_name = self.gdrive_organization_name

        gdrive_name = self.gdrive_name

        gdrive_id = self.gdrive_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "gdriveOrganizationName": gdrive_organization_name,
                "gdriveName": gdrive_name,
                "gdriveId": gdrive_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        gdrive_organization_name = d.pop("gdriveOrganizationName")

        gdrive_name = d.pop("gdriveName")

        gdrive_id = d.pop("gdriveId")

        scheduler_gsheets_options = cls(
            url=url,
            gdrive_organization_name=gdrive_organization_name,
            gdrive_name=gdrive_name,
            gdrive_id=gdrive_id,
        )

        scheduler_gsheets_options.additional_properties = d
        return scheduler_gsheets_options

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
