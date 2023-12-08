from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_dbt_semantic_layer_data_json_body_operation_name import (
    GetDbtSemanticLayerDataJsonBodyOperationName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDbtSemanticLayerDataJsonBody")


@attr.s(auto_attribs=True)
class GetDbtSemanticLayerDataJsonBody:
    """graphql query

    Attributes:
        query (str):
        operation_name (Union[Unset, GetDbtSemanticLayerDataJsonBodyOperationName]):
    """

    query: str
    operation_name: Union[Unset, GetDbtSemanticLayerDataJsonBodyOperationName] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        operation_name: Union[Unset, GetDbtSemanticLayerDataJsonBodyOperationName]
        if isinstance(_operation_name, Unset):
            operation_name = UNSET
        else:
            operation_name = GetDbtSemanticLayerDataJsonBodyOperationName(_operation_name)

        get_dbt_semantic_layer_data_json_body = cls(
            query=query,
            operation_name=operation_name,
        )

        get_dbt_semantic_layer_data_json_body.additional_properties = d
        return get_dbt_semantic_layer_data_json_body

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
