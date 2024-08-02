from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PullRequestCreated")


@_attrs_define
class PullRequestCreated:
    """
    Attributes:
        pr_url (str):
        pr_title (str):
    """

    pr_url: str
    pr_title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pr_url = self.pr_url

        pr_title = self.pr_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prUrl": pr_url,
                "prTitle": pr_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pr_url = d.pop("prUrl")

        pr_title = d.pop("prTitle")

        pull_request_created = cls(
            pr_url=pr_url,
            pr_title=pr_title,
        )

        pull_request_created.additional_properties = d
        return pull_request_created

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
