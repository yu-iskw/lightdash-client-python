from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.and_filter_group import AndFilterGroup
    from ..models.filter_rule import FilterRule


T = TypeVar("T", bound="OrFilterGroup")


@_attrs_define
class OrFilterGroup:
    """
    Attributes:
        or_ (List[Union['AndFilterGroup', 'FilterRule', 'OrFilterGroup']]):
        id (str):
    """

    or_: List[Union["AndFilterGroup", "FilterRule", "OrFilterGroup"]]
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.and_filter_group import AndFilterGroup

        or_ = []
        for or_item_data in self.or_:
            or_item: Dict[str, Any]
            if isinstance(or_item_data, OrFilterGroup):
                or_item = or_item_data.to_dict()
            elif isinstance(or_item_data, AndFilterGroup):
                or_item = or_item_data.to_dict()
            else:
                or_item = or_item_data.to_dict()

            or_.append(or_item)

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "or": or_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.and_filter_group import AndFilterGroup
        from ..models.filter_rule import FilterRule

        d = src_dict.copy()
        or_ = []
        _or_ = d.pop("or")
        for or_item_data in _or_:

            def _parse_or_item(data: object) -> Union["AndFilterGroup", "FilterRule", "OrFilterGroup"]:
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

            or_item = _parse_or_item(or_item_data)

            or_.append(or_item)

        id = d.pop("id")

        or_filter_group = cls(
            or_=or_,
            id=id,
        )

        or_filter_group.additional_properties = d
        return or_filter_group

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
