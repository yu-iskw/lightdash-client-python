import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CacheMetadata")


@_attrs_define
class CacheMetadata:
    """
    Attributes:
        cache_hit (bool):
        cache_updated_time (Union[Unset, datetime.datetime]):
    """

    cache_hit: bool
    cache_updated_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cache_hit = self.cache_hit

        cache_updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.cache_updated_time, Unset):
            cache_updated_time = self.cache_updated_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cacheHit": cache_hit,
            }
        )
        if cache_updated_time is not UNSET:
            field_dict["cacheUpdatedTime"] = cache_updated_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cache_hit = d.pop("cacheHit")

        _cache_updated_time = d.pop("cacheUpdatedTime", UNSET)
        cache_updated_time: Union[Unset, datetime.datetime]
        if isinstance(_cache_updated_time, Unset):
            cache_updated_time = UNSET
        else:
            cache_updated_time = isoparse(_cache_updated_time)

        cache_metadata = cls(
            cache_hit=cache_hit,
            cache_updated_time=cache_updated_time,
        )

        cache_metadata.additional_properties = d
        return cache_metadata

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
