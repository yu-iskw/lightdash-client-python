from enum import Enum


class ProjectTablesConfigurationTableSelectionType(str, Enum):
    ALL = "ALL"
    WITH_NAMES = "WITH_NAMES"
    WITH_TAGS = "WITH_TAGS"

    def __str__(self) -> str:
        return str(self.value)
