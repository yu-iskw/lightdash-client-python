from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scheduler_csv_options_limit_type_1 import SchedulerCsvOptionsLimitType1

T = TypeVar("T", bound="SchedulerCsvOptions")


@_attrs_define
class SchedulerCsvOptions:
    """
    Attributes:
        limit (Union[SchedulerCsvOptionsLimitType1, float]):
        formatted (bool):
    """

    limit: Union[SchedulerCsvOptionsLimitType1, float]
    formatted: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit: Union[float, str]
        if isinstance(self.limit, SchedulerCsvOptionsLimitType1):
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

        def _parse_limit(data: object) -> Union[SchedulerCsvOptionsLimitType1, float]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                limit_type_1 = SchedulerCsvOptionsLimitType1(data)

                return limit_type_1
            except:  # noqa: E722
                pass
            return cast(Union[SchedulerCsvOptionsLimitType1, float], data)

        limit = _parse_limit(d.pop("limit"))

        formatted = d.pop("formatted")

        scheduler_csv_options = cls(
            limit=limit,
            formatted=formatted,
        )

        scheduler_csv_options.additional_properties = d
        return scheduler_csv_options

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
