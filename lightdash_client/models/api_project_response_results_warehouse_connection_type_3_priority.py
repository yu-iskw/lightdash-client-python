from enum import Enum


class ApiProjectResponseResultsWarehouseConnectionType3Priority(str, Enum):
    BATCH = "batch"
    INTERACTIVE = "interactive"

    def __str__(self) -> str:
        return str(self.value)
