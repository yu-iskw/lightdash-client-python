from enum import Enum


class DbtAzureDevOpsProjectConfigType(str, Enum):
    AZURE_DEVOPS = "azure_devops"

    def __str__(self) -> str:
        return str(self.value)
