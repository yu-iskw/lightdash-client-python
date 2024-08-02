from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_group_list_response_status import ApiGroupListResponseStatus

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.group_with_members import GroupWithMembers


T = TypeVar("T", bound="ApiGroupListResponse")


@_attrs_define
class ApiGroupListResponse:
    """
    Attributes:
        results (Union[List['Group'], List['GroupWithMembers']]):
        status (ApiGroupListResponseStatus):
    """

    results: Union[List["Group"], List["GroupWithMembers"]]
    status: ApiGroupListResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: List[Dict[str, Any]]
        if isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = []
            for results_type_1_item_data in self.results:
                results_type_1_item = results_type_1_item_data.to_dict()
                results.append(results_type_1_item)

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

        def _parse_results(data: object) -> Union[List["Group"], List["GroupWithMembers"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = Group.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            results_type_1 = []
            _results_type_1 = data
            for results_type_1_item_data in _results_type_1:
                results_type_1_item = GroupWithMembers.from_dict(results_type_1_item_data)

                results_type_1.append(results_type_1_item)

            return results_type_1

        results = _parse_results(d.pop("results"))

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
