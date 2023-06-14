from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="ValidateProjectJsonBody")


@attr.s(auto_attribs=True)
class ValidateProjectJsonBody:
    """the compiled explores to validate against an existing project, this is used in the CLI to validate a project without
    creating a preview

        Attributes:
            explores (Union[Unset, List[Any]]):
    """

    explores: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        explores: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.explores, Unset):
            explores = self.explores

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if explores is not UNSET:
            field_dict["explores"] = explores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        explores = cast(List[Any], d.pop("explores", UNSET))

        validate_project_json_body = cls(
            explores=explores,
        )

        validate_project_json_body.additional_properties = d
        return validate_project_json_body

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
