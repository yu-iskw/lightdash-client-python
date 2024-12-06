from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_slack_channels_response_status import ApiSlackChannelsResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slack_channel import SlackChannel


T = TypeVar("T", bound="ApiSlackChannelsResponse")


@_attrs_define
class ApiSlackChannelsResponse:
    """
    Attributes:
        status (ApiSlackChannelsResponseStatus):
        results (Union[Unset, List['SlackChannel']]):
    """

    status: ApiSlackChannelsResponseStatus
    results: Union[Unset, List["SlackChannel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.slack_channel import SlackChannel

        status = self.status.value

        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.slack_channel import SlackChannel

        d = src_dict.copy()
        status = ApiSlackChannelsResponseStatus(d.pop("status"))

        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = SlackChannel.from_dict(results_item_data)

            results.append(results_item)

        api_slack_channels_response = cls(
            status=status,
            results=results,
        )

        api_slack_channels_response.additional_properties = d
        return api_slack_channels_response

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
