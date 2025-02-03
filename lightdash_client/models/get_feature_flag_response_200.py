from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_feature_flag_response_200_status import GetFeatureFlagResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_flag import FeatureFlag


T = TypeVar("T", bound="GetFeatureFlagResponse200")


@_attrs_define
class GetFeatureFlagResponse200:
    """
    Attributes:
        results (FeatureFlag):
        status (GetFeatureFlagResponse200Status):
    """

    results: "FeatureFlag"
    status: GetFeatureFlagResponse200Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.feature_flag import FeatureFlag

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
        from ..models.feature_flag import FeatureFlag

        d = src_dict.copy()
        results = FeatureFlag.from_dict(d.pop("results"))

        status = GetFeatureFlagResponse200Status(d.pop("status"))

        get_feature_flag_response_200 = cls(
            results=results,
            status=status,
        )

        get_feature_flag_response_200.additional_properties = d
        return get_feature_flag_response_200

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
