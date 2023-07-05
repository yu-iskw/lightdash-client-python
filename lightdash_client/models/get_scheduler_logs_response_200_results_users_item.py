from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetSchedulerLogsResponse200ResultsUsersItem")


@attr.s(auto_attribs=True)
class GetSchedulerLogsResponse200ResultsUsersItem:
    """
    Attributes:
        user_uuid (str):
        last_name (str):
        first_name (str):
    """

    user_uuid: str
    last_name: str
    first_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid
        last_name = self.last_name
        first_name = self.first_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "lastName": last_name,
                "firstName": first_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        get_scheduler_logs_response_200_results_users_item = cls(
            user_uuid=user_uuid,
            last_name=last_name,
            first_name=first_name,
        )

        get_scheduler_logs_response_200_results_users_item.additional_properties = d
        return get_scheduler_logs_response_200_results_users_item

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
