from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_field import CatalogField
    from ..models.knex_paginated_data_api_metrics_catalog_results_pagination import (
        KnexPaginatedDataApiMetricsCatalogResultsPagination,
    )


T = TypeVar("T", bound="KnexPaginatedDataApiMetricsCatalogResults")


@_attrs_define
class KnexPaginatedDataApiMetricsCatalogResults:
    """
    Attributes:
        data (List['CatalogField']):
        pagination (Union[Unset, KnexPaginatedDataApiMetricsCatalogResultsPagination]):
    """

    data: List["CatalogField"]
    pagination: Union[Unset, "KnexPaginatedDataApiMetricsCatalogResultsPagination"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.catalog_field import CatalogField
        from ..models.knex_paginated_data_api_metrics_catalog_results_pagination import (
            KnexPaginatedDataApiMetricsCatalogResultsPagination,
        )

        data = []
        for componentsschemas_api_metrics_catalog_results_item_data in self.data:
            componentsschemas_api_metrics_catalog_results_item = (
                componentsschemas_api_metrics_catalog_results_item_data.to_dict()
            )
            data.append(componentsschemas_api_metrics_catalog_results_item)

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_field import CatalogField
        from ..models.knex_paginated_data_api_metrics_catalog_results_pagination import (
            KnexPaginatedDataApiMetricsCatalogResultsPagination,
        )

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for componentsschemas_api_metrics_catalog_results_item_data in _data:
            componentsschemas_api_metrics_catalog_results_item = CatalogField.from_dict(
                componentsschemas_api_metrics_catalog_results_item_data
            )

            data.append(componentsschemas_api_metrics_catalog_results_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, KnexPaginatedDataApiMetricsCatalogResultsPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = KnexPaginatedDataApiMetricsCatalogResultsPagination.from_dict(_pagination)

        knex_paginated_data_api_metrics_catalog_results = cls(
            data=data,
            pagination=pagination,
        )

        knex_paginated_data_api_metrics_catalog_results.additional_properties = d
        return knex_paginated_data_api_metrics_catalog_results

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
