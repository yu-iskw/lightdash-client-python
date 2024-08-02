from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMetadata")


@_attrs_define
class UpdateMetadata:
    """
    Attributes:
        upstream_project_uuid (Union[None, Unset, str]):
    """

    upstream_project_uuid: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upstream_project_uuid: Union[None, Unset, str]
        if isinstance(self.upstream_project_uuid, Unset):
            upstream_project_uuid = UNSET
        else:
            upstream_project_uuid = self.upstream_project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upstream_project_uuid is not UNSET:
            field_dict["upstreamProjectUuid"] = upstream_project_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_upstream_project_uuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        upstream_project_uuid = _parse_upstream_project_uuid(d.pop("upstreamProjectUuid", UNSET))

        update_metadata = cls(
            upstream_project_uuid=upstream_project_uuid,
        )

        update_metadata.additional_properties = d
        return update_metadata

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
