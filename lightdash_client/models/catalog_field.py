from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_type_field import CatalogTypeField
from ..models.field_type import FieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_icon import CustomIcon
    from ..models.emoji_icon import EmojiIcon
    from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import PickTagNameOrColorOrTagUuidOrYamlReference
    from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray


T = TypeVar("T", bound="CatalogField")


@_attrs_define
class CatalogField:
    """
    Attributes:
        name (str):
        label (str):
        field_type (FieldType):
        table_label (str):
        icon (Union['CustomIcon', 'EmojiIcon', None]):
        categories (List['PickTagNameOrColorOrTagUuidOrYamlReference']):
        table_name (str):
        type (CatalogTypeField):
        catalog_search_uuid (str):
        description (Union[Unset, str]):
        required_attributes (Union[Unset, RecordStringStringOrStringArray]): Construct a type with a set of properties K
            of type T
        chart_usage (Union[Unset, float]):
        tags (Union[Unset, List[str]]):
        table_group_label (Union[Unset, str]):
        basic_type (Union[Unset, str]):
    """

    name: str
    label: str
    field_type: FieldType
    table_label: str
    icon: Union["CustomIcon", "EmojiIcon", None]
    categories: List["PickTagNameOrColorOrTagUuidOrYamlReference"]
    table_name: str
    type: CatalogTypeField
    catalog_search_uuid: str
    description: Union[Unset, str] = UNSET
    required_attributes: Union[Unset, "RecordStringStringOrStringArray"] = UNSET
    chart_usage: Union[Unset, float] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    table_group_label: Union[Unset, str] = UNSET
    basic_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon
        from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import (
            PickTagNameOrColorOrTagUuidOrYamlReference,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray

        name = self.name

        label = self.label

        field_type = self.field_type.value

        table_label = self.table_label

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

        table_name = self.table_name

        type = self.type.value

        catalog_search_uuid = self.catalog_search_uuid

        description = self.description

        required_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.required_attributes, Unset):
            required_attributes = self.required_attributes.to_dict()

        chart_usage = self.chart_usage

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        table_group_label = self.table_group_label

        basic_type = self.basic_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "label": label,
                "fieldType": field_type,
                "tableLabel": table_label,
                "icon": icon,
                "categories": categories,
                "tableName": table_name,
                "type": type,
                "catalogSearchUuid": catalog_search_uuid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if required_attributes is not UNSET:
            field_dict["requiredAttributes"] = required_attributes
        if chart_usage is not UNSET:
            field_dict["chartUsage"] = chart_usage
        if tags is not UNSET:
            field_dict["tags"] = tags
        if table_group_label is not UNSET:
            field_dict["tableGroupLabel"] = table_group_label
        if basic_type is not UNSET:
            field_dict["basicType"] = basic_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_icon import CustomIcon
        from ..models.emoji_icon import EmojiIcon
        from ..models.pick_tag_name_or_color_or_tag_uuid_or_yaml_reference import (
            PickTagNameOrColorOrTagUuidOrYamlReference,
        )
        from ..models.record_string_string_or_string_array import RecordStringStringOrStringArray

        d = src_dict.copy()
        name = d.pop("name")

        label = d.pop("label")

        field_type = FieldType(d.pop("fieldType"))

        table_label = d.pop("tableLabel")

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

        table_name = d.pop("tableName")

        type = CatalogTypeField(d.pop("type"))

        catalog_search_uuid = d.pop("catalogSearchUuid")

        description = d.pop("description", UNSET)

        _required_attributes = d.pop("requiredAttributes", UNSET)
        required_attributes: Union[Unset, RecordStringStringOrStringArray]
        if isinstance(_required_attributes, Unset):
            required_attributes = UNSET
        else:
            required_attributes = RecordStringStringOrStringArray.from_dict(_required_attributes)

        chart_usage = d.pop("chartUsage", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        table_group_label = d.pop("tableGroupLabel", UNSET)

        basic_type = d.pop("basicType", UNSET)

        catalog_field = cls(
            name=name,
            label=label,
            field_type=field_type,
            table_label=table_label,
            icon=icon,
            categories=categories,
            table_name=table_name,
            type=type,
            catalog_search_uuid=catalog_search_uuid,
            description=description,
            required_attributes=required_attributes,
            chart_usage=chart_usage,
            tags=tags,
            table_group_label=table_group_label,
            basic_type=basic_type,
        )

        catalog_field.additional_properties = d
        return catalog_field

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
