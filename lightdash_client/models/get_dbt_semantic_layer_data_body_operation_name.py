from enum import Enum


class GetDbtSemanticLayerDataBodyOperationName(str, Enum):
    CREATEQUERY = "CreateQuery"
    GETFIELDS = "GetFields"
    GETQUERYRESULTS = "GetQueryResults"

    def __str__(self) -> str:
        return str(self.value)
