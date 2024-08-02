from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_type import ProjectType
from ..models.warehouse_types import WarehouseTypes

T = TypeVar("T", bound="OrganizationProject")


@_attrs_define
class OrganizationProject:
    """Summary of a project under an organization

    Attributes:
        require_user_credentials (bool):
        warehouse_type (WarehouseTypes):
        type (ProjectType):
        name (str):
        project_uuid (str): The unique identifier of the project
    """

    require_user_credentials: bool
    warehouse_type: WarehouseTypes
    type: ProjectType
    name: str
    project_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        require_user_credentials = self.require_user_credentials

        warehouse_type = self.warehouse_type.value

        type = self.type.value

        name = self.name

        project_uuid = self.project_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requireUserCredentials": require_user_credentials,
                "warehouseType": warehouse_type,
                "type": type,
                "name": name,
                "projectUuid": project_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        require_user_credentials = d.pop("requireUserCredentials")

        warehouse_type = WarehouseTypes(d.pop("warehouseType"))

        type = ProjectType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_project = cls(
            require_user_credentials=require_user_credentials,
            warehouse_type=warehouse_type,
            type=type,
            name=name,
            project_uuid=project_uuid,
        )

        organization_project.additional_properties = d
        return organization_project

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
