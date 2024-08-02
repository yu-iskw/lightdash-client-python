from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supported_dbt_adapter import SupportedDbtAdapter
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compiled_explore_join import CompiledExploreJoin
    from ..models.explore_tables import ExploreTables


T = TypeVar("T", bound="Explore")


@_attrs_define
class Explore:
    """
    Attributes:
        target_database (SupportedDbtAdapter):
        tables (ExploreTables):
        joined_tables (List['CompiledExploreJoin']):
        base_table (str):
        tags (List[str]):
        label (str):
        name (str):
        sql_path (Union[Unset, str]):
        yml_path (Union[Unset, str]):
        warehouse (Union[Unset, str]):
        group_label (Union[Unset, str]):
    """

    target_database: SupportedDbtAdapter
    tables: "ExploreTables"
    joined_tables: List["CompiledExploreJoin"]
    base_table: str
    tags: List[str]
    label: str
    name: str
    sql_path: Union[Unset, str] = UNSET
    yml_path: Union[Unset, str] = UNSET
    warehouse: Union[Unset, str] = UNSET
    group_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_database = self.target_database.value

        tables = self.tables.to_dict()

        joined_tables = []
        for joined_tables_item_data in self.joined_tables:
            joined_tables_item = joined_tables_item_data.to_dict()
            joined_tables.append(joined_tables_item)

        base_table = self.base_table

        tags = self.tags

        label = self.label

        name = self.name

        sql_path = self.sql_path

        yml_path = self.yml_path

        warehouse = self.warehouse

        group_label = self.group_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetDatabase": target_database,
                "tables": tables,
                "joinedTables": joined_tables,
                "baseTable": base_table,
                "tags": tags,
                "label": label,
                "name": name,
            }
        )
        if sql_path is not UNSET:
            field_dict["sqlPath"] = sql_path
        if yml_path is not UNSET:
            field_dict["ymlPath"] = yml_path
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compiled_explore_join import CompiledExploreJoin
        from ..models.explore_tables import ExploreTables

        d = src_dict.copy()
        target_database = SupportedDbtAdapter(d.pop("targetDatabase"))

        tables = ExploreTables.from_dict(d.pop("tables"))

        joined_tables = []
        _joined_tables = d.pop("joinedTables")
        for joined_tables_item_data in _joined_tables:
            joined_tables_item = CompiledExploreJoin.from_dict(joined_tables_item_data)

            joined_tables.append(joined_tables_item)

        base_table = d.pop("baseTable")

        tags = cast(List[str], d.pop("tags"))

        label = d.pop("label")

        name = d.pop("name")

        sql_path = d.pop("sqlPath", UNSET)

        yml_path = d.pop("ymlPath", UNSET)

        warehouse = d.pop("warehouse", UNSET)

        group_label = d.pop("groupLabel", UNSET)

        explore = cls(
            target_database=target_database,
            tables=tables,
            joined_tables=joined_tables,
            base_table=base_table,
            tags=tags,
            label=label,
            name=name,
            sql_path=sql_path,
            yml_path=yml_path,
            warehouse=warehouse,
            group_label=group_label,
        )

        explore.additional_properties = d
        return explore

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
