from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dbt_version_option_latest import DbtVersionOptionLatest
from ..models.project_type import ProjectType
from ..models.supported_dbt_versions import SupportedDbtVersions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cube_semantic_layer_connection import CubeSemanticLayerConnection
    from ..models.dbt_azure_dev_ops_project_config import DbtAzureDevOpsProjectConfig
    from ..models.dbt_bit_bucket_project_config import DbtBitBucketProjectConfig
    from ..models.dbt_cloud_ide_project_config import DbtCloudIDEProjectConfig
    from ..models.dbt_github_project_config import DbtGithubProjectConfig
    from ..models.dbt_gitlab_project_config import DbtGitlabProjectConfig
    from ..models.dbt_local_project_config import DbtLocalProjectConfig
    from ..models.dbt_none_project_config import DbtNoneProjectConfig
    from ..models.dbt_semantic_layer_connection import DbtSemanticLayerConnection
    from ..models.pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names import (
        PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames,
    )
    from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names import (
        PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames,
    )
    from ..models.pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names import (
        PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames,
    )
    from ..models.pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names import (
        PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames,
    )
    from ..models.pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names import (
        PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames,
    )
    from ..models.pick_create_trino_credentials_exclude_keyof_create_trino_credentials_sensitive_credentials_field_names import (
        PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames,
    )


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        created_by_user_uuid (Union[None, str]):
        scheduler_timezone (str):
        dbt_version (Union[DbtVersionOptionLatest, SupportedDbtVersions]):
        dbt_connection (Union['DbtAzureDevOpsProjectConfig', 'DbtBitBucketProjectConfig', 'DbtCloudIDEProjectConfig',
            'DbtGithubProjectConfig', 'DbtGitlabProjectConfig', 'DbtLocalProjectConfig', 'DbtNoneProjectConfig']):
        type (ProjectType):
        name (str):
        project_uuid (str):
        organization_uuid (str):
        semantic_layer_connection (Union['CubeSemanticLayerConnection', 'DbtSemanticLayerConnection', Unset]):
        upstream_project_uuid (Union[Unset, str]):
        pinned_list_uuid (Union[Unset, str]):
        warehouse_connection
            (Union['PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames',
            'PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames',
            'PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames',
            'PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames',
            'PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames',
            'PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames', Unset]):
    """

    created_by_user_uuid: Union[None, str]
    scheduler_timezone: str
    dbt_version: Union[DbtVersionOptionLatest, SupportedDbtVersions]
    dbt_connection: Union[
        "DbtAzureDevOpsProjectConfig",
        "DbtBitBucketProjectConfig",
        "DbtCloudIDEProjectConfig",
        "DbtGithubProjectConfig",
        "DbtGitlabProjectConfig",
        "DbtLocalProjectConfig",
        "DbtNoneProjectConfig",
    ]
    type: ProjectType
    name: str
    project_uuid: str
    organization_uuid: str
    semantic_layer_connection: Union["CubeSemanticLayerConnection", "DbtSemanticLayerConnection", Unset] = UNSET
    upstream_project_uuid: Union[Unset, str] = UNSET
    pinned_list_uuid: Union[Unset, str] = UNSET
    warehouse_connection: Union[
        "PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames",
        "PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames",
        "PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames",
        "PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames",
        "PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames",
        "PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cube_semantic_layer_connection import CubeSemanticLayerConnection
        from ..models.dbt_azure_dev_ops_project_config import DbtAzureDevOpsProjectConfig
        from ..models.dbt_bit_bucket_project_config import DbtBitBucketProjectConfig
        from ..models.dbt_cloud_ide_project_config import DbtCloudIDEProjectConfig
        from ..models.dbt_github_project_config import DbtGithubProjectConfig
        from ..models.dbt_gitlab_project_config import DbtGitlabProjectConfig
        from ..models.dbt_local_project_config import DbtLocalProjectConfig
        from ..models.dbt_none_project_config import DbtNoneProjectConfig
        from ..models.dbt_semantic_layer_connection import DbtSemanticLayerConnection
        from ..models.pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names import (
            PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names import (
            PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names import (
            PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names import (
            PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names import (
            PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_trino_credentials_exclude_keyof_create_trino_credentials_sensitive_credentials_field_names import (
            PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames,
        )

        created_by_user_uuid: Union[None, str]
        created_by_user_uuid = self.created_by_user_uuid

        scheduler_timezone = self.scheduler_timezone

        dbt_version: str
        if isinstance(self.dbt_version, SupportedDbtVersions):
            dbt_version = self.dbt_version.value
        else:
            dbt_version = self.dbt_version.value

        dbt_connection: Dict[str, Any]
        if isinstance(self.dbt_connection, DbtLocalProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        elif isinstance(self.dbt_connection, DbtCloudIDEProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        elif isinstance(self.dbt_connection, DbtGithubProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        elif isinstance(self.dbt_connection, DbtBitBucketProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        elif isinstance(self.dbt_connection, DbtGitlabProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        elif isinstance(self.dbt_connection, DbtAzureDevOpsProjectConfig):
            dbt_connection = self.dbt_connection.to_dict()
        else:
            dbt_connection = self.dbt_connection.to_dict()

        type = self.type.value

        name = self.name

        project_uuid = self.project_uuid

        organization_uuid = self.organization_uuid

        semantic_layer_connection: Union[Dict[str, Any], Unset]
        if isinstance(self.semantic_layer_connection, Unset):
            semantic_layer_connection = UNSET
        elif isinstance(self.semantic_layer_connection, DbtSemanticLayerConnection):
            semantic_layer_connection = self.semantic_layer_connection.to_dict()
        else:
            semantic_layer_connection = self.semantic_layer_connection.to_dict()

        upstream_project_uuid = self.upstream_project_uuid

        pinned_list_uuid = self.pinned_list_uuid

        warehouse_connection: Union[Dict[str, Any], Unset]
        if isinstance(self.warehouse_connection, Unset):
            warehouse_connection = UNSET
        elif isinstance(
            self.warehouse_connection,
            PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames,
        ):
            warehouse_connection = self.warehouse_connection.to_dict()
        elif isinstance(
            self.warehouse_connection,
            PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames,
        ):
            warehouse_connection = self.warehouse_connection.to_dict()
        elif isinstance(
            self.warehouse_connection,
            PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames,
        ):
            warehouse_connection = self.warehouse_connection.to_dict()
        elif isinstance(
            self.warehouse_connection,
            PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames,
        ):
            warehouse_connection = self.warehouse_connection.to_dict()
        elif isinstance(
            self.warehouse_connection,
            PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames,
        ):
            warehouse_connection = self.warehouse_connection.to_dict()
        else:
            warehouse_connection = self.warehouse_connection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdByUserUuid": created_by_user_uuid,
                "schedulerTimezone": scheduler_timezone,
                "dbtVersion": dbt_version,
                "dbtConnection": dbt_connection,
                "type": type,
                "name": name,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
            }
        )
        if semantic_layer_connection is not UNSET:
            field_dict["semanticLayerConnection"] = semantic_layer_connection
        if upstream_project_uuid is not UNSET:
            field_dict["upstreamProjectUuid"] = upstream_project_uuid
        if pinned_list_uuid is not UNSET:
            field_dict["pinnedListUuid"] = pinned_list_uuid
        if warehouse_connection is not UNSET:
            field_dict["warehouseConnection"] = warehouse_connection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cube_semantic_layer_connection import CubeSemanticLayerConnection
        from ..models.dbt_azure_dev_ops_project_config import DbtAzureDevOpsProjectConfig
        from ..models.dbt_bit_bucket_project_config import DbtBitBucketProjectConfig
        from ..models.dbt_cloud_ide_project_config import DbtCloudIDEProjectConfig
        from ..models.dbt_github_project_config import DbtGithubProjectConfig
        from ..models.dbt_gitlab_project_config import DbtGitlabProjectConfig
        from ..models.dbt_local_project_config import DbtLocalProjectConfig
        from ..models.dbt_none_project_config import DbtNoneProjectConfig
        from ..models.dbt_semantic_layer_connection import DbtSemanticLayerConnection
        from ..models.pick_create_bigquery_credentials_exclude_keyof_create_bigquery_credentials_sensitive_credentials_field_names import (
            PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_databricks_credentials_exclude_keyof_create_databricks_credentials_sensitive_credentials_field_names import (
            PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_postgres_credentials_exclude_keyof_create_postgres_credentials_sensitive_credentials_field_names import (
            PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_redshift_credentials_exclude_keyof_create_redshift_credentials_sensitive_credentials_field_names import (
            PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_snowflake_credentials_exclude_keyof_create_snowflake_credentials_sensitive_credentials_field_names import (
            PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames,
        )
        from ..models.pick_create_trino_credentials_exclude_keyof_create_trino_credentials_sensitive_credentials_field_names import (
            PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames,
        )

        d = src_dict.copy()

        def _parse_created_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_uuid = _parse_created_by_user_uuid(d.pop("createdByUserUuid"))

        scheduler_timezone = d.pop("schedulerTimezone")

        def _parse_dbt_version(data: object) -> Union[DbtVersionOptionLatest, SupportedDbtVersions]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_dbt_version_option_type_0 = SupportedDbtVersions(data)

                return componentsschemas_dbt_version_option_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_dbt_version_option_type_1 = DbtVersionOptionLatest(data)

            return componentsschemas_dbt_version_option_type_1

        dbt_version = _parse_dbt_version(d.pop("dbtVersion"))

        def _parse_dbt_connection(
            data: object,
        ) -> Union[
            "DbtAzureDevOpsProjectConfig",
            "DbtBitBucketProjectConfig",
            "DbtCloudIDEProjectConfig",
            "DbtGithubProjectConfig",
            "DbtGitlabProjectConfig",
            "DbtLocalProjectConfig",
            "DbtNoneProjectConfig",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_0 = DbtLocalProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_1 = DbtCloudIDEProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_2 = DbtGithubProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_3 = DbtBitBucketProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_4 = DbtGitlabProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dbt_project_config_type_5 = DbtAzureDevOpsProjectConfig.from_dict(data)

                return componentsschemas_dbt_project_config_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_dbt_project_config_type_6 = DbtNoneProjectConfig.from_dict(data)

            return componentsschemas_dbt_project_config_type_6

        dbt_connection = _parse_dbt_connection(d.pop("dbtConnection"))

        type = ProjectType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_semantic_layer_connection(
            data: object,
        ) -> Union["CubeSemanticLayerConnection", "DbtSemanticLayerConnection", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_semantic_layer_connection_type_0 = DbtSemanticLayerConnection.from_dict(data)

                return componentsschemas_semantic_layer_connection_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_semantic_layer_connection_type_1 = CubeSemanticLayerConnection.from_dict(data)

            return componentsschemas_semantic_layer_connection_type_1

        semantic_layer_connection = _parse_semantic_layer_connection(d.pop("semanticLayerConnection", UNSET))

        upstream_project_uuid = d.pop("upstreamProjectUuid", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid", UNSET)

        def _parse_warehouse_connection(
            data: object,
        ) -> Union[
            "PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames",
            "PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames",
            "PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames",
            "PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames",
            "PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames",
            "PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_warehouse_credentials_type_0 = PickCreateSnowflakeCredentialsExcludeKeyofCreateSnowflakeCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )

                return componentsschemas_warehouse_credentials_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_warehouse_credentials_type_1 = PickCreateRedshiftCredentialsExcludeKeyofCreateRedshiftCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )

                return componentsschemas_warehouse_credentials_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_warehouse_credentials_type_2 = PickCreatePostgresCredentialsExcludeKeyofCreatePostgresCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )

                return componentsschemas_warehouse_credentials_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_warehouse_credentials_type_3 = PickCreateBigqueryCredentialsExcludeKeyofCreateBigqueryCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )

                return componentsschemas_warehouse_credentials_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_warehouse_credentials_type_4 = PickCreateDatabricksCredentialsExcludeKeyofCreateDatabricksCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )

                return componentsschemas_warehouse_credentials_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_warehouse_credentials_type_5 = (
                PickCreateTrinoCredentialsExcludeKeyofCreateTrinoCredentialsSensitiveCredentialsFieldNames.from_dict(
                    data
                )
            )

            return componentsschemas_warehouse_credentials_type_5

        warehouse_connection = _parse_warehouse_connection(d.pop("warehouseConnection", UNSET))

        project = cls(
            created_by_user_uuid=created_by_user_uuid,
            scheduler_timezone=scheduler_timezone,
            dbt_version=dbt_version,
            dbt_connection=dbt_connection,
            type=type,
            name=name,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            semantic_layer_connection=semantic_layer_connection,
            upstream_project_uuid=upstream_project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            warehouse_connection=warehouse_connection,
        )

        project.additional_properties = d
        return project

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
