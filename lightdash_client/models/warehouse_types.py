from enum import Enum


class WarehouseTypes(str, Enum):
    BIGQUERY = "bigquery"
    DATABRICKS = "databricks"
    POSTGRES = "postgres"
    REDSHIFT = "redshift"
    SNOWFLAKE = "snowflake"
    TRINO = "trino"

    def __str__(self) -> str:
        return str(self.value)
