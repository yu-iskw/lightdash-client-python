from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.create_ssh_key_pair_response_201_status import (
    CreateSshKeyPairResponse201Status,
)

if TYPE_CHECKING:
    from ..models.create_ssh_key_pair_response_201_results import (
        CreateSshKeyPairResponse201Results,
    )


T = TypeVar("T", bound="CreateSshKeyPairResponse201")


@attr.s(auto_attribs=True)
class CreateSshKeyPairResponse201:
    """
    Attributes:
        results (CreateSshKeyPairResponse201Results): From T, pick a set of properties whose keys are in the union K
        status (CreateSshKeyPairResponse201Status):
    """

    results: "CreateSshKeyPairResponse201Results"
    status: CreateSshKeyPairResponse201Status
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        from ..models.create_ssh_key_pair_response_201_results import (
            CreateSshKeyPairResponse201Results,
        )

        d = src_dict.copy()
        results = CreateSshKeyPairResponse201Results.from_dict(d.pop("results"))

        status = CreateSshKeyPairResponse201Status(d.pop("status"))

        create_ssh_key_pair_response_201 = cls(
            results=results,
            status=status,
        )

        create_ssh_key_pair_response_201.additional_properties = d
        return create_ssh_key_pair_response_201

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
