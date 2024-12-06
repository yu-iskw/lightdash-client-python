from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.semantic_layer_type_cube import SemanticLayerTypeCUBE
from ..types import UNSET, Unset

T = TypeVar("T", bound="CubeSemanticLayerConnection")


@_attrs_define
class CubeSemanticLayerConnection:
    """
    Attributes:
        token (str):
        domain (str):
        type (SemanticLayerTypeCUBE):
    """

    token: str
    domain: str
    type: SemanticLayerTypeCUBE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token

        domain = self.domain

        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "domain": domain,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        domain = d.pop("domain")

        type = SemanticLayerTypeCUBE(d.pop("type"))

        cube_semantic_layer_connection = cls(
            token=token,
            domain=domain,
            type=type,
        )

        cube_semantic_layer_connection.additional_properties = d
        return cube_semantic_layer_connection

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
