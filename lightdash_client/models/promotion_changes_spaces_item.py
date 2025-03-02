from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.promotion_action import PromotionAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_space_summary_exclude_keyof_space_summary_user_access import (
        PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess,
    )


T = TypeVar("T", bound="PromotionChangesSpacesItem")


@_attrs_define
class PromotionChangesSpacesItem:
    """
    Attributes:
        data (PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess): From T, pick a set of properties whose keys are in
            the union K
        action (PromotionAction):
    """

    data: "PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess"
    action: PromotionAction
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_space_summary_exclude_keyof_space_summary_user_access import (
            PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess,
        )

        data = self.data.to_dict()

        action = self.action.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_space_summary_exclude_keyof_space_summary_user_access import (
            PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess,
        )

        d = src_dict.copy()
        data = PickSpaceSummaryExcludeKeyofSpaceSummaryUserAccess.from_dict(d.pop("data"))

        action = PromotionAction(d.pop("action"))

        promotion_changes_spaces_item = cls(
            data=data,
            action=action,
        )

        promotion_changes_spaces_item.additional_properties = d
        return promotion_changes_spaces_item

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
