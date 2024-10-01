from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.semantic_layer_type_dbt import SemanticLayerTypeDBT

T = TypeVar("T", bound="DbtSemanticLayerConnection")


@_attrs_define
class DbtSemanticLayerConnection:
    """
    Attributes:
        token (str):
        domain (str):
        environment_id (str):
        type (SemanticLayerTypeDBT):
    """

    token: str
    domain: str
    environment_id: str
    type: SemanticLayerTypeDBT
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        domain = self.domain

        environment_id = self.environment_id

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "domain": domain,
                "environmentId": environment_id,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        domain = d.pop("domain")

        environment_id = d.pop("environmentId")

        type = SemanticLayerTypeDBT(d.pop("type"))

        dbt_semantic_layer_connection = cls(
            token=token,
            domain=domain,
            environment_id=environment_id,
            type=type,
        )

        dbt_semantic_layer_connection.additional_properties = d
        return dbt_semantic_layer_connection

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
