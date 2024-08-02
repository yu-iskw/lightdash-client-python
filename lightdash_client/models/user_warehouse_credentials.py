import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.pick_create_bigquery_credentials_type import (
        PickCreateBigqueryCredentialsType,
    )
    from ..models.pick_create_databricks_credentials_type import (
        PickCreateDatabricksCredentialsType,
    )
    from ..models.pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user import (
        PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser,
    )


T = TypeVar("T", bound="UserWarehouseCredentials")


@_attrs_define
class UserWarehouseCredentials:
    """
    Attributes:
        credentials (Union['PickCreateBigqueryCredentialsType', 'PickCreateDatabricksCredentialsType', 'PickCreateRedshi
            ftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser']):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        name (str):
        user_uuid (str):
        uuid (str):
    """

    credentials: Union[
        "PickCreateBigqueryCredentialsType",
        "PickCreateDatabricksCredentialsType",
        "PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser",
    ]
    updated_at: datetime.datetime
    created_at: datetime.datetime
    name: str
    user_uuid: str
    uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_create_bigquery_credentials_type import (
            PickCreateBigqueryCredentialsType,
        )
        from ..models.pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user import (
            PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser,
        )

        credentials: Dict[str, Any]
        if isinstance(
            self.credentials,
            PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser,
        ):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, PickCreateBigqueryCredentialsType):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        name = self.name

        user_uuid = self.user_uuid

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "name": name,
                "userUuid": user_uuid,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_create_bigquery_credentials_type import (
            PickCreateBigqueryCredentialsType,
        )
        from ..models.pick_create_databricks_credentials_type import (
            PickCreateDatabricksCredentialsType,
        )
        from ..models.pick_create_redshift_credentials_or_create_postgres_credentials_or_create_snowflake_credentials_or_create_trino_credentials_type_or_user import (
            PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser,
        )

        d = src_dict.copy()

        def _parse_credentials(
            data: object,
        ) -> Union[
            "PickCreateBigqueryCredentialsType",
            "PickCreateDatabricksCredentialsType",
            "PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = PickCreateRedshiftCredentialsOrCreatePostgresCredentialsOrCreateSnowflakeCredentialsOrCreateTrinoCredentialsTypeOrUser.from_dict(
                    data
                )

                return credentials_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_1 = PickCreateBigqueryCredentialsType.from_dict(data)

                return credentials_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_2 = PickCreateDatabricksCredentialsType.from_dict(data)

            return credentials_type_2

        credentials = _parse_credentials(d.pop("credentials"))

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        name = d.pop("name")

        user_uuid = d.pop("userUuid")

        uuid = d.pop("uuid")

        user_warehouse_credentials = cls(
            credentials=credentials,
            updated_at=updated_at,
            created_at=created_at,
            name=name,
            user_uuid=user_uuid,
            uuid=uuid,
        )

        user_warehouse_credentials.additional_properties = d
        return user_warehouse_credentials

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
