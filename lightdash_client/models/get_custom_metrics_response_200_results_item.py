from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCustomMetricsResponse200ResultsItem")


@_attrs_define
class GetCustomMetricsResponse200ResultsItem:
    """
    Attributes:
        chart_url (str):
        chart_label (str):
        yml (str):
        model_name (str):
        label (str):
        name (str):
    """

    chart_url: str
    chart_label: str
    yml: str
    model_name: str
    label: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chart_url = self.chart_url

        chart_label = self.chart_label

        yml = self.yml

        model_name = self.model_name

        label = self.label

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chartUrl": chart_url,
                "chartLabel": chart_label,
                "yml": yml,
                "modelName": model_name,
                "label": label,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chart_url = d.pop("chartUrl")

        chart_label = d.pop("chartLabel")

        yml = d.pop("yml")

        model_name = d.pop("modelName")

        label = d.pop("label")

        name = d.pop("name")

        get_custom_metrics_response_200_results_item = cls(
            chart_url=chart_url,
            chart_label=chart_label,
            yml=yml,
            model_name=model_name,
            label=label,
            name=name,
        )

        get_custom_metrics_response_200_results_item.additional_properties = d
        return get_custom_metrics_response_200_results_item

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
