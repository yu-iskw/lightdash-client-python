from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PickSshKeyPairPublicKey")


@_attrs_define
class PickSshKeyPairPublicKey:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        public_key (str):
    """

    public_key: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicKey": public_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        public_key = d.pop("publicKey")

        pick_ssh_key_pair_public_key = cls(
            public_key=public_key,
        )

        pick_ssh_key_pair_public_key.additional_properties = d
        return pick_ssh_key_pair_public_key

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
