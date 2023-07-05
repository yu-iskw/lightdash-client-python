from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.api_scheduler_and_targets_response_results_targets_item_type_0 import (
        ApiSchedulerAndTargetsResponseResultsTargetsItemType0,
    )
    from ..models.api_scheduler_and_targets_response_results_targets_item_type_1 import (
        ApiSchedulerAndTargetsResponseResultsTargetsItemType1,
    )


T = TypeVar("T", bound="ApiSchedulerAndTargetsResponseResults")


@attr.s(auto_attribs=True)
class ApiSchedulerAndTargetsResponseResults:
    """
    Attributes:
        targets (List[Union['ApiSchedulerAndTargetsResponseResultsTargetsItemType0',
            'ApiSchedulerAndTargetsResponseResultsTargetsItemType1']]):
    """

    targets: List[
        Union[
            "ApiSchedulerAndTargetsResponseResultsTargetsItemType0",
            "ApiSchedulerAndTargetsResponseResultsTargetsItemType1",
        ]
    ]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_scheduler_and_targets_response_results_targets_item_type_0 import (
            ApiSchedulerAndTargetsResponseResultsTargetsItemType0,
        )

        targets = []
        for targets_item_data in self.targets:
            targets_item: Dict[str, Any]

            if isinstance(targets_item_data, ApiSchedulerAndTargetsResponseResultsTargetsItemType0):
                targets_item = targets_item_data.to_dict()

            else:
                targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_scheduler_and_targets_response_results_targets_item_type_0 import (
            ApiSchedulerAndTargetsResponseResultsTargetsItemType0,
        )
        from ..models.api_scheduler_and_targets_response_results_targets_item_type_1 import (
            ApiSchedulerAndTargetsResponseResultsTargetsItemType1,
        )

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:

            def _parse_targets_item(
                data: object,
            ) -> Union[
                "ApiSchedulerAndTargetsResponseResultsTargetsItemType0",
                "ApiSchedulerAndTargetsResponseResultsTargetsItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_0 = ApiSchedulerAndTargetsResponseResultsTargetsItemType0.from_dict(data)

                    return targets_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                targets_item_type_1 = ApiSchedulerAndTargetsResponseResultsTargetsItemType1.from_dict(data)

                return targets_item_type_1

            targets_item = _parse_targets_item(targets_item_data)

            targets.append(targets_item)

        api_scheduler_and_targets_response_results = cls(
            targets=targets,
        )

        api_scheduler_and_targets_response_results.additional_properties = d
        return api_scheduler_and_targets_response_results

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
