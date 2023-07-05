from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.update_scheduler_response_201_status import (
    UpdateSchedulerResponse201Status,
)

if TYPE_CHECKING:
    from ..models.update_scheduler_response_201_results import (
        UpdateSchedulerResponse201Results,
    )


T = TypeVar("T", bound="UpdateSchedulerResponse201")


@attr.s(auto_attribs=True)
class UpdateSchedulerResponse201:
    """
    Attributes:
        results (UpdateSchedulerResponse201Results):
        status (UpdateSchedulerResponse201Status):
    """

    results: "UpdateSchedulerResponse201Results"
    status: UpdateSchedulerResponse201Status
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
        from ..models.update_scheduler_response_201_results import (
            UpdateSchedulerResponse201Results,
        )

        d = src_dict.copy()
        results = UpdateSchedulerResponse201Results.from_dict(d.pop("results"))

        status = UpdateSchedulerResponse201Status(d.pop("status"))

        update_scheduler_response_201 = cls(
            results=results,
            status=status,
        )

        update_scheduler_response_201.additional_properties = d
        return update_scheduler_response_201

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
