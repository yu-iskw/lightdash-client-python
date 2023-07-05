from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateShareUrlJsonBody")


@attr.s(auto_attribs=True)
class CreateShareUrlJsonBody:
    """a full URL used to generate a short url id

    Attributes:
        path (str): The URL path of the full URL
        params (str):
    """

    path: str
    params: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        params = self.params

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        params = d.pop("params")

        create_share_url_json_body = cls(
            path=path,
            params=params,
        )

        create_share_url_json_body.additional_properties = d
        return create_share_url_json_body

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
