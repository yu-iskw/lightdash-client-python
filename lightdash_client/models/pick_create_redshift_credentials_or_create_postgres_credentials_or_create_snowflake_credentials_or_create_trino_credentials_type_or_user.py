from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_snowflake import WarehouseTypesSNOWFLAKE

T = TypeVar(
    "T",
    bound="PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser",
)


@_attrs_define
class PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesSNOWFLAKE):
        user (str):
    """

    type: WarehouseTypesSNOWFLAKE
    user: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = WarehouseTypesSNOWFLAKE(d.pop("type"))

        user = d.pop("user")

        pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user = cls(
            type=type,
            user=user,
        )

        pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user.additional_properties = d
        return pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user

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
