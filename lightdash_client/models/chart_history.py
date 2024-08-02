from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pick_chart_version_chart_uuid_or_version_uuid_or_created_at_or_created_by import (
        PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy,
    )


T = TypeVar("T", bound="ChartHistory")


@_attrs_define
class ChartHistory:
    """
    Attributes:
        history (List['PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy']):
    """

    history: List["PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_chart_version_chart_uuid_or_version_uuid_or_created_at_or_created_by import (
            PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy,
        )

        d = src_dict.copy()
        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = PickChartVersionChartUuidOrVersionUuidOrCreatedAtOrCreatedBy.from_dict(history_item_data)

            history.append(history_item)

        chart_history = cls(
            history=history,
        )

        chart_history.additional_properties = d
        return chart_history

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
