from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_project_response_results_type import ApiProjectResponseResultsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_project_response_results_dbt_connection_type_0 import (
        ApiProjectResponseResultsDbtConnectionType0,
    )
    from ..models.api_project_response_results_dbt_connection_type_1 import (
        ApiProjectResponseResultsDbtConnectionType1,
    )
    from ..models.api_project_response_results_dbt_connection_type_2 import (
        ApiProjectResponseResultsDbtConnectionType2,
    )
    from ..models.api_project_response_results_dbt_connection_type_3 import (
        ApiProjectResponseResultsDbtConnectionType3,
    )
    from ..models.api_project_response_results_dbt_connection_type_4 import (
        ApiProjectResponseResultsDbtConnectionType4,
    )
    from ..models.api_project_response_results_dbt_connection_type_5 import (
        ApiProjectResponseResultsDbtConnectionType5,
    )
    from ..models.api_project_response_results_dbt_connection_type_6 import (
        ApiProjectResponseResultsDbtConnectionType6,
    )
    from ..models.api_project_response_results_warehouse_connection_type_0 import (
        ApiProjectResponseResultsWarehouseConnectionType0,
    )
    from ..models.api_project_response_results_warehouse_connection_type_1 import (
        ApiProjectResponseResultsWarehouseConnectionType1,
    )
    from ..models.api_project_response_results_warehouse_connection_type_2 import (
        ApiProjectResponseResultsWarehouseConnectionType2,
    )
    from ..models.api_project_response_results_warehouse_connection_type_3 import (
        ApiProjectResponseResultsWarehouseConnectionType3,
    )
    from ..models.api_project_response_results_warehouse_connection_type_4 import (
        ApiProjectResponseResultsWarehouseConnectionType4,
    )
    from ..models.api_project_response_results_warehouse_connection_type_5 import (
        ApiProjectResponseResultsWarehouseConnectionType5,
    )


T = TypeVar("T", bound="ApiProjectResponseResults")


@attr.s(auto_attribs=True)
class ApiProjectResponseResults:
    """
    Attributes:
        dbt_connection (Union['ApiProjectResponseResultsDbtConnectionType0',
            'ApiProjectResponseResultsDbtConnectionType1', 'ApiProjectResponseResultsDbtConnectionType2',
            'ApiProjectResponseResultsDbtConnectionType3', 'ApiProjectResponseResultsDbtConnectionType4',
            'ApiProjectResponseResultsDbtConnectionType5', 'ApiProjectResponseResultsDbtConnectionType6']):
        type (ApiProjectResponseResultsType):
        name (str):
        project_uuid (str):
        organization_uuid (str):
        copied_from_project_uuid (Union[Unset, str]):
        pinned_list_uuid (Union[Unset, str]):
        warehouse_connection (Union['ApiProjectResponseResultsWarehouseConnectionType0',
            'ApiProjectResponseResultsWarehouseConnectionType1', 'ApiProjectResponseResultsWarehouseConnectionType2',
            'ApiProjectResponseResultsWarehouseConnectionType3', 'ApiProjectResponseResultsWarehouseConnectionType4',
            'ApiProjectResponseResultsWarehouseConnectionType5', Unset]):
    """

    dbt_connection: Union[
        "ApiProjectResponseResultsDbtConnectionType0",
        "ApiProjectResponseResultsDbtConnectionType1",
        "ApiProjectResponseResultsDbtConnectionType2",
        "ApiProjectResponseResultsDbtConnectionType3",
        "ApiProjectResponseResultsDbtConnectionType4",
        "ApiProjectResponseResultsDbtConnectionType5",
        "ApiProjectResponseResultsDbtConnectionType6",
    ]
    type: ApiProjectResponseResultsType
    name: str
    project_uuid: str
    organization_uuid: str
    copied_from_project_uuid: Union[Unset, str] = UNSET
    pinned_list_uuid: Union[Unset, str] = UNSET
    warehouse_connection: Union[
        "ApiProjectResponseResultsWarehouseConnectionType0",
        "ApiProjectResponseResultsWarehouseConnectionType1",
        "ApiProjectResponseResultsWarehouseConnectionType2",
        "ApiProjectResponseResultsWarehouseConnectionType3",
        "ApiProjectResponseResultsWarehouseConnectionType4",
        "ApiProjectResponseResultsWarehouseConnectionType5",
        Unset,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_project_response_results_dbt_connection_type_0 import (
            ApiProjectResponseResultsDbtConnectionType0,
        )
        from ..models.api_project_response_results_dbt_connection_type_1 import (
            ApiProjectResponseResultsDbtConnectionType1,
        )
        from ..models.api_project_response_results_dbt_connection_type_2 import (
            ApiProjectResponseResultsDbtConnectionType2,
        )
        from ..models.api_project_response_results_dbt_connection_type_3 import (
            ApiProjectResponseResultsDbtConnectionType3,
        )
        from ..models.api_project_response_results_dbt_connection_type_4 import (
            ApiProjectResponseResultsDbtConnectionType4,
        )
        from ..models.api_project_response_results_dbt_connection_type_5 import (
            ApiProjectResponseResultsDbtConnectionType5,
        )
        from ..models.api_project_response_results_warehouse_connection_type_0 import (
            ApiProjectResponseResultsWarehouseConnectionType0,
        )
        from ..models.api_project_response_results_warehouse_connection_type_1 import (
            ApiProjectResponseResultsWarehouseConnectionType1,
        )
        from ..models.api_project_response_results_warehouse_connection_type_2 import (
            ApiProjectResponseResultsWarehouseConnectionType2,
        )
        from ..models.api_project_response_results_warehouse_connection_type_3 import (
            ApiProjectResponseResultsWarehouseConnectionType3,
        )
        from ..models.api_project_response_results_warehouse_connection_type_4 import (
            ApiProjectResponseResultsWarehouseConnectionType4,
        )

        dbt_connection: Dict[str, Any]

        if isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType0):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType1):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType2):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType3):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType4):
            dbt_connection = self.dbt_connection.to_dict()

        elif isinstance(self.dbt_connection, ApiProjectResponseResultsDbtConnectionType5):
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

        elif isinstance(self.warehouse_connection, ApiProjectResponseResultsWarehouseConnectionType0):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ApiProjectResponseResultsWarehouseConnectionType1):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ApiProjectResponseResultsWarehouseConnectionType2):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ApiProjectResponseResultsWarehouseConnectionType3):
            warehouse_connection = UNSET
            if not isinstance(self.warehouse_connection, Unset):
                warehouse_connection = self.warehouse_connection.to_dict()

        elif isinstance(self.warehouse_connection, ApiProjectResponseResultsWarehouseConnectionType4):
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
        from ..models.api_project_response_results_dbt_connection_type_0 import (
            ApiProjectResponseResultsDbtConnectionType0,
        )
        from ..models.api_project_response_results_dbt_connection_type_1 import (
            ApiProjectResponseResultsDbtConnectionType1,
        )
        from ..models.api_project_response_results_dbt_connection_type_2 import (
            ApiProjectResponseResultsDbtConnectionType2,
        )
        from ..models.api_project_response_results_dbt_connection_type_3 import (
            ApiProjectResponseResultsDbtConnectionType3,
        )
        from ..models.api_project_response_results_dbt_connection_type_4 import (
            ApiProjectResponseResultsDbtConnectionType4,
        )
        from ..models.api_project_response_results_dbt_connection_type_5 import (
            ApiProjectResponseResultsDbtConnectionType5,
        )
        from ..models.api_project_response_results_dbt_connection_type_6 import (
            ApiProjectResponseResultsDbtConnectionType6,
        )
        from ..models.api_project_response_results_warehouse_connection_type_0 import (
            ApiProjectResponseResultsWarehouseConnectionType0,
        )
        from ..models.api_project_response_results_warehouse_connection_type_1 import (
            ApiProjectResponseResultsWarehouseConnectionType1,
        )
        from ..models.api_project_response_results_warehouse_connection_type_2 import (
            ApiProjectResponseResultsWarehouseConnectionType2,
        )
        from ..models.api_project_response_results_warehouse_connection_type_3 import (
            ApiProjectResponseResultsWarehouseConnectionType3,
        )
        from ..models.api_project_response_results_warehouse_connection_type_4 import (
            ApiProjectResponseResultsWarehouseConnectionType4,
        )
        from ..models.api_project_response_results_warehouse_connection_type_5 import (
            ApiProjectResponseResultsWarehouseConnectionType5,
        )

        d = src_dict.copy()

        def _parse_dbt_connection(
            data: object,
        ) -> Union[
            "ApiProjectResponseResultsDbtConnectionType0",
            "ApiProjectResponseResultsDbtConnectionType1",
            "ApiProjectResponseResultsDbtConnectionType2",
            "ApiProjectResponseResultsDbtConnectionType3",
            "ApiProjectResponseResultsDbtConnectionType4",
            "ApiProjectResponseResultsDbtConnectionType5",
            "ApiProjectResponseResultsDbtConnectionType6",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_0 = ApiProjectResponseResultsDbtConnectionType0.from_dict(data)

                return dbt_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_1 = ApiProjectResponseResultsDbtConnectionType1.from_dict(data)

                return dbt_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_2 = ApiProjectResponseResultsDbtConnectionType2.from_dict(data)

                return dbt_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_3 = ApiProjectResponseResultsDbtConnectionType3.from_dict(data)

                return dbt_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_4 = ApiProjectResponseResultsDbtConnectionType4.from_dict(data)

                return dbt_connection_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dbt_connection_type_5 = ApiProjectResponseResultsDbtConnectionType5.from_dict(data)

                return dbt_connection_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            dbt_connection_type_6 = ApiProjectResponseResultsDbtConnectionType6.from_dict(data)

            return dbt_connection_type_6

        dbt_connection = _parse_dbt_connection(d.pop("dbtConnection"))

        type = ApiProjectResponseResultsType(d.pop("type"))

        name = d.pop("name")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        copied_from_project_uuid = d.pop("copiedFromProjectUuid", UNSET)

        pinned_list_uuid = d.pop("pinnedListUuid", UNSET)

        def _parse_warehouse_connection(
            data: object,
        ) -> Union[
            "ApiProjectResponseResultsWarehouseConnectionType0",
            "ApiProjectResponseResultsWarehouseConnectionType1",
            "ApiProjectResponseResultsWarehouseConnectionType2",
            "ApiProjectResponseResultsWarehouseConnectionType3",
            "ApiProjectResponseResultsWarehouseConnectionType4",
            "ApiProjectResponseResultsWarehouseConnectionType5",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_0 = data
                warehouse_connection_type_0: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType0]
                if isinstance(_warehouse_connection_type_0, Unset):
                    warehouse_connection_type_0 = UNSET
                else:
                    warehouse_connection_type_0 = ApiProjectResponseResultsWarehouseConnectionType0.from_dict(
                        _warehouse_connection_type_0
                    )

                return warehouse_connection_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_1 = data
                warehouse_connection_type_1: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType1]
                if isinstance(_warehouse_connection_type_1, Unset):
                    warehouse_connection_type_1 = UNSET
                else:
                    warehouse_connection_type_1 = ApiProjectResponseResultsWarehouseConnectionType1.from_dict(
                        _warehouse_connection_type_1
                    )

                return warehouse_connection_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_2 = data
                warehouse_connection_type_2: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType2]
                if isinstance(_warehouse_connection_type_2, Unset):
                    warehouse_connection_type_2 = UNSET
                else:
                    warehouse_connection_type_2 = ApiProjectResponseResultsWarehouseConnectionType2.from_dict(
                        _warehouse_connection_type_2
                    )

                return warehouse_connection_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_3 = data
                warehouse_connection_type_3: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType3]
                if isinstance(_warehouse_connection_type_3, Unset):
                    warehouse_connection_type_3 = UNSET
                else:
                    warehouse_connection_type_3 = ApiProjectResponseResultsWarehouseConnectionType3.from_dict(
                        _warehouse_connection_type_3
                    )

                return warehouse_connection_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _warehouse_connection_type_4 = data
                warehouse_connection_type_4: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType4]
                if isinstance(_warehouse_connection_type_4, Unset):
                    warehouse_connection_type_4 = UNSET
                else:
                    warehouse_connection_type_4 = ApiProjectResponseResultsWarehouseConnectionType4.from_dict(
                        _warehouse_connection_type_4
                    )

                return warehouse_connection_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _warehouse_connection_type_5 = data
            warehouse_connection_type_5: Union[Unset, ApiProjectResponseResultsWarehouseConnectionType5]
            if isinstance(_warehouse_connection_type_5, Unset):
                warehouse_connection_type_5 = UNSET
            else:
                warehouse_connection_type_5 = ApiProjectResponseResultsWarehouseConnectionType5.from_dict(
                    _warehouse_connection_type_5
                )

            return warehouse_connection_type_5

        warehouse_connection = _parse_warehouse_connection(d.pop("warehouseConnection", UNSET))

        api_project_response_results = cls(
            dbt_connection=dbt_connection,
            type=type,
            name=name,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            copied_from_project_uuid=copied_from_project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            warehouse_connection=warehouse_connection,
        )

        api_project_response_results.additional_properties = d
        return api_project_response_results

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
