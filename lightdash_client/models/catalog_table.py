from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_table import CatalogTypeTable
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compiled_explore_join import CompiledExploreJoin
    from ..models.custom_icon import CustomIcon
    from ..models.emoji_icon import EmojiIcon
    from ..models.inline_error import InlineError
    from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import PickTagNameOrColorOrTagUuidOrYamlReference
    from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray


T = TypeVar("T", bound="CatalogTable")


@_attrs_define
class CatalogTable:
    """
    Attributes:
        name (str):
        label (str):
        icon (Union['CustomIcon', 'EmojiIcon', None]):
        categories (List['PickTagNameOrColorOrTagUuidOrYamlReference']):
        type (CatalogTypeTable):
        catalog_search_uuid (str):
        description (Union[Unset, str]):
        group_label (Union[Unset, str]):
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        chart_usage (Union[Unset, float]):
        joined_tables (Union[Unset, List['CompiledExploreJoin']]):
        tags (Union[Unset, List[str]]):
        errors (Union[Unset, List['InlineError']]):
    """

    name: str
    label: str
    icon: Union["CustomIcon", "EmojiIcon", None]
    categories: List["PickTagNameOrColorOrTagUuidOrYamlReference"]
    type: CatalogTypeTable
    catalog_search_uuid: str
    description: Union[Unset, str] = UNSET
    group_label: Union[Unset, str] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    chart_usage: Union[Unset, float] = UNSET
    joined_tables: Union[Unset, List["CompiledExploreJoin"]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    errors: Union[Unset, List["InlineError"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.compiled_explore_join import CompiledExploreJoin
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon
        from ..models.inline_error import InlineError
        from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import (
            PickTagNameOrColorOrTagUuidOrYamlReference,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray

        name = self.name

        label = self.label

        icon: Union[Dict[str, Any], None]
        if isinstance(self.icon, EmojiIcon):
            icon = self.icon.to_dict()
        elif isinstance(self.icon, CustomIcon):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        type = self.type.value

        catalog_search_uuid = self.catalog_search_uuid

        description = self.description

        group_label = self.group_label

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        chart_usage = self.chart_usage

        joined_tables: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.joined_tables, Unset):
            joined_tables = []
            for joined_tables_item_data in self.joined_tables:
                joined_tables_item = joined_tables_item_data.to_dict()
                joined_tables.append(joined_tables_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "icon": icon,
                "categories": categories,
                "type": type,
                "catalogSearchUuid": catalog_search_uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if chart_usage is not UNSET:
            field_dict["chartUsage"] = chart_usage
        if joined_tables is not UNSET:
            field_dict["joinedTables"] = joined_tables
        if tags is not UNSET:
            field_dict["tags"] = tags
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compiled_explore_join import CompiledExploreJoin
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon
        from ..models.inline_error import InlineError
        from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import (
            PickTagNameOrColorOrTagUuidOrYamlReference,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        def _parse_icon(data: object) -> Union["CustomIcon", "EmojiIcon", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_catalog_item_icon_type_0 = EmojiIcon.from_dict(data)

                return componentsschemas_catalog_item_icon_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_catalog_item_icon_type_1 = CustomIcon.from_dict(data)

                return componentsschemas_catalog_item_icon_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomIcon", "EmojiIcon", None], data)

        icon = _parse_icon(d.pop("icon"))

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = PickTagNameOrColorOrTagUuidOrYamlReference.from_dict(categories_item_data)

            categories.append(categories_item)

        type = CatalogTypeTable(d.pop("type"))

        catalog_search_uuid = d.pop("catalogSearchUuid")

        description = d.pop("description", UNSET)

        group_label = d.pop("groupLabel", UNSET)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        chart_usage = d.pop("chartUsage", UNSET)

        joined_tables = []
        _joined_tables = d.pop("joinedTables", UNSET)
        for joined_tables_item_data in _joined_tables or []:
            joined_tables_item = CompiledExploreJoin.from_dict(joined_tables_item_data)

            joined_tables.append(joined_tables_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = InlineError.from_dict(errors_item_data)

            errors.append(errors_item)

        catalog_table = cls(
            name=name,
            label=label,
            icon=icon,
            categories=categories,
            type=type,
            catalog_search_uuid=catalog_search_uuid,
            description=description,
            group_label=group_label,
            required_attributes=required_attributes,
            chart_usage=chart_usage,
            joined_tables=joined_tables,
            tags=tags,
            errors=errors,
        )

        catalog_table.additional_properties = d
        return catalog_table

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
