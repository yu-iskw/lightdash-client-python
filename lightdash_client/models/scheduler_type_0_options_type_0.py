from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.scheduler_type_0_options_type_0_limit_type_1 import SchedulerType0OptionsType0LimitType1

T = TypeVar("T", bound="SchedulerType0OptionsType0")


@attr.s(auto_attribs=True)
class SchedulerType0OptionsType0:
    """
    Attributes:
        limit (Union[SchedulerType0OptionsType0LimitType1, float]):
        formatted (bool):
    """

    limit: Union[SchedulerType0OptionsType0LimitType1, float]
    formatted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit: Union[float, str]

        if isinstance(self.limit, SchedulerType0OptionsType0LimitType1):
            limit = self.limit.value

        else:
            limit = self.limit

        formatted = self.formatted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "formatted": formatted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_limit(data: object) -> Union[SchedulerType0OptionsType0LimitType1, float]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_type_1 = SchedulerType0OptionsType0LimitType1(data)

                return limit_type_1
            except:  # noqa: E722
                pass
            return cast(Union[SchedulerType0OptionsType0LimitType1, float], data)

        limit = _parse_limit(d.pop("limit"))

        formatted = d.pop("formatted")

        scheduler_type_0_options_type_0 = cls(
            limit=limit,
            formatted=formatted,
        )

        scheduler_type_0_options_type_0.additional_properties = d
        return scheduler_type_0_options_type_0

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
