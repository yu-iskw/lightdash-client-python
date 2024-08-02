from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_explore_response_200_status import GetExploreResponse200Status

if TYPE_CHECKING:
    from ..models.explore import Explore


T = TypeVar("T", bound="GetExploreResponse200")


@_attrs_define
class GetExploreResponse200:
    """
    Attributes:
        results (Explore):
        status (GetExploreResponse200Status):
    """

    results: "Explore"
    status: GetExploreResponse200Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        from ..models.explore import Explore

        d = src_dict.copy()
        results = Explore.from_dict(d.pop("results"))

        status = GetExploreResponse200Status(d.pop("status"))

        get_explore_response_200 = cls(
            results=results,
            status=status,
        )

        get_explore_response_200.additional_properties = d
        return get_explore_response_200

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
