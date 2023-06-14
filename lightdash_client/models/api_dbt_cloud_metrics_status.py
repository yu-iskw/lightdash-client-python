from enum import Enum


class ApiDbtCloudMetricsStatus(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
