from enum import Enum


class GetProjectResponse200ResultsDbtVersion(str, Enum):
    V1_4 = "v1.4"
    V1_5 = "v1.5"

    def __str__(self) -> str:
        return str(self.value)
