from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_databricks import WarehouseTypesDATABRICKS

T = TypeVar("T", bound="PickCreateDatabricksCredentialsTypeOrPersonalAccessToken")


@_attrs_define
class PickCreateDatabricksCredentialsTypeOrPersonalAccessToken:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesDATABRICKS):
        personal_access_token (str):
    """

    type: WarehouseTypesDATABRICKS
    personal_access_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        personal_access_token = self.personal_access_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "personalAccessToken": personal_access_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesDATABRICKS(d.pop("type"))

        personal_access_token = d.pop("personalAccessToken")

        pick_create_databricks_credentials_type_or_personal_access_token = cls(
            type=type,
            personal_access_token=personal_access_token,
        )

        pick_create_databricks_credentials_type_or_personal_access_token.additional_properties = d
        return pick_create_databricks_credentials_type_or_personal_access_token

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
