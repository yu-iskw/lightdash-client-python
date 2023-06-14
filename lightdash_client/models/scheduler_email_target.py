import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="SchedulerEmailTarget")


@attr.s(auto_attribs=True)
class SchedulerEmailTarget:
    """
    Attributes:
        recipient (str):
        scheduler_uuid (str):
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        scheduler_email_target_uuid (str):
    """

    recipient: str
    scheduler_uuid: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
    scheduler_email_target_uuid: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recipient = self.recipient
        scheduler_uuid = self.scheduler_uuid
        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        scheduler_email_target_uuid = self.scheduler_email_target_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipient": recipient,
                "schedulerUuid": scheduler_uuid,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "schedulerEmailTargetUuid": scheduler_email_target_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recipient = d.pop("recipient")

        scheduler_uuid = d.pop("schedulerUuid")

        updated_at = isoparse(d.pop("updatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        scheduler_email_target_uuid = d.pop("schedulerEmailTargetUuid")

        scheduler_email_target = cls(
            recipient=recipient,
            scheduler_uuid=scheduler_uuid,
            updated_at=updated_at,
            created_at=created_at,
            scheduler_email_target_uuid=scheduler_email_target_uuid,
        )

        scheduler_email_target.additional_properties = d
        return scheduler_email_target

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
