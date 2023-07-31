from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ApiCreateUserAttributeResponseResultsUsersItem")


@attr.s(auto_attribs=True)
class ApiCreateUserAttributeResponseResultsUsersItem:
    """
    Attributes:
        value (str):
        email (str):
        user_uuid (str):
    """

    value: str
    email: str
    user_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        email = self.email
        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "email": email,
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        email = d.pop("email")

        user_uuid = d.pop("userUuid")

        api_create_user_attribute_response_results_users_item = cls(
            value=value,
            email=email,
            user_uuid=user_uuid,
        )

        api_create_user_attribute_response_results_users_item.additional_properties = d
        return api_create_user_attribute_response_results_users_item

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
