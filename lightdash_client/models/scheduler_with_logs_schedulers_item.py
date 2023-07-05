from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.scheduler_with_logs_schedulers_item_targets_item_type_0 import (
        SchedulerWithLogsSchedulersItemTargetsItemType0,
    )
    from ..models.scheduler_with_logs_schedulers_item_targets_item_type_1 import (
        SchedulerWithLogsSchedulersItemTargetsItemType1,
    )


T = TypeVar("T", bound="SchedulerWithLogsSchedulersItem")


@attr.s(auto_attribs=True)
class SchedulerWithLogsSchedulersItem:
    """
    Attributes:
        targets (List[Union['SchedulerWithLogsSchedulersItemTargetsItemType0',
            'SchedulerWithLogsSchedulersItemTargetsItemType1']]):
    """

    targets: List[
        Union["SchedulerWithLogsSchedulersItemTargetsItemType0", "SchedulerWithLogsSchedulersItemTargetsItemType1"]
    ]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scheduler_with_logs_schedulers_item_targets_item_type_0 import (
            SchedulerWithLogsSchedulersItemTargetsItemType0,
        )

        targets = []
        for targets_item_data in self.targets:
            targets_item: Dict[str, Any]

            if isinstance(targets_item_data, SchedulerWithLogsSchedulersItemTargetsItemType0):
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
        from ..models.scheduler_with_logs_schedulers_item_targets_item_type_0 import (
            SchedulerWithLogsSchedulersItemTargetsItemType0,
        )
        from ..models.scheduler_with_logs_schedulers_item_targets_item_type_1 import (
            SchedulerWithLogsSchedulersItemTargetsItemType1,
        )

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:

            def _parse_targets_item(
                data: object,
            ) -> Union[
                "SchedulerWithLogsSchedulersItemTargetsItemType0", "SchedulerWithLogsSchedulersItemTargetsItemType1"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_0 = SchedulerWithLogsSchedulersItemTargetsItemType0.from_dict(data)

                    return targets_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                targets_item_type_1 = SchedulerWithLogsSchedulersItemTargetsItemType1.from_dict(data)

                return targets_item_type_1

            targets_item = _parse_targets_item(targets_item_data)

            targets.append(targets_item)

        scheduler_with_logs_schedulers_item = cls(
            targets=targets,
        )

        scheduler_with_logs_schedulers_item.additional_properties = d
        return scheduler_with_logs_schedulers_item

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
