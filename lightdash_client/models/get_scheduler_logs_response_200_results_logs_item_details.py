from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetSchedulerLogsResponse200ResultsLogsItemDetails")


@attr.s(auto_attribs=True)
class GetSchedulerLogsResponse200ResultsLogsItemDetails:
    """Construct a type with a set of properties K of type T"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_scheduler_logs_response_200_results_logs_item_details = cls()

        get_scheduler_logs_response_200_results_logs_item_details.additional_properties = d
        return get_scheduler_logs_response_200_results_logs_item_details

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
