# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lightdash_client.paths.org_users import Api
from lightdash_client.paths import PathValues

path = PathValues.ORG_USERS
