# coding: utf-8
"""
    Lightdash API

    API spec for Lightdash server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightdash.com
    Generated by: https://openapi-generator.tech
"""
from lightdash_client.paths.dashboards_dashboard_uuid.delete import DeleteDashboard
from lightdash_client.paths.dashboards_dashboard_uuid.get import GetDashboard
from lightdash_client.paths.dashboards_dashboard_uuid.patch import PatchDashboard
from lightdash_client.paths.projects_project_uuid_dashboards.get import GetDashboards
from lightdash_client.paths.projects_project_uuid_dashboards.post import CreateDashboard


class DashboardApi(
    CreateDashboard,
    DeleteDashboard,
    GetDashboard,
    GetDashboards,
    PatchDashboard,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
