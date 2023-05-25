from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="CreateSavedChartTableConfig")


@attr.s(auto_attribs=True)
class CreateSavedChartTableConfig:
    """
    Attributes:
        column_order (List[str]):
    """

    column_order: List[str]

    def to_dict(self) -> Dict[str, Any]:
        column_order = self.column_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "columnOrder": column_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        column_order = cast(List[str], d.pop("columnOrder"))

        create_saved_chart_table_config = cls(
            column_order=column_order,
        )

        return create_saved_chart_table_config
