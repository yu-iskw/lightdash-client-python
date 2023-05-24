# coding: utf-8
"""


    Generated by: https://openapi-generator.tech
"""
import unittest
from unittest.mock import patch

import urllib3

import lightdash_client
from .. import ApiTestMixin
from lightdash_client import api_client
from lightdash_client import configuration
from lightdash_client import schemas
from lightdash_client.paths.projects_project_uuid_dashboards import get  # noqa: E501


class TestProjectsProjectUuidDashboards(ApiTestMixin, unittest.TestCase):
    """
    ProjectsProjectUuidDashboards unit test stubs
        List dashboards  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
