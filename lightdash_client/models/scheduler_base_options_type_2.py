from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SchedulerBaseOptionsType2")


@attr.s(auto_attribs=True)
class SchedulerBaseOptionsType2:
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
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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

        scheduler_base_options_type_2 = cls(
            url=url,
            gdrive_organization_name=gdrive_organization_name,
            gdrive_name=gdrive_name,
            gdrive_id=gdrive_id,
        )

        scheduler_base_options_type_2.additional_properties = d
        return scheduler_base_options_type_2

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
