from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_response_200_results_dbt_version import (
    GetProjectResponse200ResultsDbtVersion,
)
from ..models.get_project_response_200_results_type import (
    GetProjectResponse200ResultsType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_response_200_results_dbt_connection_type_0 import (
        GetProjectResponse200ResultsDbtConnectionType0,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_1 import (
        GetProjectResponse200ResultsDbtConnectionType1,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_2 import (
        GetProjectResponse200ResultsDbtConnectionType2,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_3 import (
        GetProjectResponse200ResultsDbtConnectionType3,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_4 import (
        GetProjectResponse200ResultsDbtConnectionType4,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_5 import (
        GetProjectResponse200ResultsDbtConnectionType5,
    )
    from ..models.get_project_response_200_results_dbt_connection_type_6 import (
        GetProjectResponse200ResultsDbtConnectionType6,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_0 import (
        GetProjectResponse200ResultsWarehouseConnectionType0,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_1 import (
        GetProjectResponse200ResultsWarehouseConnectionType1,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_2 import (
        GetProjectResponse200ResultsWarehouseConnectionType2,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_3 import (
        GetProjectResponse200ResultsWarehouseConnectionType3,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_4 import (
        GetProjectResponse200ResultsWarehouseConnectionType4,
    )
    from ..models.get_project_response_200_results_warehouse_connection_type_5 import (
        GetProjectResponse200ResultsWarehouseConnectionType5,
    )


T = TypeVar("T", bound="GetProjectResponse200Results")


@attr.s(auto_attribs=True)
class GetProjectResponse200Results:
    """
    Attributes:
        dbt_version (GetProjectResponse200ResultsDbtVersion):
        dbt_connection (Union['GetProjectResponse200ResultsDbtConnectionType0',
            'GetProjectResponse200ResultsDbtConnectionType1', 'GetProjectResponse200ResultsDbtConnectionType2',
            'GetProjectResponse200ResultsDbtConnectionType3', 'GetProjectResponse200ResultsDbtConnectionType4',
            'GetProjectResponse200ResultsDbtConnectionType5', 'GetProjectResponse200ResultsDbtConnectionType6']):
        type (GetProjectResponse200ResultsType):
        name (str):
        project_uuid (str):
        organization_uuid (str):
        copied_from_project_uuid (Union[Unset, str]):
        pinned_list_uuid (Union[Unset, str]):
        warehouse_connection (Union['GetProjectResponse200ResultsWarehouseConnectionType0',
            'GetProjectResponse200ResultsWarehouseConnectionType1', 'GetProjectResponse200ResultsWarehouseConnectionType2',
            'GetProjectResponse200ResultsWarehouseConnectionType3', 'GetProjectResponse200ResultsWarehouseConnectionType4',
            'GetProjectResponse200ResultsWarehouseConnectionType5', Unset]):
    """

    dbt_version: GetProjectResponse200ResultsDbtVersion
    dbt_connection: Union[
        "GetProjectResponse200ResultsDbtConnectionType0",
        "GetProjectResponse200ResultsDbtConnectionType1",
        "GetProjectResponse200ResultsDbtConnectionType2",
        "GetProjectResponse200ResultsDbtConnectionType3",
        "GetProjectResponse200ResultsDbtConnectionType4",
        "GetProjectResponse200ResultsDbtConnectionType5",
        "GetProjectResponse200ResultsDbtConnectionType6",
    ]
    type: GetProjectResponse200ResultsType
    name: str
    project_uuid: str
    organization_uuid: str
    copied_from_project_uuid: Union[Unset, str] = UNSET
    pinned_list_uuid: Union[Unset, str] = UNSET
    warehouse_connection: Union[
        "GetProjectResponse200ResultsWarehouseConnectionType0",
        "GetProjectResponse200ResultsWarehouseConnectionType1",
        "GetProjectResponse200ResultsWarehouseConnectionType2",
        "GetProjectResponse200ResultsWarehouseConnectionType3",
        "GetProjectResponse200ResultsWarehouseConnectionType4",
        "GetProjectResponse200ResultsWarehouseConnectionType5",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_project_response_200_results_dbt_connection_type_0 import (
            GetProjectResponse200ResultsDbtConnectionType0,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_1 import (
            GetProjectResponse200ResultsDbtConnectionType1,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_2 import (
            GetProjectResponse200ResultsDbtConnectionType2,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_3 import (
            GetProjectResponse200ResultsDbtConnectionType3,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_4 import (
            GetProjectResponse200ResultsDbtConnectionType4,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_5 import (
            GetProjectResponse200ResultsDbtConnectionType5,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_0 import (
            GetProjectResponse200ResultsWarehouseConnectionType0,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_1 import (
            GetProjectResponse200ResultsWarehouseConnectionType1,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_2 import (
            GetProjectResponse200ResultsWarehouseConnectionType2,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_3 import (
            GetProjectResponse200ResultsWarehouseConnectionType3,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_4 import (
            GetProjectResponse200ResultsWarehouseConnectionType4,
        )

        dbt_version = self.dbt_version.value

        dbt_connection: Dict[str, Any]

        if isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType0):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType1):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType2):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType3):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType4):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, GetProjectResponse200ResultsDbtConnectionType5):
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

        elif isinstance(self.warehouse_connection, GetProjectResponse200ResultsWarehouseConnectionType0):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, GetProjectResponse200ResultsWarehouseConnectionType1):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, GetProjectResponse200ResultsWarehouseConnectionType2):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, GetProjectResponse200ResultsWarehouseConnectionType3):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, GetProjectResponse200ResultsWarehouseConnectionType4):
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
                "dbtVersion": dbt_version,
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
        from ..models.get_project_response_200_results_dbt_connection_type_0 import (
            GetProjectResponse200ResultsDbtConnectionType0,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_1 import (
            GetProjectResponse200ResultsDbtConnectionType1,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_2 import (
            GetProjectResponse200ResultsDbtConnectionType2,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_3 import (
            GetProjectResponse200ResultsDbtConnectionType3,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_4 import (
            GetProjectResponse200ResultsDbtConnectionType4,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_5 import (
            GetProjectResponse200ResultsDbtConnectionType5,
        )
        from ..models.get_project_response_200_results_dbt_connection_type_6 import (
            GetProjectResponse200ResultsDbtConnectionType6,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_0 import (
            GetProjectResponse200ResultsWarehouseConnectionType0,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_1 import (
            GetProjectResponse200ResultsWarehouseConnectionType1,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_2 import (
            GetProjectResponse200ResultsWarehouseConnectionType2,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_3 import (
            GetProjectResponse200ResultsWarehouseConnectionType3,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_4 import (
            GetProjectResponse200ResultsWarehouseConnectionType4,
        )
        from ..models.get_project_response_200_results_warehouse_connection_type_5 import (
            GetProjectResponse200ResultsWarehouseConnectionType5,
        )

        d = src_dict.copy()
        dbt_version = GetProjectResponse200ResultsDbtVersion(d.pop("dbtVersion"))

        def _parse_dbt_connection(
            data: object,
        ) -> Union[
            "GetProjectResponse200ResultsDbtConnectionType0",
            "GetProjectResponse200ResultsDbtConnectionType1",
            "GetProjectResponse200ResultsDbtConnectionType2",
            "GetProjectResponse200ResultsDbtConnectionType3",
            "GetProjectResponse200ResultsDbtConnectionType4",
            "GetProjectResponse200ResultsDbtConnectionType5",
            "GetProjectResponse200ResultsDbtConnectionType6",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_0 = GetProjectResponse200ResultsDbtConnectionType0.from_dict(data)

                return dbt_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_1 = GetProjectResponse200ResultsDbtConnectionType1.from_dict(data)

                return dbt_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_2 = GetProjectResponse200ResultsDbtConnectionType2.from_dict(data)

                return dbt_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_3 = GetProjectResponse200ResultsDbtConnectionType3.from_dict(data)

                return dbt_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_4 = GetProjectResponse200ResultsDbtConnectionType4.from_dict(data)

                return dbt_connection_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_5 = GetProjectResponse200ResultsDbtConnectionType5.from_dict(data)

                return dbt_connection_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            dbt_connection_type_6 = GetProjectResponse200ResultsDbtConnectionType6.from_dict(data)

            return dbt_connection_type_6

        dbt_connection = _parse_dbt_connection(d.pop("dbtConnection"))

        type = GetProjectResponse200ResultsType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        copied_from_project_uuid = d.pop("copiedFromProjectUuid", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid", UNSET)

        def _parse_warehouse_connection(
            data: object,
        ) -> Union[
            "GetProjectResponse200ResultsWarehouseConnectionType0",
            "GetProjectResponse200ResultsWarehouseConnectionType1",
            "GetProjectResponse200ResultsWarehouseConnectionType2",
            "GetProjectResponse200ResultsWarehouseConnectionType3",
            "GetProjectResponse200ResultsWarehouseConnectionType4",
            "GetProjectResponse200ResultsWarehouseConnectionType5",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_0 = data
                warehouse_connection_type_0: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType0]
                if isinstance(_warehouse_connection_type_0, Unset):
                    warehouse_connection_type_0 = UNSET
                else:
                    warehouse_connection_type_0 = GetProjectResponse200ResultsWarehouseConnectionType0.from_dict(
                        _warehouse_connection_type_0
                    )

                return warehouse_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_1 = data
                warehouse_connection_type_1: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType1]
                if isinstance(_warehouse_connection_type_1, Unset):
                    warehouse_connection_type_1 = UNSET
                else:
                    warehouse_connection_type_1 = GetProjectResponse200ResultsWarehouseConnectionType1.from_dict(
                        _warehouse_connection_type_1
                    )

                return warehouse_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_2 = data
                warehouse_connection_type_2: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType2]
                if isinstance(_warehouse_connection_type_2, Unset):
                    warehouse_connection_type_2 = UNSET
                else:
                    warehouse_connection_type_2 = GetProjectResponse200ResultsWarehouseConnectionType2.from_dict(
                        _warehouse_connection_type_2
                    )

                return warehouse_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_3 = data
                warehouse_connection_type_3: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType3]
                if isinstance(_warehouse_connection_type_3, Unset):
                    warehouse_connection_type_3 = UNSET
                else:
                    warehouse_connection_type_3 = GetProjectResponse200ResultsWarehouseConnectionType3.from_dict(
                        _warehouse_connection_type_3
                    )

                return warehouse_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_4 = data
                warehouse_connection_type_4: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType4]
                if isinstance(_warehouse_connection_type_4, Unset):
                    warehouse_connection_type_4 = UNSET
                else:
                    warehouse_connection_type_4 = GetProjectResponse200ResultsWarehouseConnectionType4.from_dict(
                        _warehouse_connection_type_4
                    )

                return warehouse_connection_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _warehouse_connection_type_5 = data
            warehouse_connection_type_5: Union[Unset, GetProjectResponse200ResultsWarehouseConnectionType5]
            if isinstance(_warehouse_connection_type_5, Unset):
                warehouse_connection_type_5 = UNSET
            else:
                warehouse_connection_type_5 = GetProjectResponse200ResultsWarehouseConnectionType5.from_dict(
                    _warehouse_connection_type_5
                )

            return warehouse_connection_type_5

        warehouse_connection = _parse_warehouse_connection(d.pop("warehouseConnection", UNSET))

        get_project_response_200_results = cls(
            dbt_version=dbt_version,
            dbt_connection=dbt_connection,
            type=type,
            name=name,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            copied_from_project_uuid=copied_from_project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            warehouse_connection=warehouse_connection,
        )

        get_project_response_200_results.additional_properties = d
        return get_project_response_200_results

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
