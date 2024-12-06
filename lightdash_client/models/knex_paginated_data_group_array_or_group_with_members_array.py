from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.group_with_members import GroupWithMembers
    from ..models.knex_paginated_data_group_array_or_group_with_members_array_pagination import (
        KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination,
    )


T = TypeVar("T", bound="KnexPaginatedDataGroupArrayOrGroupWithMembersArray")


@_attrs_define
class KnexPaginatedDataGroupArrayOrGroupWithMembersArray:
    """
    Attributes:
        data (Union[List['Group'], List['GroupWithMembers']]):
        pagination (Union[Unset, KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination]):
    """

    data: Union[List["Group"], List["GroupWithMembers"]]
    pagination: Union[Unset, "KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group import Group
        from ..models.group_with_members import GroupWithMembers
        from ..models.knex_paginated_data_group_array_or_group_with_members_array_pagination import (
            KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination,
        )

        data: List[Dict[str, Any]]
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = []
            for data_type_1_item_data in self.data:
                data_type_1_item = data_type_1_item_data.to_dict()
                data.append(data_type_1_item)

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group import Group
        from ..models.group_with_members import GroupWithMembers
        from ..models.knex_paginated_data_group_array_or_group_with_members_array_pagination import (
            KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination,
        )

        d = src_dict.copy()

        def _parse_data(data: object) -> Union[List["Group"], List["GroupWithMembers"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = Group.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = []
            _data_type_1 = data
            for data_type_1_item_data in _data_type_1:
                data_type_1_item = GroupWithMembers.from_dict(data_type_1_item_data)

                data_type_1.append(data_type_1_item)

            return data_type_1

        data = _parse_data(d.pop("data"))

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = KnexPaginatedDataGroupArrayOrGroupWithMembersArrayPagination.from_dict(_pagination)

        knex_paginated_data_group_array_or_group_with_members_array = cls(
            data=data,
            pagination=pagination,
        )

        knex_paginated_data_group_array_or_group_with_members_array.additional_properties = d
        return knex_paginated_data_group_array_or_group_with_members_array

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
