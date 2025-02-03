import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="PickSavedChartUpdatedAtOrUpdatedByUserOrPinnedListOrder")


@_attrs_define
class PickSavedChartUpdatedAtOrUpdatedByUserOrPinnedListOrder:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        pinned_list_order (Union[None, float]):
        updated_at (datetime.datetime):
        updated_by_user (Union[Unset, UpdatedByUser]):
    """

    pinned_list_order: Union[None, float]
    updated_at: datetime.datetime
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.updated_by_user import UpdatedByUser

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        updated_at = self.updated_at.isoformat()

        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pinnedListOrder": pinned_list_order,
                "updatedAt": updated_at,
            }
        )
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        updated_at = isoparse(d.pop("updatedAt"))

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        pick_saved_chart_updated_at_or_updated_by_user_or_pinned_list_order = cls(
            pinned_list_order=pinned_list_order,
            updated_at=updated_at,
            updated_by_user=updated_by_user,
        )

        pick_saved_chart_updated_at_or_updated_by_user_or_pinned_list_order.additional_properties = d
        return pick_saved_chart_updated_at_or_updated_by_user_or_pinned_list_order

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
