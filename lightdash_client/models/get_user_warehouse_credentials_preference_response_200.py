from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_user_warehouse_credentials_preference_response_200_status import (
    GetUserWarehouseCredentialsPreferenceResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_warehouse_credentials import UserWarehouseCredentials


T = TypeVar("T", bound="GetUserWarehouseCredentialsPreferenceResponse200")


@_attrs_define
class GetUserWarehouseCredentialsPreferenceResponse200:
    """
    Attributes:
        status (GetUserWarehouseCredentialsPreferenceResponse200Status):
        results (Union[Unset, UserWarehouseCredentials]):
    """

    status: GetUserWarehouseCredentialsPreferenceResponse200Status
    results: Union[Unset, "UserWarehouseCredentials"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_warehouse_credentials import UserWarehouseCredentials

        d = src_dict.copy()
        status = GetUserWarehouseCredentialsPreferenceResponse200Status(d.pop("status"))

        _results = d.pop("results", UNSET)
        results: Union[Unset, UserWarehouseCredentials]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = UserWarehouseCredentials.from_dict(_results)

        get_user_warehouse_credentials_preference_response_200 = cls(
            status=status,
            results=results,
        )

        get_user_warehouse_credentials_preference_response_200.additional_properties = d
        return get_user_warehouse_credentials_preference_response_200

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
