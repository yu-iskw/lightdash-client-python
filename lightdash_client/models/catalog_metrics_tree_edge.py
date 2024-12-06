import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pick_catalog_field_catalog_search_uuid_or_name_or_table_name import (
        PickCatalogFieldCatalogSearchUuidOrNameOrTableName,
    )


T = TypeVar("T", bound="CatalogMetricsTreeEdge")


@_attrs_define
class CatalogMetricsTreeEdge:
    """
    Attributes:
        project_uuid (str):
        created_by_user_uuid (Union[None, str]):
        created_at (datetime.datetime):
        target (PickCatalogFieldCatalogSearchUuidOrNameOrTableName): From T, pick a set of properties whose keys are in
            the union K
        source (PickCatalogFieldCatalogSearchUuidOrNameOrTableName): From T, pick a set of properties whose keys are in
            the union K
    """

    project_uuid: str
    created_by_user_uuid: Union[None, str]
    created_at: datetime.datetime
    target: "PickCatalogFieldCatalogSearchUuidOrNameOrTableName"
    source: "PickCatalogFieldCatalogSearchUuidOrNameOrTableName"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pick_catalog_field_catalog_search_uuid_or_name_or_table_name import (
            PickCatalogFieldCatalogSearchUuidOrNameOrTableName,
        )

        project_uuid = self.project_uuid

        created_by_user_uuid: Union[None, str]
        created_by_user_uuid = self.created_by_user_uuid

        created_at = self.created_at.isoformat()

        target = self.target.to_dict()

        source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectUuid": project_uuid,
                "createdByUserUuid": created_by_user_uuid,
                "createdAt": created_at,
                "target": target,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pick_catalog_field_catalog_search_uuid_or_name_or_table_name import (
            PickCatalogFieldCatalogSearchUuidOrNameOrTableName,
        )

        d = src_dict.copy()
        project_uuid = d.pop("projectUuid")

        def _parse_created_by_user_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_uuid = _parse_created_by_user_uuid(d.pop("createdByUserUuid"))

        created_at = isoparse(d.pop("createdAt"))

        target = PickCatalogFieldCatalogSearchUuidOrNameOrTableName.from_dict(d.pop("target"))

        source = PickCatalogFieldCatalogSearchUuidOrNameOrTableName.from_dict(d.pop("source"))

        catalog_metrics_tree_edge = cls(
            project_uuid=project_uuid,
            created_by_user_uuid=created_by_user_uuid,
            created_at=created_at,
            target=target,
            source=source,
        )

        catalog_metrics_tree_edge.additional_properties = d
        return catalog_metrics_tree_edge

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
