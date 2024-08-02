from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiCsvUrlResponseResults")


@_attrs_define
class ApiCsvUrlResponseResults:
    """
    Attributes:
        truncated (bool):
        status (str):
        url (str):
    """

    truncated: bool
    status: str
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        truncated = self.truncated

        status = self.status

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "truncated": truncated,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        truncated = d.pop("truncated")

        status = d.pop("status")

        url = d.pop("url")

        api_csv_url_response_results = cls(
            truncated=truncated,
            status=status,
            url=url,
        )

        api_csv_url_response_results.additional_properties = d
        return api_csv_url_response_results

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
