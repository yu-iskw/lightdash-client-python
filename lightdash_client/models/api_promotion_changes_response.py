from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_promotion_changes_response_status import (
    ApiPromotionChangesResponseStatus,
)

if TYPE_CHECKING:
    from ..models.promotion_changes import PromotionChanges


T = TypeVar("T", bound="ApiPromotionChangesResponse")


@_attrs_define
class ApiPromotionChangesResponse:
    """
    Attributes:
        results (PromotionChanges):
        status (ApiPromotionChangesResponseStatus):
    """

    results: "PromotionChanges"
    status: ApiPromotionChangesResponseStatus
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
        from ..models.promotion_changes import PromotionChanges

        d = src_dict.copy()
        results = PromotionChanges.from_dict(d.pop("results"))

        status = ApiPromotionChangesResponseStatus(d.pop("status"))

        api_promotion_changes_response = cls(
            results=results,
            status=status,
        )

        api_promotion_changes_response.additional_properties = d
        return api_promotion_changes_response

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
