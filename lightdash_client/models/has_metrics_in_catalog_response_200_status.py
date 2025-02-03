from enum import Enum


class HasMetricsInCatalogResponse200Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
