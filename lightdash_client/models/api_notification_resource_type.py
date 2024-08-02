from enum import Enum


class ApiNotificationResourceType(str, Enum):
    DASHBOARDCOMMENTS = "dashboardComments"

    def __str__(self) -> str:
        return str(self.value)
