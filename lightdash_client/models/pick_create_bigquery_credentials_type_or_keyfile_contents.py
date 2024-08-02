from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_types_bigquery import WarehouseTypesBIGQUERY

if TYPE_CHECKING:
    from ..models.record_string_string import RecordStringString


T = TypeVar("T", bound="PickCreateBigqueryCredentialsTypeOrKeyfileContents")


@_attrs_define
class PickCreateBigqueryCredentialsTypeOrKeyfileContents:
    """From T, pick a set of properties whose keys are in the union K

    Attributes:
        type (WarehouseTypesBIGQUERY):
        keyfile_contents (RecordStringString): Construct a type with a set of properties K of type T
    """

    type: WarehouseTypesBIGQUERY
    keyfile_contents: "RecordStringString"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        keyfile_contents = self.keyfile_contents.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "keyfileContents": keyfile_contents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_string_string import RecordStringString

        d = src_dict.copy()
        type = WarehouseTypesBIGQUERY(d.pop("type"))

        keyfile_contents = RecordStringString.from_dict(d.pop("keyfileContents"))

        pick_create_bigquery_credentials_type_or_keyfile_contents = cls(
            type=type,
            keyfile_contents=keyfile_contents,
        )

        pick_create_bigquery_credentials_type_or_keyfile_contents.additional_properties = d
        return pick_create_bigquery_credentials_type_or_keyfile_contents

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
