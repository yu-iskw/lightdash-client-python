from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

if TYPE_CHECKING:
    from ..models.scheduler_and_targets_targets_item_type_0 import SchedulerAndTargetsTargetsItemType0
    from ..models.scheduler_and_targets_targets_item_type_1 import SchedulerAndTargetsTargetsItemType1


T = TypeVar("T", bound="SchedulerAndTargets")


@attr.s(auto_attribs=True)
class SchedulerAndTargets:
    """
    Attributes:
        targets (List[Union['SchedulerAndTargetsTargetsItemType0', 'SchedulerAndTargetsTargetsItemType1']]):
    """

    targets: List[Union["SchedulerAndTargetsTargetsItemType0", "SchedulerAndTargetsTargetsItemType1"]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.scheduler_and_targets_targets_item_type_0 import SchedulerAndTargetsTargetsItemType0

        targets = []
        for targets_item_data in self.targets:
            targets_item: Dict[str, Any]

            if isinstance(targets_item_data, SchedulerAndTargetsTargetsItemType0):
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
        from ..models.scheduler_and_targets_targets_item_type_0 import SchedulerAndTargetsTargetsItemType0
        from ..models.scheduler_and_targets_targets_item_type_1 import SchedulerAndTargetsTargetsItemType1

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:

            def _parse_targets_item(
                data: object,
            ) -> Union["SchedulerAndTargetsTargetsItemType0", "SchedulerAndTargetsTargetsItemType1"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    targets_item_type_0 = SchedulerAndTargetsTargetsItemType0.from_dict(data)

                    return targets_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                targets_item_type_1 = SchedulerAndTargetsTargetsItemType1.from_dict(data)

                return targets_item_type_1

            targets_item = _parse_targets_item(targets_item_data)

            targets.append(targets_item)

        scheduler_and_targets = cls(
            targets=targets,
        )

        scheduler_and_targets.additional_properties = d
        return scheduler_and_targets

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
