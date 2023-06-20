from enum import Enum


class DbtProjectConfigType5Type(str, Enum):
    AZURE_DEVOPS = "azure_devops"

    def __str__(self) -> str:
        return str(self.value)
