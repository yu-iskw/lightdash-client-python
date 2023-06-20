from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar

import attr

from ..models.update_organization_email_domains_response_200_status import (
    UpdateOrganizationEmailDomainsResponse200Status,
)

if TYPE_CHECKING:
    from ..models.update_organization_email_domains_response_200_results import (
        UpdateOrganizationEmailDomainsResponse200Results,
    )


T = TypeVar("T", bound="UpdateOrganizationEmailDomainsResponse200")


@attr.s(auto_attribs=True)
class UpdateOrganizationEmailDomainsResponse200:
    """
    Attributes:
        results (UpdateOrganizationEmailDomainsResponse200Results):
        status (UpdateOrganizationEmailDomainsResponse200Status):
    """

    results: "UpdateOrganizationEmailDomainsResponse200Results"
    status: UpdateOrganizationEmailDomainsResponse200Status
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
        from ..models.update_organization_email_domains_response_200_results import (
            UpdateOrganizationEmailDomainsResponse200Results,
        )

        d = src_dict.copy()
        results = UpdateOrganizationEmailDomainsResponse200Results.from_dict(d.pop("results"))

        status = UpdateOrganizationEmailDomainsResponse200Status(d.pop("status"))

        update_organization_email_domains_response_200 = cls(
            results=results,
            status=status,
        )

        update_organization_email_domains_response_200.additional_properties = d
        return update_organization_email_domains_response_200

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