# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lightdash_client.apis.path_to_api import path_to_api
import enum


class PathValues(str, enum.Enum):
    LOGIN = "/login"
    USER = "/user"
    ORG = "/org"
    ORG_USERS = "/org/users"
    ORG_PROJECTS_PROJECT_UUID = "/org/projects/{projectUuid}"
    ORG_PROJECTS = "/org/projects"
    ORG_USERS_USER_UUID = "/org/users/{userUuid}"
    INVITELINKS = "/invite-links"
    INVITELINKS_INVITE_LINK_ID = "/invite-links/{inviteLinkId}"
    PROJECTS_PROJECT_UUID_SQL_QUERY = "/projects/{projectUuid}/sqlQuery"
    PROJECTS_PROJECT_UUID_EXPLORES_TABLE_ID_RUN_QUERY = "/projects/{projectUuid}/explores/{tableId}/runQuery"
    PROJECTS_PROJECT_UUID_CATALOG = "/projects/{projectUuid}/catalog"
    PROJECTS_PROJECT_UUID_DASHBOARDS = "/projects/{projectUuid}/dashboards"
    PROJECTS_PROJECT_UUID_TABLES_CONFIGURATION = "/projects/{projectUuid}/tablesConfiguration"
    PROJECTS_PROJECT_UUID_SAVED = "/projects/{projectUuid}/saved"
    DASHBOARDS_DASHBOARD_UUID = "/dashboards/{dashboardUuid}"
    SAVED_SAVED_CHART_UUID_AVAILABLE_FILTERS = "/saved/{savedChartUuid}/availableFilters"
    SAVED_SAVED_CHART_UUID = "/saved/{savedChartUuid}"
    SAVED_SAVED_CHART_UUID_VERSION = "/saved/{savedChartUuid}/version"
    JOBS_JOB_UUID = "/jobs/{jobUuid}"
    USER_ME_PERSONALACCESSTOKENS = "/user/me/personal-access-tokens"
