from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.success_status import SuccessStatus
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="UpdateOrganizationMemberResponse200")


@attr.s(auto_attribs=True)
class UpdateOrganizationMemberResponse200:
    """
    Attributes:
        user_uuid (str):
        first_name (str):
        last_name (str):
        status (Union[Unset, SuccessStatus]):
        email (Union[Unset, str]):
    """

    user_uuid: str
    first_name: str
    last_name: str
    status: Union[Unset, SuccessStatus] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid
        first_name = self.first_name
        last_name = self.last_name
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userUuid": user_uuid,
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        _status = d.pop("status", UNSET)
        status: Union[Unset, SuccessStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SuccessStatus(_status)

        email = d.pop("email", UNSET)

        update_organization_member_response_200 = cls(
            user_uuid=user_uuid,
            first_name=first_name,
            last_name=last_name,
            status=status,
            email=email,
        )

        update_organization_member_response_200.additional_properties = d
        return update_organization_member_response_200

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
