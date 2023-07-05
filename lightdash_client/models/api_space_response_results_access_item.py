from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_space_response_results_access_item_role import (
    ApiSpaceResponseResultsAccessItemRole,
)

T = TypeVar("T", bound="ApiSpaceResponseResultsAccessItem")


@attr.s(auto_attribs=True)
class ApiSpaceResponseResultsAccessItem:
    """
    Attributes:
        role (ApiSpaceResponseResultsAccessItemRole):
        last_name (str):
        first_name (str):
        user_uuid (str):
    """

    role: ApiSpaceResponseResultsAccessItemRole
    last_name: str
    first_name: str
    user_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        last_name = self.last_name
        first_name = self.first_name
        user_uuid = self.user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "lastName": last_name,
                "firstName": first_name,
                "userUuid": user_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = ApiSpaceResponseResultsAccessItemRole(d.pop("role"))

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        user_uuid = d.pop("userUuid")

        api_space_response_results_access_item = cls(
            role=role,
            last_name=last_name,
            first_name=first_name,
            user_uuid=user_uuid,
        )

        api_space_response_results_access_item.additional_properties = d
        return api_space_response_results_access_item

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
