from enum import Enum


class CreateSshKeyPairResponse201Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
