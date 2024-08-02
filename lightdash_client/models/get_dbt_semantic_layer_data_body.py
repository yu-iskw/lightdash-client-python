from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_dbt_semantic_layer_data_body_operation_name import (
    GetDbtSemanticLayerDataBodyOperationName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDbtSemanticLayerDataBody")


@_attrs_define
class GetDbtSemanticLayerDataBody:
    """graphql query

    Attributes:
        query (str):
        operation_name (Union[Unset, GetDbtSemanticLayerDataBodyOperationName]):
    """

    query: str
    operation_name: Union[Unset, GetDbtSemanticLayerDataBodyOperationName] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query = self.query

        operation_name: Union[Unset, str] = UNSET
        if not isinstance(self.operation_name, Unset):
            operation_name = self.operation_name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query")

        _operation_name = d.pop("operationName", UNSET)
        operation_name: Union[Unset, GetDbtSemanticLayerDataBodyOperationName]
        if isinstance(_operation_name, Unset):
            operation_name = UNSET
        else:
            operation_name = GetDbtSemanticLayerDataBodyOperationName(_operation_name)

        get_dbt_semantic_layer_data_body = cls(
            query=query,
            operation_name=operation_name,
        )

        get_dbt_semantic_layer_data_body.additional_properties = d
        return get_dbt_semantic_layer_data_body

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
