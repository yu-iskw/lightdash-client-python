from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="TilePropertiesChart")


@attr.s(auto_attribs=True)
class TilePropertiesChart:
    """
    Attributes:
        saved_chart_uuid (Optional[str]):
    """

    saved_chart_uuid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_chart_uuid = self.saved_chart_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "savedChartUuid": saved_chart_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_chart_uuid = d.pop("savedChartUuid")

        tile_properties_chart = cls(
            saved_chart_uuid=saved_chart_uuid,
        )

        tile_properties_chart.additional_properties = d
        return tile_properties_chart

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
