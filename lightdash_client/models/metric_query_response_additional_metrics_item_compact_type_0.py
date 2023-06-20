from enum import Enum


class MetricQueryResponseAdditionalMetricsItemCompactType0(str, Enum):
    BILLIONS = "billions"
    MILLIONS = "millions"
    THOUSANDS = "thousands"
    TRILLIONS = "trillions"

    def __str__(self) -> str:
        return str(self.value)
