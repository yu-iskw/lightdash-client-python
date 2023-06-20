from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

from ..models.api_slack_channels_response_status import ApiSlackChannelsResponseStatus

if TYPE_CHECKING:
    from ..models.api_slack_channels_response_results_item import ApiSlackChannelsResponseResultsItem


T = TypeVar("T", bound="ApiSlackChannelsResponse")


@attr.s(auto_attribs=True)
class ApiSlackChannelsResponse:
    """
    Attributes:
        results (List['ApiSlackChannelsResponseResultsItem']):
        status (ApiSlackChannelsResponseStatus):
    """

    results: List["ApiSlackChannelsResponseResultsItem"]
    status: ApiSlackChannelsResponseStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_slack_channels_response_results_item import ApiSlackChannelsResponseResultsItem

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ApiSlackChannelsResponseResultsItem.from_dict(results_item_data)

            results.append(results_item)

        status = ApiSlackChannelsResponseStatus(d.pop("status"))

        api_slack_channels_response = cls(
            results=results,
            status=status,
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
