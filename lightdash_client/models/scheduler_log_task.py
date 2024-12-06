from enum import Enum


class SchedulerLogTask(str, Enum):
    COMPILEPROJECT = "compileProject"
    CREATEPROJECTWITHCOMPILE = "createProjectWithCompile"
    DOWNLOADCSV = "downloadCsv"
    HANDLESCHEDULEDDELIVERY = "handleScheduledDelivery"
    INDEXCATALOG = "indexCatalog"
    SEMANTICLAYER = "semanticLayer"
    SENDEMAILNOTIFICATION = "sendEmailNotification"
    SENDSLACKNOTIFICATION = "sendSlackNotification"
    SQLRUNNER = "sqlRunner"
    SQLRUNNERPIVOTQUERY = "sqlRunnerPivotQuery"
    TESTANDCOMPILEPROJECT = "testAndCompileProject"
    UPLOADGSHEETFROMQUERY = "uploadGsheetFromQuery"
    UPLOADGSHEETS = "uploadGsheets"
    VALIDATEPROJECT = "validateProject"

    def __str__(self) -> str:
        return str(self.value)
