from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.filter_rule import FilterRule
    from ..models.or_filter_group import OrFilterGroup


T = TypeVar("T", bound="AndFilterGroup")


@_attrs_define
class AndFilterGroup:
    """
    Attributes:
        and_ (List[Union['AndFilterGroup', 'FilterRule', 'OrFilterGroup']]):
        id (str):
    """

    and_: List[Union["AndFilterGroup", "FilterRule", "OrFilterGroup"]]
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.or_filter_group import OrFilterGroup

        and_ = []
        for and_item_data in self.and_:
            and_item: Dict[str, Any]
            if isinstance(and_item_data, OrFilterGroup):
                and_item = and_item_data.to_dict()
            elif isinstance(and_item_data, AndFilterGroup):
                and_item = and_item_data.to_dict()
            else:
                and_item = and_item_data.to_dict()

            and_.append(and_item)

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "and": and_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_rule import FilterRule
        from ..models.or_filter_group import OrFilterGroup

        d = src_dict.copy()
        and_ = []
        _and_ = d.pop("and")
        for and_item_data in _and_:

            def _parse_and_item(data: object) -> Union["AndFilterGroup", "FilterRule", "OrFilterGroup"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_filter_group_type_0 = OrFilterGroup.from_dict(data)

                    return componentsschemas_filter_group_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_filter_group_type_1 = AndFilterGroup.from_dict(data)

                    return componentsschemas_filter_group_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_item_type_1 = FilterRule.from_dict(data)

                return componentsschemas_filter_group_item_type_1

            and_item = _parse_and_item(and_item_data)

            and_.append(and_item)

        id = d.pop("id")

        and_filter_group = cls(
            and_=and_,
            id=id,
        )

        and_filter_group.additional_properties = d
        return and_filter_group

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
