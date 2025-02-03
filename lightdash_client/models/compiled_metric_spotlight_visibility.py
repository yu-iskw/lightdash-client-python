from enum import Enum


class CompiledMetricSpotlightVisibility(str, Enum):
    HIDE = "hide"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
