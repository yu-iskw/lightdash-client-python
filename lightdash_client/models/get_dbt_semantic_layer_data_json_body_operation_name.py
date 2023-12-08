from enum import Enum


class GetDbtSemanticLayerDataJsonBodyOperationName(str, Enum):
    CREATEQUERY = "CreateQuery"
    GETFIELDS = "GetFields"
    GETQUERYRESULTS = "GetQueryResults"

    def __str__(self) -> str:
        return str(self.value)
