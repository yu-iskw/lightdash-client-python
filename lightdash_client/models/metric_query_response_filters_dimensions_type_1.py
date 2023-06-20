from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="MetricQueryResponseFiltersDimensionsType1")


@attr.s(auto_attribs=True)
class MetricQueryResponseFiltersDimensionsType1:
    """
    Attributes:
        and_ (List[Any]):
        id (str):
    """

    and_: List[Any]
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        and_ = self.and_

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "and": and_,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        and_ = cast(List[Any], d.pop("and"))

        id = d.pop("id")

        metric_query_response_filters_dimensions_type_1 = cls(
            and_=and_,
            id=id,
        )

        metric_query_response_filters_dimensions_type_1.additional_properties = d
        return metric_query_response_filters_dimensions_type_1

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
