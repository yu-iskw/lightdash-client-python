from lightdash_client.paths.saved_saved_chart_uuid.delete import ApiFordelete
from lightdash_client.paths.saved_saved_chart_uuid.get import ApiForget
from lightdash_client.paths.saved_saved_chart_uuid.patch import ApiForpatch


class SavedSavedChartUuid(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
