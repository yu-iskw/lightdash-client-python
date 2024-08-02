from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_label import CustomLabel
    from ..models.metric_query_response import MetricQueryResponse


T = TypeVar("T", bound="UploadMetricGsheet")


@_attrs_define
class UploadMetricGsheet:
    """
    Attributes:
        column_order (List[str]):
        show_table_names (bool):
        metric_query (MetricQueryResponse):
        explore_id (str):
        project_uuid (str):
        hidden_fields (Union[Unset, List[str]]):
        custom_labels (Union[Unset, CustomLabel]):
    """

    column_order: List[str]
    show_table_names: bool
    metric_query: "MetricQueryResponse"
    explore_id: str
    project_uuid: str
    hidden_fields: Union[Unset, List[str]] = UNSET
    custom_labels: Union[Unset, "CustomLabel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        column_order = self.column_order

        show_table_names = self.show_table_names

        metric_query = self.metric_query.to_dict()

        explore_id = self.explore_id

        project_uuid = self.project_uuid

        hidden_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hidden_fields, Unset):
            hidden_fields = self.hidden_fields

        custom_labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_labels, Unset):
            custom_labels = self.custom_labels.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnOrder": column_order,
                "showTableNames": show_table_names,
                "metricQuery": metric_query,
                "exploreId": explore_id,
                "projectUuid": project_uuid,
            }
        )
        if hidden_fields is not UNSET:
            field_dict["hiddenFields"] = hidden_fields
        if custom_labels is not UNSET:
            field_dict["customLabels"] = custom_labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_label import CustomLabel
        from ..models.metric_query_response import MetricQueryResponse

        d = src_dict.copy()
        column_order = cast(List[str], d.pop("columnOrder"))

        show_table_names = d.pop("showTableNames")

        metric_query = MetricQueryResponse.from_dict(d.pop("metricQuery"))

        explore_id = d.pop("exploreId")

        project_uuid = d.pop("projectUuid")

        hidden_fields = cast(List[str], d.pop("hiddenFields", UNSET))

        _custom_labels = d.pop("customLabels", UNSET)
        custom_labels: Union[Unset, CustomLabel]
        if isinstance(_custom_labels, Unset):
            custom_labels = UNSET
        else:
            custom_labels = CustomLabel.from_dict(_custom_labels)

        upload_metric_gsheet = cls(
            column_order=column_order,
            show_table_names=show_table_names,
            metric_query=metric_query,
            explore_id=explore_id,
            project_uuid=project_uuid,
            hidden_fields=hidden_fields,
            custom_labels=custom_labels,
        )

        upload_metric_gsheet.additional_properties = d
        return upload_metric_gsheet

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
