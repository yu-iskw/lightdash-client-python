from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PostRunQueryJsonBodySortsItem")


@attr.s(auto_attribs=True)
class PostRunQueryJsonBodySortsItem:
    """
    Attributes:
        descending (bool):
        field_id (str):
    """

    descending: bool
    field_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descending = self.descending
        field_id = self.field_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "descending": descending,
                "fieldId": field_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        descending = d.pop("descending")

        field_id = d.pop("fieldId")

        post_run_query_json_body_sorts_item = cls(
            descending=descending,
            field_id=field_id,
        )

        post_run_query_json_body_sorts_item.additional_properties = d
        return post_run_query_json_body_sorts_item

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
