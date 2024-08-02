from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chart_type_custom import ChartTypeCUSTOM
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_vis import CustomVis


T = TypeVar("T", bound="CustomVisConfig")


@_attrs_define
class CustomVisConfig:
    """
    Attributes:
        type (ChartTypeCUSTOM):
        config (Union[Unset, CustomVis]):
    """

    type: ChartTypeCUSTOM
    config: Union[Unset, "CustomVis"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_vis import CustomVis

        d = src_dict.copy()
        type = ChartTypeCUSTOM(d.pop("type"))

        _config = d.pop("config", UNSET)
        config: Union[Unset, CustomVis]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = CustomVis.from_dict(_config)

        custom_vis_config = cls(
            type=type,
            config=config,
        )

        custom_vis_config.additional_properties = d
        return custom_vis_config

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
