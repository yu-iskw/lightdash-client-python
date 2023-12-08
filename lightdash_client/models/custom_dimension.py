from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.bin_type import BinType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bin_range import BinRange


T = TypeVar("T", bound="CustomDimension")


@attr.s(auto_attribs=True)
class CustomDimension:
    """
    Attributes:
        id (str):
        name (str):
        dimension_id (str):
        table (str):
        bin_type (BinType):
        bin_number (Union[Unset, float]):
        bin_width (Union[Unset, float]):
        custom_range (Union[Unset, List['BinRange']]):
    """

    id: str
    name: str
    dimension_id: str
    table: str
    bin_type: BinType
    bin_number: Union[Unset, float] = UNSET
    bin_width: Union[Unset, float] = UNSET
    custom_range: Union[Unset, List["BinRange"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        dimension_id = self.dimension_id
        table = self.table
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
        field_dict.update(
            {
                "id": id,
                "name": name,
                "dimensionId": dimension_id,
                "table": table,
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

        dimension_id = d.pop("dimensionId")

        table = d.pop("table")

        bin_type = BinType(d.pop("binType"))

        bin_number = d.pop("binNumber", UNSET)

        bin_width = d.pop("binWidth", UNSET)

        custom_range = []
        _custom_range = d.pop("customRange", UNSET)
        for custom_range_item_data in _custom_range or []:
            custom_range_item = BinRange.from_dict(custom_range_item_data)

            custom_range.append(custom_range_item)

        custom_dimension = cls(
            id=id,
            name=name,
            dimension_id=dimension_id,
            table=table,
            bin_type=bin_type,
            bin_number=bin_number,
            bin_width=bin_width,
            custom_range=custom_range,
        )

        return custom_dimension
