from enum import Enum


class SemanticLayerTypeDBT(str, Enum):
    DBT = "DBT"

    def __str__(self) -> str:
        return str(self.value)
