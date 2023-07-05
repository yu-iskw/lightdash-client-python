from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.get_scheduler_logs_response_200_results_schedulers_item_targets_item_type_0 import (
        GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0,
    )
    from ..models.get_scheduler_logs_response_200_results_schedulers_item_targets_item_type_1 import (
        GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1,
    )


T = TypeVar("T", bound="GetSchedulerLogsResponse200ResultsSchedulersItem")


@attr.s(auto_attribs=True)
class GetSchedulerLogsResponse200ResultsSchedulersItem:
    """
    Attributes:
        targets (List[Union['GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0',
            'GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1']]):
    """

    targets: List[
        Union[
            "GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0",
            "GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1",
        ]
    ]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_scheduler_logs_response_200_results_schedulers_item_targets_item_type_0 import (
            GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0,
        )

        targets = []
        for targets_item_data in self.targets:
            targets_item: Dict[str, Any]

            if isinstance(targets_item_data, GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0):
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
        from ..models.get_scheduler_logs_response_200_results_schedulers_item_targets_item_type_0 import (
            GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0,
        )
        from ..models.get_scheduler_logs_response_200_results_schedulers_item_targets_item_type_1 import (
            GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1,
        )

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:

            def _parse_targets_item(
                data: object,
            ) -> Union[
                "GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0",
                "GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_0 = GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType0.from_dict(
                        data
                    )

                    return targets_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                targets_item_type_1 = GetSchedulerLogsResponse200ResultsSchedulersItemTargetsItemType1.from_dict(data)

                return targets_item_type_1

            targets_item = _parse_targets_item(targets_item_data)

            targets.append(targets_item)

        get_scheduler_logs_response_200_results_schedulers_item = cls(
            targets=targets,
        )

        get_scheduler_logs_response_200_results_schedulers_item.additional_properties = d
        return get_scheduler_logs_response_200_results_schedulers_item

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
