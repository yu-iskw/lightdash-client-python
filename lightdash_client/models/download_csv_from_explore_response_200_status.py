from enum import Enum


class DownloadCsvFromExploreResponse200Status(str, Enum):
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
