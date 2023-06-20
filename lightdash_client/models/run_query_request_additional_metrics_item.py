from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar
from typing import Union

import attr

from ..models.run_query_request_additional_metrics_item_compact_type_0 import (
    RunQueryRequestAdditionalMetricsItemCompactType0,
)
from ..models.run_query_request_additional_metrics_item_compact_type_1 import (
    RunQueryRequestAdditionalMetricsItemCompactType1,
)
from ..models.run_query_request_additional_metrics_item_type import RunQueryRequestAdditionalMetricsItemType
from ..types import UNSET
from ..types import Unset

T = TypeVar("T", bound="RunQueryRequestAdditionalMetricsItem")


@attr.s(auto_attribs=True)
class RunQueryRequestAdditionalMetricsItem:
    """
    Attributes:
        type (RunQueryRequestAdditionalMetricsItemType):
        sql (str):
        table (str):
        name (str):
        label (Union[Unset, str]):
        description (Union[Unset, str]):
        hidden (Union[Unset, bool]):
        round_ (Union[Unset, float]):
        compact (Union[RunQueryRequestAdditionalMetricsItemCompactType0,
            RunQueryRequestAdditionalMetricsItemCompactType1, Unset]):
        format_ (Union[Unset, str]):
        index (Union[Unset, float]):
    """

    type: RunQueryRequestAdditionalMetricsItemType
    sql: str
    table: str
    name: str
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    round_: Union[Unset, float] = UNSET
    compact: Union[
        RunQueryRequestAdditionalMetricsItemCompactType0, RunQueryRequestAdditionalMetricsItemCompactType1, Unset
    ] = UNSET
    format_: Union[Unset, str] = UNSET
    index: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        sql = self.sql
        table = self.table
        name = self.name
        label = self.label
        description = self.description
        hidden = self.hidden
        round_ = self.round_
        compact: Union[Unset, str]
        if isinstance(self.compact, Unset):
            compact = UNSET

        elif isinstance(self.compact, RunQueryRequestAdditionalMetricsItemCompactType0):
            compact = UNSET
            if not isinstance(self.compact, Unset):
                compact = self.compact.value

        else:
            compact = UNSET
            if not isinstance(self.compact, Unset):
                compact = self.compact.value

        format_ = self.format_
        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "sql": sql,
                "table": table,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if round_ is not UNSET:
            field_dict["round"] = round_
        if compact is not UNSET:
            field_dict["compact"] = compact
        if format_ is not UNSET:
            field_dict["format"] = format_
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RunQueryRequestAdditionalMetricsItemType(d.pop("type"))

        sql = d.pop("sql")

        table = d.pop("table")

        name = d.pop("name")

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        round_ = d.pop("round", UNSET)

        def _parse_compact(
            data: object,
        ) -> Union[
            RunQueryRequestAdditionalMetricsItemCompactType0, RunQueryRequestAdditionalMetricsItemCompactType1, Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _compact_type_0 = data
                compact_type_0: Union[Unset, RunQueryRequestAdditionalMetricsItemCompactType0]
                if isinstance(_compact_type_0, Unset):
                    compact_type_0 = UNSET
                else:
                    compact_type_0 = RunQueryRequestAdditionalMetricsItemCompactType0(_compact_type_0)

                return compact_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _compact_type_1 = data
            compact_type_1: Union[Unset, RunQueryRequestAdditionalMetricsItemCompactType1]
            if isinstance(_compact_type_1, Unset):
                compact_type_1 = UNSET
            else:
                compact_type_1 = RunQueryRequestAdditionalMetricsItemCompactType1(_compact_type_1)

            return compact_type_1

        compact = _parse_compact(d.pop("compact", UNSET))

        format_ = d.pop("format", UNSET)

        index = d.pop("index", UNSET)

        run_query_request_additional_metrics_item = cls(
            type=type,
            sql=sql,
            table=table,
            name=name,
            label=label,
            description=description,
            hidden=hidden,
            round_=round_,
            compact=compact,
            format_=format_,
            index=index,
        )

        return run_query_request_additional_metrics_item
