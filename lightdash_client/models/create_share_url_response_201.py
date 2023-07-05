from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.create_share_url_response_201_status import (
    CreateShareUrlResponse201Status,
)

if TYPE_CHECKING:
    from ..models.create_share_url_response_201_results import (
        CreateShareUrlResponse201Results,
    )


T = TypeVar("T", bound="CreateShareUrlResponse201")


@attr.s(auto_attribs=True)
class CreateShareUrlResponse201:
    """
    Attributes:
        results (CreateShareUrlResponse201Results): A ShareUrl maps a short shareable id to a full URL
            in the Lightdash UI. This allows very long URLs
            to be represented by short ids.
        status (CreateShareUrlResponse201Status):
    """

    results: "CreateShareUrlResponse201Results"
    status: CreateShareUrlResponse201Status
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
        from ..models.create_share_url_response_201_results import (
            CreateShareUrlResponse201Results,
        )

        d = src_dict.copy()
        results = CreateShareUrlResponse201Results.from_dict(d.pop("results"))

        status = CreateShareUrlResponse201Status(d.pop("status"))

        create_share_url_response_201 = cls(
            results=results,
            status=status,
        )

        create_share_url_response_201.additional_properties = d
        return create_share_url_response_201

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
