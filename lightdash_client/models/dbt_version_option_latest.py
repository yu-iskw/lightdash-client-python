from enum import Enum


class DbtVersionOptionLatest(str, Enum):
    LATEST = "latest"

    def __str__(self) -> str:
        return str(self.value)
