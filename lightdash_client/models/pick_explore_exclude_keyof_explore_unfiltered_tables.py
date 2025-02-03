from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.explore_type import ExploreType
from ..models.supported_dbt_adapter import SupportedDbtAdapter
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compiled_explore_join import CompiledExploreJoin
    from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_spotlight import (
        PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight,
    )
    from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_tables import (
        PickExploreExcludeKeyofExploreUnfilteredTablesTables,
    )


T = TypeVar("T", bound="PickExploreExcludeKeyofExploreUnfilteredTables")


@_attrs_define
class PickExploreExcludeKeyofExploreUnfilteredTables:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        name (str):
        label (str):
        tags (List[str]):
        base_table (str):
        joined_tables (List['CompiledExploreJoin']):
        tables (PickExploreExcludeKeyofExploreUnfilteredTablesTables):
        target_database (SupportedDbtAdapter):
        type (Union[Unset, ExploreType]):
        spotlight (Union[Unset, PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight]):
        warehouse (Union[Unset, str]):
        group_label (Union[Unset, str]):
        yml_path (Union[Unset, str]):
        sql_path (Union[Unset, str]):
    """

    name: str
    label: str
    tags: List[str]
    base_table: str
    joined_tables: List["CompiledExploreJoin"]
    tables: "PickExploreExcludeKeyofExploreUnfilteredTablesTables"
    target_database: SupportedDbtAdapter
    type: Union[Unset, ExploreType] = UNSET
    spotlight: Union[Unset, "PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight"] = UNSET
    warehouse: Union[Unset, str] = UNSET
    group_label: Union[Unset, str] = UNSET
    yml_path: Union[Unset, str] = UNSET
    sql_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.compiled_explore_join import CompiledExploreJoin
        from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_spotlight import (
            PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight,
        )
        from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_tables import (
            PickExploreExcludeKeyofExploreUnfilteredTablesTables,
        )

        name = self.name

        label = self.label

        tags = self.tags

        base_table = self.base_table

        joined_tables = []
        for joined_tables_item_data in self.joined_tables:
            joined_tables_item = joined_tables_item_data.to_dict()
            joined_tables.append(joined_tables_item)

        tables = self.tables.to_dict()

        target_database = self.target_database.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        spotlight: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spotlight, Unset):
            spotlight = self.spotlight.to_dict()

        warehouse = self.warehouse

        group_label = self.group_label

        yml_path = self.yml_path

        sql_path = self.sql_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "tags": tags,
                "baseTable": base_table,
                "joinedTables": joined_tables,
                "tables": tables,
                "targetDatabase": target_database,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if spotlight is not UNSET:
            field_dict["spotlight"] = spotlight
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label
        if yml_path is not UNSET:
            field_dict["ymlPath"] = yml_path
        if sql_path is not UNSET:
            field_dict["sqlPath"] = sql_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compiled_explore_join import CompiledExploreJoin
        from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_spotlight import (
            PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight,
        )
        from ..models.pick_explore_exclude_keyof_explore_unfiltered_tables_tables import (
            PickExploreExcludeKeyofExploreUnfilteredTablesTables,
        )

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        tags = cast(List[str], d.pop("tags"))

        base_table = d.pop("baseTable")

        joined_tables = []
        _joined_tables = d.pop("joinedTables")
        for joined_tables_item_data in _joined_tables:
            joined_tables_item = CompiledExploreJoin.from_dict(joined_tables_item_data)

            joined_tables.append(joined_tables_item)

        tables = PickExploreExcludeKeyofExploreUnfilteredTablesTables.from_dict(d.pop("tables"))

        target_database = SupportedDbtAdapter(d.pop("targetDatabase"))

        _type = d.pop("type", UNSET)
        type: Union[Unset, ExploreType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ExploreType(_type)

        _spotlight = d.pop("spotlight", UNSET)
        spotlight: Union[Unset, PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight]
        if isinstance(_spotlight, Unset):
            spotlight = UNSET
        else:
            spotlight = PickExploreExcludeKeyofExploreUnfilteredTablesSpotlight.from_dict(_spotlight)

        warehouse = d.pop("warehouse", UNSET)

        group_label = d.pop("groupLabel", UNSET)

        yml_path = d.pop("ymlPath", UNSET)

        sql_path = d.pop("sqlPath", UNSET)

        pick_explore_exclude_keyof_explore_unfiltered_tables = cls(
            name=name,
            label=label,
            tags=tags,
            base_table=base_table,
            joined_tables=joined_tables,
            tables=tables,
            target_database=target_database,
            type=type,
            spotlight=spotlight,
            warehouse=warehouse,
            group_label=group_label,
            yml_path=yml_path,
            sql_path=sql_path,
        )

        pick_explore_exclude_keyof_explore_unfiltered_tables.additional_properties = d
        return pick_explore_exclude_keyof_explore_unfiltered_tables

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
