from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.api_share_response_status import ApiShareResponseStatus

if TYPE_CHECKING:
    from ..models.api_share_response_results import ApiShareResponseResults


T = TypeVar("T", bound="ApiShareResponse")


@attr.s(auto_attribs=True)
class ApiShareResponse:
    """
    Attributes:
        results (ApiShareResponseResults): A ShareUrl maps a short shareable id to a full URL
            in the Lightdash UI. This allows very long URLs
            to be represented by short ids.
        status (ApiShareResponseStatus):
    """

    results: "ApiShareResponseResults"
    status: ApiShareResponseStatus
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
        from ..models.api_share_response_results import ApiShareResponseResults

        d = src_dict.copy()
        results = ApiShareResponseResults.from_dict(d.pop("results"))

        status = ApiShareResponseStatus(d.pop("status"))

        api_share_response = cls(
            results=results,
            status=status,
        )

        api_share_response.additional_properties = d
        return api_share_response

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
