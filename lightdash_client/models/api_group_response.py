from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_group_response_status import ApiGroupResponseStatus

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.group_with_members import GroupWithMembers


T = TypeVar("T", bound="ApiGroupResponse")


@_attrs_define
class ApiGroupResponse:
    """
    Attributes:
        results (Union['Group', 'GroupWithMembers']):
        status (ApiGroupResponseStatus):
    """

    results: Union["Group", "GroupWithMembers"]
    status: ApiGroupResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group import Group

        results: Dict[str, Any]
        if isinstance(self.results, Group):
            results = self.results.to_dict()
        else:
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
        from ..models.group import Group
        from ..models.group_with_members import GroupWithMembers

        d = src_dict.copy()

        def _parse_results(data: object) -> Union["Group", "GroupWithMembers"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                results_type_0 = Group.from_dict(data)

                return results_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            results_type_1 = GroupWithMembers.from_dict(data)

            return results_type_1

        results = _parse_results(d.pop("results"))

        status = ApiGroupResponseStatus(d.pop("status"))

        api_group_response = cls(
            results=results,
            status=status,
        )

        api_group_response.additional_properties = d
        return api_group_response

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
