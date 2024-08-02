from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_target import ValidationTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateProjectBody")


@_attrs_define
class ValidateProjectBody:
    """the compiled explores to validate against an existing project, this is used in the CLI to validate a project without
    creating a preview

        Attributes:
            validation_targets (Union[Unset, List[ValidationTarget]]):
            explores (Union[Unset, List[Any]]):
    """

    validation_targets: Union[Unset, List[ValidationTarget]] = UNSET
    explores: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validation_targets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.validation_targets, Unset):
            validation_targets = []
            for validation_targets_item_data in self.validation_targets:
                validation_targets_item = validation_targets_item_data.value
                validation_targets.append(validation_targets_item)

        explores: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.explores, Unset):
            explores = self.explores

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validation_targets is not UNSET:
            field_dict["validationTargets"] = validation_targets
        if explores is not UNSET:
            field_dict["explores"] = explores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        validation_targets = []
        _validation_targets = d.pop("validationTargets", UNSET)
        for validation_targets_item_data in _validation_targets or []:
            validation_targets_item = ValidationTarget(validation_targets_item_data)

            validation_targets.append(validation_targets_item)

        explores = cast(List[Any], d.pop("explores", UNSET))

        validate_project_body = cls(
            validation_targets=validation_targets,
            explores=explores,
        )

        validate_project_body.additional_properties = d
        return validate_project_body

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
