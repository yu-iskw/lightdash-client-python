from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PostRunUnderlyingDataQueryJsonBodyAdditionalMetricsItemFiltersItemTarget")


@attr.s(auto_attribs=True)
class PostRunUnderlyingDataQueryJsonBodyAdditionalMetricsItemFiltersItemTarget:
    """
    Attributes:
        field_ref (str):
    """

    field_ref: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_ref = self.field_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fieldRef": field_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_ref = d.pop("fieldRef")

        post_run_underlying_data_query_json_body_additional_metrics_item_filters_item_target = cls(
            field_ref=field_ref,
        )

        post_run_underlying_data_query_json_body_additional_metrics_item_filters_item_target.additional_properties = d
        return post_run_underlying_data_query_json_body_additional_metrics_item_filters_item_target

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
