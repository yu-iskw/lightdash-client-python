from enum import Enum


class DbtProjectTypeBITBUCKET(str, Enum):
    BITBUCKET = "bitbucket"

    def __str__(self) -> str:
        return str(self.value)
