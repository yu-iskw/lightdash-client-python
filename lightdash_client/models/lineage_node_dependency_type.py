from enum import Enum


class LineageNodeDependencyType(str, Enum):
    MODEL = "model"
    SEED = "seed"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
