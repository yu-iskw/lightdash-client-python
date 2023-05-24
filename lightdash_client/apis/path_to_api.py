import typing_extensions

from lightdash_client.apis.paths.dashboards_dashboard_uuid import DashboardsDashboardUuid
from lightdash_client.apis.paths.invite_links import InviteLinks
from lightdash_client.apis.paths.invite_links_invite_link_id import InviteLinksInviteLinkId
from lightdash_client.apis.paths.jobs_job_uuid import JobsJobUuid
from lightdash_client.apis.paths.login import Login
from lightdash_client.apis.paths.org import Org
from lightdash_client.apis.paths.org_projects import OrgProjects
from lightdash_client.apis.paths.org_projects_project_uuid import OrgProjectsProjectUuid
from lightdash_client.apis.paths.org_users import OrgUsers
from lightdash_client.apis.paths.org_users_user_uuid import OrgUsersUserUuid
from lightdash_client.apis.paths.projects_project_uuid_catalog import ProjectsProjectUuidCatalog
from lightdash_client.apis.paths.projects_project_uuid_dashboards import ProjectsProjectUuidDashboards
from lightdash_client.apis.paths.projects_project_uuid_explores_table_id_run_query import ProjectsProjectUuidExploresTableIdRunQuery
from lightdash_client.apis.paths.projects_project_uuid_saved import ProjectsProjectUuidSaved
from lightdash_client.apis.paths.projects_project_uuid_sql_query import ProjectsProjectUuidSqlQuery
from lightdash_client.apis.paths.projects_project_uuid_tables_configuration import ProjectsProjectUuidTablesConfiguration
from lightdash_client.apis.paths.saved_saved_chart_uuid import SavedSavedChartUuid
from lightdash_client.apis.paths.saved_saved_chart_uuid_available_filters import SavedSavedChartUuidAvailableFilters
from lightdash_client.apis.paths.saved_saved_chart_uuid_version import SavedSavedChartUuidVersion
from lightdash_client.apis.paths.user import User
from lightdash_client.apis.paths.user_me_personal_access_tokens import UserMePersonalAccessTokens
from lightdash_client.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.LOGIN: Login,
        PathValues.USER: User,
        PathValues.ORG: Org,
        PathValues.ORG_USERS: OrgUsers,
        PathValues.ORG_PROJECTS_PROJECT_UUID: OrgProjectsProjectUuid,
        PathValues.ORG_PROJECTS: OrgProjects,
        PathValues.ORG_USERS_USER_UUID: OrgUsersUserUuid,
        PathValues.INVITELINKS: InviteLinks,
        PathValues.INVITELINKS_INVITE_LINK_ID: InviteLinksInviteLinkId,
        PathValues.PROJECTS_PROJECT_UUID_SQL_QUERY: ProjectsProjectUuidSqlQuery,
        PathValues.PROJECTS_PROJECT_UUID_EXPLORES_TABLE_ID_RUN_QUERY: ProjectsProjectUuidExploresTableIdRunQuery,
        PathValues.PROJECTS_PROJECT_UUID_CATALOG: ProjectsProjectUuidCatalog,
        PathValues.PROJECTS_PROJECT_UUID_DASHBOARDS: ProjectsProjectUuidDashboards,
        PathValues.PROJECTS_PROJECT_UUID_TABLES_CONFIGURATION: ProjectsProjectUuidTablesConfiguration,
        PathValues.PROJECTS_PROJECT_UUID_SAVED: ProjectsProjectUuidSaved,
        PathValues.DASHBOARDS_DASHBOARD_UUID: DashboardsDashboardUuid,
        PathValues.SAVED_SAVED_CHART_UUID_AVAILABLE_FILTERS: SavedSavedChartUuidAvailableFilters,
        PathValues.SAVED_SAVED_CHART_UUID: SavedSavedChartUuid,
        PathValues.SAVED_SAVED_CHART_UUID_VERSION: SavedSavedChartUuidVersion,
        PathValues.JOBS_JOB_UUID: JobsJobUuid,
        PathValues.USER_ME_PERSONALACCESSTOKENS: UserMePersonalAccessTokens,
    }
)

path_to_api = PathToApi(
    {
        PathValues.LOGIN: Login,
        PathValues.USER: User,
        PathValues.ORG: Org,
        PathValues.ORG_USERS: OrgUsers,
        PathValues.ORG_PROJECTS_PROJECT_UUID: OrgProjectsProjectUuid,
        PathValues.ORG_PROJECTS: OrgProjects,
        PathValues.ORG_USERS_USER_UUID: OrgUsersUserUuid,
        PathValues.INVITELINKS: InviteLinks,
        PathValues.INVITELINKS_INVITE_LINK_ID: InviteLinksInviteLinkId,
        PathValues.PROJECTS_PROJECT_UUID_SQL_QUERY: ProjectsProjectUuidSqlQuery,
        PathValues.PROJECTS_PROJECT_UUID_EXPLORES_TABLE_ID_RUN_QUERY: ProjectsProjectUuidExploresTableIdRunQuery,
        PathValues.PROJECTS_PROJECT_UUID_CATALOG: ProjectsProjectUuidCatalog,
        PathValues.PROJECTS_PROJECT_UUID_DASHBOARDS: ProjectsProjectUuidDashboards,
        PathValues.PROJECTS_PROJECT_UUID_TABLES_CONFIGURATION: ProjectsProjectUuidTablesConfiguration,
        PathValues.PROJECTS_PROJECT_UUID_SAVED: ProjectsProjectUuidSaved,
        PathValues.DASHBOARDS_DASHBOARD_UUID: DashboardsDashboardUuid,
        PathValues.SAVED_SAVED_CHART_UUID_AVAILABLE_FILTERS: SavedSavedChartUuidAvailableFilters,
        PathValues.SAVED_SAVED_CHART_UUID: SavedSavedChartUuid,
        PathValues.SAVED_SAVED_CHART_UUID_VERSION: SavedSavedChartUuidVersion,
        PathValues.JOBS_JOB_UUID: JobsJobUuid,
        PathValues.USER_ME_PERSONALACCESSTOKENS: UserMePersonalAccessTokens,
    }
)
