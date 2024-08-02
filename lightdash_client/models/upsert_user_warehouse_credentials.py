from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pick_create_bigquery_credentials_type_or_keyfile_contents import (
        PickCreateBigqueryCredentialsTypeOrKeyfileContents,
    )
    from ..models.pick_create_databricks_credentials_type_or_personal_access_token import (
        PickCreateDatabricksCredentialsTypeOrPersonalAccessToken,
    )
    from ..models.pick_create_postgres_credentials_type_or_user_or_password import (
        PickCreatePostgresCredentialsTypeOrUserOrPassword,
    )
    from ..models.pick_create_redshift_credentials_type_or_user_or_password import (
        PickCreateRedshiftCredentialsTypeOrUserOrPassword,
    )
    from ..models.pick_create_snowflake_credentials_type_or_user_or_password import (
        PickCreateSnowflakeCredentialsTypeOrUserOrPassword,
    )
    from ..models.pick_create_trino_credentials_type_or_user_or_password import (
        PickCreateTrinoCredentialsTypeOrUserOrPassword,
    )


T = TypeVar("T", bound="UpsertUserWarehouseCredentials")


@_attrs_define
class UpsertUserWarehouseCredentials:
    """
    Attributes:
        credentials (Union['PickCreateBigqueryCredentialsTypeOrKeyfileContents',
            'PickCreateDatabricksCredentialsTypeOrPersonalAccessToken', 'PickCreatePostgresCredentialsTypeOrUserOrPassword',
            'PickCreateRedshiftCredentialsTypeOrUserOrPassword', 'PickCreateSnowflakeCredentialsTypeOrUserOrPassword',
            'PickCreateTrinoCredentialsTypeOrUserOrPassword']):
        name (str):
    """

    credentials: Union[
        "PickCreateBigqueryCredentialsTypeOrKeyfileContents",
        "PickCreateDatabricksCredentialsTypeOrPersonalAccessToken",
        "PickCreatePostgresCredentialsTypeOrUserOrPassword",
        "PickCreateRedshiftCredentialsTypeOrUserOrPassword",
        "PickCreateSnowflakeCredentialsTypeOrUserOrPassword",
        "PickCreateTrinoCredentialsTypeOrUserOrPassword",
    ]
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_create_bigquery_credentials_type_or_keyfile_contents import (
            PickCreateBigqueryCredentialsTypeOrKeyfileContents,
        )
        from ..models.pick_create_postgres_credentials_type_or_user_or_password import (
            PickCreatePostgresCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_redshift_credentials_type_or_user_or_password import (
            PickCreateRedshiftCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_snowflake_credentials_type_or_user_or_password import (
            PickCreateSnowflakeCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_trino_credentials_type_or_user_or_password import (
            PickCreateTrinoCredentialsTypeOrUserOrPassword,
        )

        credentials: Dict[str, Any]
        if isinstance(self.credentials, PickCreateRedshiftCredentialsTypeOrUserOrPassword):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, PickCreatePostgresCredentialsTypeOrUserOrPassword):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, PickCreateSnowflakeCredentialsTypeOrUserOrPassword):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, PickCreateTrinoCredentialsTypeOrUserOrPassword):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, PickCreateBigqueryCredentialsTypeOrKeyfileContents):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_create_bigquery_credentials_type_or_keyfile_contents import (
            PickCreateBigqueryCredentialsTypeOrKeyfileContents,
        )
        from ..models.pick_create_databricks_credentials_type_or_personal_access_token import (
            PickCreateDatabricksCredentialsTypeOrPersonalAccessToken,
        )
        from ..models.pick_create_postgres_credentials_type_or_user_or_password import (
            PickCreatePostgresCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_redshift_credentials_type_or_user_or_password import (
            PickCreateRedshiftCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_snowflake_credentials_type_or_user_or_password import (
            PickCreateSnowflakeCredentialsTypeOrUserOrPassword,
        )
        from ..models.pick_create_trino_credentials_type_or_user_or_password import (
            PickCreateTrinoCredentialsTypeOrUserOrPassword,
        )

        d = src_dict.copy()

        def _parse_credentials(
            data: object,
        ) -> Union[
            "PickCreateBigqueryCredentialsTypeOrKeyfileContents",
            "PickCreateDatabricksCredentialsTypeOrPersonalAccessToken",
            "PickCreatePostgresCredentialsTypeOrUserOrPassword",
            "PickCreateRedshiftCredentialsTypeOrUserOrPassword",
            "PickCreateSnowflakeCredentialsTypeOrUserOrPassword",
            "PickCreateTrinoCredentialsTypeOrUserOrPassword",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = PickCreateRedshiftCredentialsTypeOrUserOrPassword.from_dict(data)

                return credentials_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_1 = PickCreatePostgresCredentialsTypeOrUserOrPassword.from_dict(data)

                return credentials_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_2 = PickCreateSnowflakeCredentialsTypeOrUserOrPassword.from_dict(data)

                return credentials_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_3 = PickCreateTrinoCredentialsTypeOrUserOrPassword.from_dict(data)

                return credentials_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_4 = PickCreateBigqueryCredentialsTypeOrKeyfileContents.from_dict(data)

                return credentials_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_5 = PickCreateDatabricksCredentialsTypeOrPersonalAccessToken.from_dict(data)

            return credentials_type_5

        credentials = _parse_credentials(d.pop("credentials"))

        name = d.pop("name")

        upsert_user_warehouse_credentials = cls(
            credentials=credentials,
            name=name,
        )

        upsert_user_warehouse_credentials.additional_properties = d
        return upsert_user_warehouse_credentials

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
