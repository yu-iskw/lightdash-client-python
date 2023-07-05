from enum import Enum


class PostRunUnderlyingDataQueryResponse200ResultsMetricQueryTableCalculationsItemFormatCompact(str, Enum):
    BILLIONS = "billions"
    MILLIONS = "millions"
    THOUSANDS = "thousands"
    TRILLIONS = "trillions"

    def __str__(self) -> str:
        return str(self.value)
