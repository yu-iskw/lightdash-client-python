from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="DbtCloudMetric")


@attr.s(auto_attribs=True)
class DbtCloudMetric:
    """
    Attributes:
        label (str):
        time_grains (List[str]):
        description (str):
        dimensions (List[str]):
        name (str):
        unique_id (str):
    """

    label: str
    time_grains: List[str]
    description: str
    dimensions: List[str]
    name: str
    unique_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        time_grains = self.time_grains

        description = self.description
        dimensions = self.dimensions

        name = self.name
        unique_id = self.unique_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "timeGrains": time_grains,
                "description": description,
                "dimensions": dimensions,
                "name": name,
                "uniqueId": unique_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        time_grains = cast(List[str], d.pop("timeGrains"))

        description = d.pop("description")

        dimensions = cast(List[str], d.pop("dimensions"))

        name = d.pop("name")

        unique_id = d.pop("uniqueId")

        dbt_cloud_metric = cls(
            label=label,
            time_grains=time_grains,
            description=description,
            dimensions=dimensions,
            name=name,
            unique_id=unique_id,
        )

        dbt_cloud_metric.additional_properties = d
        return dbt_cloud_metric

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
