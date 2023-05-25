from enum import Enum


class JobJobType(str, Enum):
    COMPILE_PROJECT = "COMPILE_PROJECT"
    CREATE_PROJECT = "CREATE_PROJECT"

    def __str__(self) -> str:
        return str(self.value)
