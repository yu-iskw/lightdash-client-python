from enum import Enum


class ApiNotificationResourceTypeDashboardComments(str, Enum):
    DASHBOARDCOMMENTS = "dashboardComments"

    def __str__(self) -> str:
        return str(self.value)
