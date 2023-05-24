from lightdash_client.paths.dashboards_dashboard_uuid.delete import ApiFordelete
from lightdash_client.paths.dashboards_dashboard_uuid.get import ApiForget
from lightdash_client.paths.dashboards_dashboard_uuid.patch import ApiForpatch


class DashboardsDashboardUuid(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
