from enum import Enum


class NotificationFrequency(str, Enum):
    ALWAYS = "always"
    ONCE = "once"

    def __str__(self) -> str:
        return str(self.value)
