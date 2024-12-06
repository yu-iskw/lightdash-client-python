from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.semantic_layer_type_cube import SemanticLayerTypeCUBE
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialCubeSemanticLayerConnection")


@_attrs_define
class PartialCubeSemanticLayerConnection:
    """Make all properties in T optional

    Attributes:
        type (Union[Unset, SemanticLayerTypeCUBE]):
        domain (Union[Unset, str]):
        token (Union[Unset, str]):
    """

    type: Union[Unset, SemanticLayerTypeCUBE] = UNSET
    domain: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        domain = self.domain

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if domain is not UNSET:
            field_dict["domain"] = domain
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, SemanticLayerTypeCUBE]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SemanticLayerTypeCUBE(_type)

        domain = d.pop("domain", UNSET)

        token = d.pop("token", UNSET)

        partial_cube_semantic_layer_connection = cls(
            type=type,
            domain=domain,
            token=token,
        )

        partial_cube_semantic_layer_connection.additional_properties = d
        return partial_cube_semantic_layer_connection

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
