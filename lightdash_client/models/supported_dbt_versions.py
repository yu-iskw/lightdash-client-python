from enum import Enum


class SupportedDbtVersions(str, Enum):
    V1_4 = "v1.4"
    V1_5 = "v1.5"
    V1_6 = "v1.6"
    V1_7 = "v1.7"
    V1_8 = "v1.8"
    V1_9 = "v1.9"

    def __str__(self) -> str:
        return str(self.value)
