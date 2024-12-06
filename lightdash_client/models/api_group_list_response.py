from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_group_list_response_status import ApiGroupListResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knex_paginated_data_group_array_or_group_with_members_array import (
        KnexPaginatedDataGroupArrayOrGroupWithMembersArray,
    )


T = TypeVar("T", bound="ApiGroupListResponse")


@_attrs_define
class ApiGroupListResponse:
    """
    Attributes:
        results (KnexPaginatedDataGroupArrayOrGroupWithMembersArray):
        status (ApiGroupListResponseStatus):
    """

    results: "KnexPaginatedDataGroupArrayOrGroupWithMembersArray"
    status: ApiGroupListResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.knex_paginated_data_group_array_or_group_with_members_array import (
            KnexPaginatedDataGroupArrayOrGroupWithMembersArray,
        )

        results = self.results.to_dict()

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.knex_paginated_data_group_array_or_group_with_members_array import (
            KnexPaginatedDataGroupArrayOrGroupWithMembersArray,
        )

        d = src_dict.copy()
        results = KnexPaginatedDataGroupArrayOrGroupWithMembersArray.from_dict(d.pop("results"))

        status = ApiGroupListResponseStatus(d.pop("status"))

        api_group_list_response = cls(
            results=results,
            status=status,
        )

        api_group_list_response.additional_properties = d
        return api_group_list_response

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
