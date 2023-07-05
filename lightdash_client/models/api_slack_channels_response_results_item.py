from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiSlackChannelsResponseResultsItem")


@attr.s(auto_attribs=True)
class ApiSlackChannelsResponseResultsItem:
    """
    Attributes:
        name (str):
        id (str):
    """

    name: str
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        api_slack_channels_response_results_item = cls(
            name=name,
            id=id,
        )

        api_slack_channels_response_results_item.additional_properties = d
        return api_slack_channels_response_results_item

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
