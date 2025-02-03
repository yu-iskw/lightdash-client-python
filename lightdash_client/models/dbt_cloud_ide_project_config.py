from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dbt_project_type_dbtcloudide import DbtProjectTypeDBTCLOUDIDE
from ..types import UNSET, Unset

T = TypeVar("T", bound="DbtCloudIDEProjectConfig")


@_attrs_define
class DbtCloudIDEProjectConfig:
    """
    Attributes:
        type (DbtProjectTypeDBTCLOUDIDE):
        api_key (str):
        environment_id (str):
        discovery_api_endpoint (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
    """

    type: DbtProjectTypeDBTCLOUDIDE
    api_key: str
    environment_id: str
    discovery_api_endpoint: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        api_key = self.api_key

        environment_id = self.environment_id

        discovery_api_endpoint = self.discovery_api_endpoint

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "api_key": api_key,
                "environment_id": environment_id,
            }
        )
        if discovery_api_endpoint is not UNSET:
            field_dict["discovery_api_endpoint"] = discovery_api_endpoint
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = DbtProjectTypeDBTCLOUDIDE(d.pop("type"))

        api_key = d.pop("api_key")

        environment_id = d.pop("environment_id")

        discovery_api_endpoint = d.pop("discovery_api_endpoint", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        dbt_cloud_ide_project_config = cls(
            type=type,
            api_key=api_key,
            environment_id=environment_id,
            discovery_api_endpoint=discovery_api_endpoint,
            tags=tags,
        )

        dbt_cloud_ide_project_config.additional_properties = d
        return dbt_cloud_ide_project_config

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
