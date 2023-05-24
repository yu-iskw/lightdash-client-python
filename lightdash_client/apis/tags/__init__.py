# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lightdash_client.apis.tag_to_api import tag_to_api
import enum


class TagValues(str, enum.Enum):
    USER = "user"
    DASHBOARD = "dashboard"
    JOB = "job"
    ORGANIZATION = "organization"
    PROJECT = "project"
    SAVED = "saved"
    SAVEDCHART = "saved-chart"
