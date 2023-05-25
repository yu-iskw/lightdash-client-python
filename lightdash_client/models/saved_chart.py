import datetime
from typing import Any
from typing import Dict
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.chart_config import ChartConfig
    from ..models.saved_chart_metric_query import SavedChartMetricQuery
    from ..models.saved_chart_pivot_config import SavedChartPivotConfig
    from ..models.saved_chart_table_config import SavedChartTableConfig
    from ..models.updated_by_user import UpdatedByUser


T = TypeVar("T", bound="SavedChart")


@attr.s(auto_attribs=True)
class SavedChart:
    """
    Attributes:
        uuid (str):
        project_uuid (str):
        name (str):
        table_name (str):
        metric_query (SavedChartMetricQuery):
        chart_config (ChartConfig):
        table_config (SavedChartTableConfig):
        updated_at (datetime.datetime):
        space_uuid (str):
        space_name (str):
        description (Union[Unset, None, str]):
        updated_by_user (Union[Unset, UpdatedByUser]):
        pivot_config (Union[Unset, SavedChartPivotConfig]):
        pinned_list_uuid (Union[Unset, str]):
    """

    uuid: str
    project_uuid: str
    name: str
    table_name: str
    metric_query: "SavedChartMetricQuery"
    chart_config: "ChartConfig"
    table_config: "SavedChartTableConfig"
    updated_at: datetime.datetime
    space_uuid: str
    space_name: str
    description: Union[Unset, None, str] = UNSET
    updated_by_user: Union[Unset, "UpdatedByUser"] = UNSET
    pivot_config: Union[Unset, "SavedChartPivotConfig"] = UNSET
    pinned_list_uuid: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        project_uuid = self.project_uuid
        name = self.name
        table_name = self.table_name
        metric_query = self.metric_query.to_dict()

        chart_config = self.chart_config.to_dict()

        table_config = self.table_config.to_dict()

        updated_at = self.updated_at.isoformat()

        space_uuid = self.space_uuid
        space_name = self.space_name
        description = self.description
        updated_by_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by_user, Unset):
            updated_by_user = self.updated_by_user.to_dict()

        pivot_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pivot_config, Unset):
            pivot_config = self.pivot_config.to_dict()

        pinned_list_uuid = self.pinned_list_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uuid": uuid,
                "projectUuid": project_uuid,
                "name": name,
                "tableName": table_name,
                "metricQuery": metric_query,
                "chartConfig": chart_config,
                "tableConfig": table_config,
                "updatedAt": updated_at,
                "spaceUuid": space_uuid,
                "spaceName": space_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by_user is not UNSET:
            field_dict["updatedByUser"] = updated_by_user
        if pivot_config is not UNSET:
            field_dict["pivotConfig"] = pivot_config
        if pinned_list_uuid is not UNSET:
            field_dict["pinnedListUuid"] = pinned_list_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chart_config import ChartConfig
        from ..models.saved_chart_metric_query import SavedChartMetricQuery
        from ..models.saved_chart_pivot_config import SavedChartPivotConfig
        from ..models.saved_chart_table_config import SavedChartTableConfig
        from ..models.updated_by_user import UpdatedByUser

        d = src_dict.copy()
        uuid = d.pop("uuid")

        project_uuid = d.pop("projectUuid")

        name = d.pop("name")

        table_name = d.pop("tableName")

        metric_query = SavedChartMetricQuery.from_dict(d.pop("metricQuery"))

        chart_config = ChartConfig.from_dict(d.pop("chartConfig"))

        table_config = SavedChartTableConfig.from_dict(d.pop("tableConfig"))

        updated_at = isoparse(d.pop("updatedAt"))

        space_uuid = d.pop("spaceUuid")

        space_name = d.pop("spaceName")

        description = d.pop("description", UNSET)

        _updated_by_user = d.pop("updatedByUser", UNSET)
        updated_by_user: Union[Unset, UpdatedByUser]
        if isinstance(_updated_by_user, Unset):
            updated_by_user = UNSET
        else:
            updated_by_user = UpdatedByUser.from_dict(_updated_by_user)

        _pivot_config = d.pop("pivotConfig", UNSET)
        pivot_config: Union[Unset, SavedChartPivotConfig]
        if isinstance(_pivot_config, Unset):
            pivot_config = UNSET
        else:
            pivot_config = SavedChartPivotConfig.from_dict(_pivot_config)

        pinned_list_uuid = d.pop("pinnedListUuid", UNSET)

        saved_chart = cls(
            uuid=uuid,
            project_uuid=project_uuid,
            name=name,
            table_name=table_name,
            metric_query=metric_query,
            chart_config=chart_config,
            table_config=table_config,
            updated_at=updated_at,
            space_uuid=space_uuid,
            space_name=space_name,
            description=description,
            updated_by_user=updated_by_user,
            pivot_config=pivot_config,
            pinned_list_uuid=pinned_list_uuid,
        )

        return saved_chart
