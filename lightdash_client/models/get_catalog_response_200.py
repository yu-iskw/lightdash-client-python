from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_catalog_response_200_status import GetCatalogResponse200Status

if TYPE_CHECKING:
    from ..models.catalog_field import CatalogField
    from ..models.catalog_table import CatalogTable


T = TypeVar("T", bound="GetCatalogResponse200")


@_attrs_define
class GetCatalogResponse200:
    """
    Attributes:
        results (List[Union['CatalogField', 'CatalogTable']]):
        status (GetCatalogResponse200Status):
    """

    results: List[Union["CatalogField", "CatalogTable"]]
    status: GetCatalogResponse200Status
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.catalog_field import CatalogField

        results = []
        for componentsschemas_api_catalog_results_item_data in self.results:
            componentsschemas_api_catalog_results_item: Dict[str, Any]
            if isinstance(componentsschemas_api_catalog_results_item_data, CatalogField):
                componentsschemas_api_catalog_results_item = componentsschemas_api_catalog_results_item_data.to_dict()
            else:
                componentsschemas_api_catalog_results_item = componentsschemas_api_catalog_results_item_data.to_dict()

            results.append(componentsschemas_api_catalog_results_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_field import CatalogField
        from ..models.catalog_table import CatalogTable

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for componentsschemas_api_catalog_results_item_data in _results:

            def _parse_componentsschemas_api_catalog_results_item(
                data: object,
            ) -> Union["CatalogField", "CatalogTable"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_catalog_item_type_0 = CatalogField.from_dict(data)

                    return componentsschemas_catalog_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_catalog_item_type_1 = CatalogTable.from_dict(data)

                return componentsschemas_catalog_item_type_1

            componentsschemas_api_catalog_results_item = _parse_componentsschemas_api_catalog_results_item(
                componentsschemas_api_catalog_results_item_data
            )

            results.append(componentsschemas_api_catalog_results_item)

        status = GetCatalogResponse200Status(d.pop("status"))

        get_catalog_response_200 = cls(
            results=results,
            status=status,
        )

        get_catalog_response_200.additional_properties = d
        return get_catalog_response_200

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
