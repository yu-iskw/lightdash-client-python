from enum import Enum


class SemanticLayerTypeCUBE(str, Enum):
    CUBE = "CUBE"

    def __str__(self) -> str:
        return str(self.value)
