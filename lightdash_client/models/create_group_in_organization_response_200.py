from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.create_group_in_organization_response_200_status import (
    CreateGroupInOrganizationResponse200Status,
)

if TYPE_CHECKING:
    from ..models.create_group_in_organization_response_200_results import (
        CreateGroupInOrganizationResponse200Results,
    )


T = TypeVar("T", bound="CreateGroupInOrganizationResponse200")


@attr.s(auto_attribs=True)
class CreateGroupInOrganizationResponse200:
    """
    Attributes:
        results (CreateGroupInOrganizationResponse200Results):
        status (CreateGroupInOrganizationResponse200Status):
    """

    results: "CreateGroupInOrganizationResponse200Results"
    status: CreateGroupInOrganizationResponse200Status
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
        from ..models.create_group_in_organization_response_200_results import (
            CreateGroupInOrganizationResponse200Results,
        )

        d = src_dict.copy()
        results = CreateGroupInOrganizationResponse200Results.from_dict(d.pop("results"))

        status = CreateGroupInOrganizationResponse200Status(d.pop("status"))

        create_group_in_organization_response_200 = cls(
            results=results,
            status=status,
        )

        create_group_in_organization_response_200.additional_properties = d
        return create_group_in_organization_response_200

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
