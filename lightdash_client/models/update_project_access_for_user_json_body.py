from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

from ..models.update_project_access_for_user_json_body_role import UpdateProjectAccessForUserJsonBodyRole

T = TypeVar("T", bound="UpdateProjectAccessForUserJsonBody")


@attr.s(auto_attribs=True)
class UpdateProjectAccessForUserJsonBody:
    """
    Attributes:
        role (UpdateProjectAccessForUserJsonBodyRole):
    """

    role: UpdateProjectAccessForUserJsonBodyRole
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = UpdateProjectAccessForUserJsonBodyRole(d.pop("role"))

        update_project_access_for_user_json_body = cls(
            role=role,
        )

        update_project_access_for_user_json_body.additional_properties = d
        return update_project_access_for_user_json_body

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
