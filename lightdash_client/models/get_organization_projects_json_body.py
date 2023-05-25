from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="GetOrganizationProjectsJsonBody")


@attr.s(auto_attribs=True)
class GetOrganizationProjectsJsonBody:
    """
    Attributes:
        role (Union[Unset, str]):
    """

    role: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = d.pop("role", UNSET)

        get_organization_projects_json_body = cls(
            role=role,
        )

        return get_organization_projects_json_body
