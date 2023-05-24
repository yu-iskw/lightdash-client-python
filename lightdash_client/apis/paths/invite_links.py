from lightdash_client.paths.invite_links.delete import ApiFordelete
from lightdash_client.paths.invite_links.post import ApiForpost


class InviteLinks(
    ApiForpost,
    ApiFordelete,
):
    pass
