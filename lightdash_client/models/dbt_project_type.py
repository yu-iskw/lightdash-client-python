from enum import Enum


class DbtProjectType(str, Enum):
    AZURE_DEVOPS = "azure_devops"
    BITBUCKET = "bitbucket"
    DBT = "dbt"
    DBT_CLOUD_IDE = "dbt_cloud_ide"
    GITHUB = "github"
    GITLAB = "gitlab"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
