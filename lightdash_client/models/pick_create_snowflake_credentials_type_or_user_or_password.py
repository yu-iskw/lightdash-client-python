from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_snowflake import WarehouseTypesSNOWFLAKE
from ..types import UNSET, Unset

T = TypeVar("T", bound="PickCreateSnowflakeCredentialsTypeOrUserOrPassword")


@_attrs_define
class PickCreateSnowflakeCredentialsTypeOrUserOrPassword:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user (str):
        type (WarehouseTypesSNOWFLAKE):
        password (Union[Unset, str]):
    """

    user: str
    type: WarehouseTypesSNOWFLAKE
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        type = self.type.value

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "type": type,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        type = WarehouseTypesSNOWFLAKE(d.pop("type"))

        password = d.pop("password", UNSET)

        pick_create_snowflake_credentials_type_or_user_or_password = cls(
            user=user,
            type=type,
            password=password,
        )

        pick_create_snowflake_credentials_type_or_user_or_password.additional_properties = d
        return pick_create_snowflake_credentials_type_or_user_or_password

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
