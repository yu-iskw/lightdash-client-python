import typing_extensions

from lightdash_client.apis.tags import TagValues
from lightdash_client.apis.tags.dashboard_api import DashboardApi
from lightdash_client.apis.tags.job_api import JobApi
from lightdash_client.apis.tags.organization_api import OrganizationApi
from lightdash_client.apis.tags.project_api import ProjectApi
from lightdash_client.apis.tags.saved_api import SavedApi
from lightdash_client.apis.tags.saved_chart_api import SavedChartApi
from lightdash_client.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER: UserApi,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.JOB: JobApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SAVED: SavedApi,
        TagValues.SAVEDCHART: SavedChartApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER: UserApi,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.JOB: JobApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SAVED: SavedApi,
        TagValues.SAVEDCHART: SavedChartApi,
    }
)
