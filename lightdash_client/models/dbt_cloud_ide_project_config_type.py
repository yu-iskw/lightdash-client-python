from enum import Enum


class DbtCloudIDEProjectConfigType(str, Enum):
    DBT_CLOUD_IDE = "dbt_cloud_ide"

    def __str__(self) -> str:
        return str(self.value)
