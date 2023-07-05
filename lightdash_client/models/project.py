from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_type import ProjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_dbt_connection_type_0 import ProjectDbtConnectionType0
    from ..models.project_dbt_connection_type_1 import ProjectDbtConnectionType1
    from ..models.project_dbt_connection_type_2 import ProjectDbtConnectionType2
    from ..models.project_dbt_connection_type_3 import ProjectDbtConnectionType3
    from ..models.project_dbt_connection_type_4 import ProjectDbtConnectionType4
    from ..models.project_dbt_connection_type_5 import ProjectDbtConnectionType5
    from ..models.project_dbt_connection_type_6 import ProjectDbtConnectionType6
    from ..models.project_warehouse_connection_type_0 import (
        ProjectWarehouseConnectionType0,
    )
    from ..models.project_warehouse_connection_type_1 import (
        ProjectWarehouseConnectionType1,
    )
    from ..models.project_warehouse_connection_type_2 import (
        ProjectWarehouseConnectionType2,
    )
    from ..models.project_warehouse_connection_type_3 import (
        ProjectWarehouseConnectionType3,
    )
    from ..models.project_warehouse_connection_type_4 import (
        ProjectWarehouseConnectionType4,
    )
    from ..models.project_warehouse_connection_type_5 import (
        ProjectWarehouseConnectionType5,
    )


T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """
    Attributes:
        dbt_connection (Union['ProjectDbtConnectionType0', 'ProjectDbtConnectionType1', 'ProjectDbtConnectionType2',
            'ProjectDbtConnectionType3', 'ProjectDbtConnectionType4', 'ProjectDbtConnectionType5',
            'ProjectDbtConnectionType6']):
        type (ProjectType):
        name (str):
        project_uuid (str):
        organization_uuid (str):
        copied_from_project_uuid (Union[Unset, str]):
        pinned_list_uuid (Union[Unset, str]):
        warehouse_connection (Union['ProjectWarehouseConnectionType0', 'ProjectWarehouseConnectionType1',
            'ProjectWarehouseConnectionType2', 'ProjectWarehouseConnectionType3', 'ProjectWarehouseConnectionType4',
            'ProjectWarehouseConnectionType5', Unset]):
    """

    dbt_connection: Union[
        "ProjectDbtConnectionType0",
        "ProjectDbtConnectionType1",
        "ProjectDbtConnectionType2",
        "ProjectDbtConnectionType3",
        "ProjectDbtConnectionType4",
        "ProjectDbtConnectionType5",
        "ProjectDbtConnectionType6",
    ]
    type: ProjectType
    name: str
    project_uuid: str
    organization_uuid: str
    copied_from_project_uuid: Union[Unset, str] = UNSET
    pinned_list_uuid: Union[Unset, str] = UNSET
    warehouse_connection: Union[
        "ProjectWarehouseConnectionType0",
        "ProjectWarehouseConnectionType1",
        "ProjectWarehouseConnectionType2",
        "ProjectWarehouseConnectionType3",
        "ProjectWarehouseConnectionType4",
        "ProjectWarehouseConnectionType5",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.project_dbt_connection_type_0 import ProjectDbtConnectionType0
        from ..models.project_dbt_connection_type_1 import ProjectDbtConnectionType1
        from ..models.project_dbt_connection_type_2 import ProjectDbtConnectionType2
        from ..models.project_dbt_connection_type_3 import ProjectDbtConnectionType3
        from ..models.project_dbt_connection_type_4 import ProjectDbtConnectionType4
        from ..models.project_dbt_connection_type_5 import ProjectDbtConnectionType5
        from ..models.project_warehouse_connection_type_0 import (
            ProjectWarehouseConnectionType0,
        )
        from ..models.project_warehouse_connection_type_1 import (
            ProjectWarehouseConnectionType1,
        )
        from ..models.project_warehouse_connection_type_2 import (
            ProjectWarehouseConnectionType2,
        )
        from ..models.project_warehouse_connection_type_3 import (
            ProjectWarehouseConnectionType3,
        )
        from ..models.project_warehouse_connection_type_4 import (
            ProjectWarehouseConnectionType4,
        )

        dbt_connection: Dict[str, Any]

        if isinstance(self.dbt_connection, ProjectDbtConnectionType0):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ProjectDbtConnectionType1):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ProjectDbtConnectionType2):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ProjectDbtConnectionType3):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ProjectDbtConnectionType4):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ProjectDbtConnectionType5):
            dbt_connection = self.dbt_connection.to_dict()

        else:
            dbt_connection = self.dbt_connection.to_dict()

        type = self.type.value

        name = self.name
        project_uuid = self.project_uuid
        organization_uuid = self.organization_uuid
        copied_from_project_uuid = self.copied_from_project_uuid
        pinned_list_uuid = self.pinned_list_uuid
        warehouse_connection: Union[Dict[str, Any], Unset]
        if isinstance(self.warehouse_connection, Unset):
            warehouse_connection = UNSET

        elif isinstance(self.warehouse_connection, ProjectWarehouseConnectionType0):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ProjectWarehouseConnectionType1):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ProjectWarehouseConnectionType2):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ProjectWarehouseConnectionType3):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ProjectWarehouseConnectionType4):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        else:
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbtConnection": dbt_connection,
                "type": type,
                "name": name,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
            }
        )
        if copied_from_project_uuid is not UNSET:
            field_dict["copiedFromProjectUuid"] = copied_from_project_uuid
        if pinned_list_uuid is not UNSET:
            field_dict["pinnedListUuid"] = pinned_list_uuid
        if warehouse_connection is not UNSET:
            field_dict["warehouseConnection"] = warehouse_connection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_dbt_connection_type_0 import ProjectDbtConnectionType0
        from ..models.project_dbt_connection_type_1 import ProjectDbtConnectionType1
        from ..models.project_dbt_connection_type_2 import ProjectDbtConnectionType2
        from ..models.project_dbt_connection_type_3 import ProjectDbtConnectionType3
        from ..models.project_dbt_connection_type_4 import ProjectDbtConnectionType4
        from ..models.project_dbt_connection_type_5 import ProjectDbtConnectionType5
        from ..models.project_dbt_connection_type_6 import ProjectDbtConnectionType6
        from ..models.project_warehouse_connection_type_0 import (
            ProjectWarehouseConnectionType0,
        )
        from ..models.project_warehouse_connection_type_1 import (
            ProjectWarehouseConnectionType1,
        )
        from ..models.project_warehouse_connection_type_2 import (
            ProjectWarehouseConnectionType2,
        )
        from ..models.project_warehouse_connection_type_3 import (
            ProjectWarehouseConnectionType3,
        )
        from ..models.project_warehouse_connection_type_4 import (
            ProjectWarehouseConnectionType4,
        )
        from ..models.project_warehouse_connection_type_5 import (
            ProjectWarehouseConnectionType5,
        )

        d = src_dict.copy()

        def _parse_dbt_connection(
            data: object,
        ) -> Union[
            "ProjectDbtConnectionType0",
            "ProjectDbtConnectionType1",
            "ProjectDbtConnectionType2",
            "ProjectDbtConnectionType3",
            "ProjectDbtConnectionType4",
            "ProjectDbtConnectionType5",
            "ProjectDbtConnectionType6",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_0 = ProjectDbtConnectionType0.from_dict(data)

                return dbt_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_1 = ProjectDbtConnectionType1.from_dict(data)

                return dbt_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_2 = ProjectDbtConnectionType2.from_dict(data)

                return dbt_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_3 = ProjectDbtConnectionType3.from_dict(data)

                return dbt_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_4 = ProjectDbtConnectionType4.from_dict(data)

                return dbt_connection_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_5 = ProjectDbtConnectionType5.from_dict(data)

                return dbt_connection_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            dbt_connection_type_6 = ProjectDbtConnectionType6.from_dict(data)

            return dbt_connection_type_6

        dbt_connection = _parse_dbt_connection(d.pop("dbtConnection"))

        type = ProjectType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        copied_from_project_uuid = d.pop("copiedFromProjectUuid", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid", UNSET)

        def _parse_warehouse_connection(
            data: object,
        ) -> Union[
            "ProjectWarehouseConnectionType0",
            "ProjectWarehouseConnectionType1",
            "ProjectWarehouseConnectionType2",
            "ProjectWarehouseConnectionType3",
            "ProjectWarehouseConnectionType4",
            "ProjectWarehouseConnectionType5",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_0 = data
                warehouse_connection_type_0: Union[Unset, ProjectWarehouseConnectionType0]
                if isinstance(_warehouse_connection_type_0, Unset):
                    warehouse_connection_type_0 = UNSET
                else:
                    warehouse_connection_type_0 = ProjectWarehouseConnectionType0.from_dict(
                        _warehouse_connection_type_0
                    )

                return warehouse_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_1 = data
                warehouse_connection_type_1: Union[Unset, ProjectWarehouseConnectionType1]
                if isinstance(_warehouse_connection_type_1, Unset):
                    warehouse_connection_type_1 = UNSET
                else:
                    warehouse_connection_type_1 = ProjectWarehouseConnectionType1.from_dict(
                        _warehouse_connection_type_1
                    )

                return warehouse_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_2 = data
                warehouse_connection_type_2: Union[Unset, ProjectWarehouseConnectionType2]
                if isinstance(_warehouse_connection_type_2, Unset):
                    warehouse_connection_type_2 = UNSET
                else:
                    warehouse_connection_type_2 = ProjectWarehouseConnectionType2.from_dict(
                        _warehouse_connection_type_2
                    )

                return warehouse_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_3 = data
                warehouse_connection_type_3: Union[Unset, ProjectWarehouseConnectionType3]
                if isinstance(_warehouse_connection_type_3, Unset):
                    warehouse_connection_type_3 = UNSET
                else:
                    warehouse_connection_type_3 = ProjectWarehouseConnectionType3.from_dict(
                        _warehouse_connection_type_3
                    )

                return warehouse_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_4 = data
                warehouse_connection_type_4: Union[Unset, ProjectWarehouseConnectionType4]
                if isinstance(_warehouse_connection_type_4, Unset):
                    warehouse_connection_type_4 = UNSET
                else:
                    warehouse_connection_type_4 = ProjectWarehouseConnectionType4.from_dict(
                        _warehouse_connection_type_4
                    )

                return warehouse_connection_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _warehouse_connection_type_5 = data
            warehouse_connection_type_5: Union[Unset, ProjectWarehouseConnectionType5]
            if isinstance(_warehouse_connection_type_5, Unset):
                warehouse_connection_type_5 = UNSET
            else:
                warehouse_connection_type_5 = ProjectWarehouseConnectionType5.from_dict(_warehouse_connection_type_5)

            return warehouse_connection_type_5

        warehouse_connection = _parse_warehouse_connection(d.pop("warehouseConnection", UNSET))

        project = cls(
            dbt_connection=dbt_connection,
            type=type,
            name=name,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            copied_from_project_uuid=copied_from_project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            warehouse_connection=warehouse_connection,
        )

        project.additional_properties = d
        return project

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
