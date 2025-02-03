from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_postgres import WarehouseTypesPOSTGRES
from ..models.warehouse_types_redshift import WarehouseTypesREDSHIFT
from ..models.warehouse_types_snowflake import WarehouseTypesSNOWFLAKE
from ..models.warehouse_types_trino import WarehouseTypesTRINO
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser",
)


@_attrs_define
class PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        user (str):
        type (Union[WarehouseTypesPOSTGRES, WarehouseTypesREDSHIFT, WarehouseTypesSNOWFLAKE, WarehouseTypesTRINO]):
    """

    user: str
    type: Union[WarehouseTypesPOSTGRES, WarehouseTypesREDSHIFT, WarehouseTypesSNOWFLAKE, WarehouseTypesTRINO]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        type: str
        if isinstance(self.type, WarehouseTypesPOSTGRES):
            type = self.type.value
        elif isinstance(self.type, WarehouseTypesREDSHIFT):
            type = self.type.value
        elif isinstance(self.type, WarehouseTypesSNOWFLAKE):
            type = self.type.value
        else:
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        def _parse_type(
            data: object,
        ) -> Union[WarehouseTypesPOSTGRES, WarehouseTypesREDSHIFT, WarehouseTypesSNOWFLAKE, WarehouseTypesTRINO]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = WarehouseTypesPOSTGRES(data)

                return type_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = WarehouseTypesREDSHIFT(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2 = WarehouseTypesSNOWFLAKE(data)

                return type_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            type_type_3 = WarehouseTypesTRINO(data)

            return type_type_3

        type = _parse_type(d.pop("type"))

        pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user = cls(
            user=user,
            type=type,
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
