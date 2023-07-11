from enum import Enum


class ApiRunQueryResponseResultsMetricQueryAdditionalMetricsItemFiltersItemOperator(str, Enum):
    DOESNOTINCLUDE = "doesNotInclude"
    ENDSWITH = "endsWith"
    EQUALS = "equals"
    GREATERTHAN = "greaterThan"
    GREATERTHANOREQUAL = "greaterThanOrEqual"
    INBETWEEN = "inBetween"
    INCLUDE = "include"
    INTHECURRENT = "inTheCurrent"
    INTHENEXT = "inTheNext"
    INTHEPAST = "inThePast"
    ISNULL = "isNull"
    LESSTHAN = "lessThan"
    LESSTHANOREQUAL = "lessThanOrEqual"
    NOTEQUALS = "notEquals"
    NOTINTHEPAST = "notInThePast"
    NOTNULL = "notNull"
    STARTSWITH = "startsWith"

    def __str__(self) -> str:
        return str(self.value)
