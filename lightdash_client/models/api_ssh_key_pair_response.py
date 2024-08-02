from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_ssh_key_pair_response_status import ApiSshKeyPairResponseStatus

if TYPE_CHECKING:
    from ..models.pick_ssh_key_pair_public_key import PickSshKeyPairPublicKey


T = TypeVar("T", bound="ApiSshKeyPairResponse")


@_attrs_define
class ApiSshKeyPairResponse:
    """
    Attributes:
        results (PickSshKeyPairPublicKey): From T, pick a set of properties whose keys are in the union K
        status (ApiSshKeyPairResponseStatus):
    """

    results: "PickSshKeyPairPublicKey"
    status: ApiSshKeyPairResponseStatus
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
        from ..models.pick_ssh_key_pair_public_key import PickSshKeyPairPublicKey

        d = src_dict.copy()
        results = PickSshKeyPairPublicKey.from_dict(d.pop("results"))

        status = ApiSshKeyPairResponseStatus(d.pop("status"))

        api_ssh_key_pair_response = cls(
            results=results,
            status=status,
        )

        api_ssh_key_pair_response.additional_properties = d
        return api_ssh_key_pair_response

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
