from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination")


@_attrs_define
class KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination:
    """
    Attributes:
        page (float):
        page_size (float):
        total_results (float):
        total_page_count (float):
    """

    page: float
    page_size: float
    total_results: float
    total_page_count: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page

        page_size = self.page_size

        total_results = self.total_results

        total_page_count = self.total_page_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
                "totalResults": total_results,
                "totalPageCount": total_page_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page")

        page_size = d.pop("pageSize")

        total_results = d.pop("totalResults")

        total_page_count = d.pop("totalPageCount")

        knex_paginated_data_group_array_or_group_with_members_array_pagination = cls(
            page=page,
            page_size=page_size,
            total_results=total_results,
            total_page_count=total_page_count,
        )

        knex_paginated_data_group_array_or_group_with_members_array_pagination.additional_properties = d
        return knex_paginated_data_group_array_or_group_with_members_array_pagination

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
