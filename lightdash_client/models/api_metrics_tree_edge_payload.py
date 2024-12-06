from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMetricsTreeEdgePayload")


@_attrs_define
class ApiMetricsTreeEdgePayload:
    """
    Attributes:
        target_catalog_search_uuid (str):
        source_catalog_search_uuid (str):
    """

    target_catalog_search_uuid: str
    source_catalog_search_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_catalog_search_uuid = self.target_catalog_search_uuid

        source_catalog_search_uuid = self.source_catalog_search_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetCatalogSearchUuid": target_catalog_search_uuid,
                "sourceCatalogSearchUuid": source_catalog_search_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_catalog_search_uuid = d.pop("targetCatalogSearchUuid")

        source_catalog_search_uuid = d.pop("sourceCatalogSearchUuid")

        api_metrics_tree_edge_payload = cls(
            target_catalog_search_uuid=target_catalog_search_uuid,
            source_catalog_search_uuid=source_catalog_search_uuid,
        )

        api_metrics_tree_edge_payload.additional_properties = d
        return api_metrics_tree_edge_payload

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
