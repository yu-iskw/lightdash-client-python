import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ViewStatistics")


@_attrs_define
class ViewStatistics:
    """
    Attributes:
        first_viewed_at (Union[None, datetime.datetime, str]):
        views (float):
    """

    first_viewed_at: Union[None, datetime.datetime, str]
    views: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_viewed_at: Union[None, str]
        if isinstance(self.first_viewed_at, datetime.datetime):
            first_viewed_at = self.first_viewed_at.isoformat()
        else:
            first_viewed_at = self.first_viewed_at

        views = self.views

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstViewedAt": first_viewed_at,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_first_viewed_at(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_viewed_at_type_0 = isoparse(data)

                return first_viewed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        first_viewed_at = _parse_first_viewed_at(d.pop("firstViewedAt"))

        views = d.pop("views")

        view_statistics = cls(
            first_viewed_at=first_viewed_at,
            views=views,
        )

        view_statistics.additional_properties = d
        return view_statistics

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
