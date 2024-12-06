from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_metrics_tree_edge import CatalogMetricsTreeEdge


T = TypeVar("T", bound="ApiGetMetricsTreeResults")


@_attrs_define
class ApiGetMetricsTreeResults:
    """
    Attributes:
        edges (List['CatalogMetricsTreeEdge']):
    """

    edges: List["CatalogMetricsTreeEdge"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.catalog_metrics_tree_edge import CatalogMetricsTreeEdge

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edges": edges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_metrics_tree_edge import CatalogMetricsTreeEdge

        d = src_dict.copy()
        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = CatalogMetricsTreeEdge.from_dict(edges_item_data)

            edges.append(edges_item)

        api_get_metrics_tree_results = cls(
            edges=edges,
        )

        api_get_metrics_tree_results.additional_properties = d
        return api_get_metrics_tree_results

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
