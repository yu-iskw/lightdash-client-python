from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectWarehouseConnectionType2StartOfWeek")


@attr.s(auto_attribs=True)
class ProjectWarehouseConnectionType2StartOfWeek:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_warehouse_connection_type_2_start_of_week = cls()

        project_warehouse_connection_type_2_start_of_week.additional_properties = d
        return project_warehouse_connection_type_2_start_of_week

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
