from enum import Enum


class ProjectWarehouseConnectionType3Priority(str, Enum):
    BATCH = "batch"
    INTERACTIVE = "interactive"

    def __str__(self) -> str:
        return str(self.value)
