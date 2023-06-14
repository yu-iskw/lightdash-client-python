from enum import Enum


class ApiDbtCloudSettingsDeleteSuccessStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
