from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_vis_spec import CustomVisSpec


T = TypeVar("T", bound="CustomVis")


@_attrs_define
class CustomVis:
    """
    Attributes:
        spec (Union[Unset, CustomVisSpec]):
    """

    spec: Union[Unset, "CustomVisSpec"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_vis_spec import CustomVisSpec

        d = src_dict.copy()
        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, CustomVisSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = CustomVisSpec.from_dict(_spec)

        custom_vis = cls(
            spec=spec,
        )

        custom_vis.additional_properties = d
        return custom_vis

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
