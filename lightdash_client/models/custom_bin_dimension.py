from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bin_type import BinType
from ..models.custom_dimension_type_bin import CustomDimensionTypeBIN
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bin_range import BinRange


T = TypeVar("T", bound="CustomBinDimension")


@_attrs_define
class CustomBinDimension:
    """
    Attributes:
        id (str):
        name (str):
        table (str):
        type (CustomDimensionTypeBIN):
        dimension_id (str):
        bin_type (BinType):
        bin_number (Union[Unset, float]):
        bin_width (Union[Unset, float]):
        custom_range (Union[Unset, List['BinRange']]):
    """

    id: str
    name: str
    table: str
    type: CustomDimensionTypeBIN
    dimension_id: str
    bin_type: BinType
    bin_number: Union[Unset, float] = UNSET
    bin_width: Union[Unset, float] = UNSET
    custom_range: Union[Unset, List["BinRange"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        table = self.table

        type = self.type.value

        dimension_id = self.dimension_id

        bin_type = self.bin_type.value

        bin_number = self.bin_number

        bin_width = self.bin_width

        custom_range: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_range, Unset):
            custom_range = []
            for custom_range_item_data in self.custom_range:
                custom_range_item = custom_range_item_data.to_dict()
                custom_range.append(custom_range_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "table": table,
                "type": type,
                "dimensionId": dimension_id,
                "binType": bin_type,
            }
        )
        if bin_number is not UNSET:
            field_dict["binNumber"] = bin_number
        if bin_width is not UNSET:
            field_dict["binWidth"] = bin_width
        if custom_range is not UNSET:
            field_dict["customRange"] = custom_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bin_range import BinRange

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        table = d.pop("table")

        type = CustomDimensionTypeBIN(d.pop("type"))

        dimension_id = d.pop("dimensionId")

        bin_type = BinType(d.pop("binType"))

        bin_number = d.pop("binNumber", UNSET)

        bin_width = d.pop("binWidth", UNSET)

        custom_range = []
        _custom_range = d.pop("customRange", UNSET)
        for custom_range_item_data in _custom_range or []:
            custom_range_item = BinRange.from_dict(custom_range_item_data)

            custom_range.append(custom_range_item)

        custom_bin_dimension = cls(
            id=id,
            name=name,
            table=table,
            type=type,
            dimension_id=dimension_id,
            bin_type=bin_type,
            bin_number=bin_number,
            bin_width=bin_width,
            custom_range=custom_range,
        )

        custom_bin_dimension.additional_properties = d
        return custom_bin_dimension

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
