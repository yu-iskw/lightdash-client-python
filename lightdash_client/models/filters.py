from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.filter_group_response_type_0 import FilterGroupResponseType0
    from ..models.filter_group_response_type_1 import FilterGroupResponseType1


T = TypeVar("T", bound="Filters")


@attr.s(auto_attribs=True)
class Filters:
    """
    Attributes:
        metrics (Union['FilterGroupResponseType0', 'FilterGroupResponseType1', Unset]):
        dimensions (Union['FilterGroupResponseType0', 'FilterGroupResponseType1', Unset]):
    """

    metrics: Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset] = UNSET
    dimensions: Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.filter_group_response_type_0 import FilterGroupResponseType0

        metrics: Union[Dict[str, Any], Unset]
        if isinstance(self.metrics, Unset):
            metrics = UNSET

        elif isinstance(self.metrics, FilterGroupResponseType0):
            metrics = self.metrics.to_dict()

        else:
            metrics = self.metrics.to_dict()

        dimensions: Union[Dict[str, Any], Unset]
        if isinstance(self.dimensions, Unset):
            dimensions = UNSET

        elif isinstance(self.dimensions, FilterGroupResponseType0):
            dimensions = self.dimensions.to_dict()

        else:
            dimensions = self.dimensions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_group_response_type_0 import FilterGroupResponseType0
        from ..models.filter_group_response_type_1 import FilterGroupResponseType1

        d = src_dict.copy()

        def _parse_metrics(data: object) -> Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_response_type_0 = FilterGroupResponseType0.from_dict(data)

                return componentsschemas_filter_group_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_response_type_1 = FilterGroupResponseType1.from_dict(data)

            return componentsschemas_filter_group_response_type_1

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_dimensions(data: object) -> Union["FilterGroupResponseType0", "FilterGroupResponseType1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_filter_group_response_type_0 = FilterGroupResponseType0.from_dict(data)

                return componentsschemas_filter_group_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_filter_group_response_type_1 = FilterGroupResponseType1.from_dict(data)

            return componentsschemas_filter_group_response_type_1

        dimensions = _parse_dimensions(d.pop("dimensions", UNSET))

        filters = cls(
            metrics=metrics,
            dimensions=dimensions,
        )

        filters.additional_properties = d
        return filters

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
