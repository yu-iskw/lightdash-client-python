from enum import Enum


class SchedulerWithLogsLogsItemTask(str, Enum):
    COMPILEPROJECT = "compileProject"
    DOWNLOADCSV = "downloadCsv"
    HANDLESCHEDULEDDELIVERY = "handleScheduledDelivery"
    SENDEMAILNOTIFICATION = "sendEmailNotification"
    SENDSLACKNOTIFICATION = "sendSlackNotification"
    TESTANDCOMPILEPROJECT = "testAndCompileProject"
    VALIDATEPROJECT = "validateProject"

    def __str__(self) -> str:
        return str(self.value)
