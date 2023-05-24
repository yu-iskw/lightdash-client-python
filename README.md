# lightdash-client
API spec for Lightdash server

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import lightdash_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lightdash_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import lightdash_client
from pprint import pprint
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.create_dashboard import CreateDashboard
from lightdash_client.model.dashboard import Dashboard
from lightdash_client.model.dashboard_list_item import DashboardListItem
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.update_dashboard import UpdateDashboard
# Defining the host is optional and defaults to http://localhost:8080/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = lightdash_client.Configuration(
    host = "http://localhost:8080/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lightdash_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dashboard_api.DashboardApi(api_client)
    project_uuid = "projectUuid_example" # str |
duplicate_from = "duplicateFrom_example" # str |  (optional)
create_dashboard = CreateDashboard(
        name="name_example",
        description="description_example",
        tiles=[
            CreateDashboardTile(
                uuid="uuid_example",
                type="saved_chart",
                properties=None,
                x=3.14,
                y=3.14,
                h=3.14,
                w=3.14,
            )
        ],
        filters=DashboardFilters(
            dimensions=[
                DashboardFilterRule(
                    id="id_example",
                    target=dict(
                        field_id="field_id_example",
                        table_name="table_name_example",
                    ),
                    operator="operator_example",
null,
                    settings=dict(),
                    label="label_example",
                    tile_targets=dict(
                        tile_uuid=dict(),
                    ),
                )
            ],
,
        ),
    ) # CreateDashboard | New dashboard specification (optional)

    try:
        # Create dashboard
        api_response = api_instance.create_dashboard(project_uuidduplicate_from=duplicate_fromcreate_dashboard=create_dashboard)
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DashboardApi* | [**create_dashboard**](docs/apis/tags/DashboardApi.md#create_dashboard) | **post** /projects/{projectUuid}/dashboards | Create dashboard
*DashboardApi* | [**delete_dashboard**](docs/apis/tags/DashboardApi.md#delete_dashboard) | **delete** /dashboards/{dashboardUuid} | Delete dashboard
*DashboardApi* | [**get_dashboard**](docs/apis/tags/DashboardApi.md#get_dashboard) | **get** /dashboards/{dashboardUuid} | Get dashboard
*DashboardApi* | [**get_dashboards**](docs/apis/tags/DashboardApi.md#get_dashboards) | **get** /projects/{projectUuid}/dashboards | List dashboards
*DashboardApi* | [**patch_dashboard**](docs/apis/tags/DashboardApi.md#patch_dashboard) | **patch** /dashboards/{dashboardUuid} | Update dashboard
*JobApi* | [**get_job**](docs/apis/tags/JobApi.md#get_job) | **get** /jobs/{jobUuid} | List status of a job
*OrganizationApi* | [**delete_organization_project**](docs/apis/tags/OrganizationApi.md#delete_organization_project) | **delete** /org/projects/{projectUuid} | Delete organization project
*OrganizationApi* | [**delete_organization_user**](docs/apis/tags/OrganizationApi.md#delete_organization_user) | **delete** /org/users/{userUuid} | Delete organization user
*OrganizationApi* | [**get_organization_projects**](docs/apis/tags/OrganizationApi.md#get_organization_projects) | **get** /org/projects | List organization projects
*OrganizationApi* | [**get_organization_users**](docs/apis/tags/OrganizationApi.md#get_organization_users) | **get** /org/users | Get organization users
*OrganizationApi* | [**update_organization**](docs/apis/tags/OrganizationApi.md#update_organization) | **patch** /org | Update organization
*OrganizationApi* | [**update_organization_member**](docs/apis/tags/OrganizationApi.md#update_organization_member) | **patch** /org/users/{userUuid} | Update organization member
*ProjectApi* | [**delete_organization_project**](docs/apis/tags/ProjectApi.md#delete_organization_project) | **delete** /org/projects/{projectUuid} | Delete organization project
*ProjectApi* | [**get_organization_projects**](docs/apis/tags/ProjectApi.md#get_organization_projects) | **get** /org/projects | List organization projects
*ProjectApi* | [**get_project_catalog**](docs/apis/tags/ProjectApi.md#get_project_catalog) | **get** /projects/{projectUuid}/catalog | Get project catalog
*ProjectApi* | [**get_project_tables_configuration**](docs/apis/tags/ProjectApi.md#get_project_tables_configuration) | **get** /projects/{projectUuid}/tablesConfiguration | Get project tables configuration
*ProjectApi* | [**run_query**](docs/apis/tags/ProjectApi.md#run_query) | **post** /projects/{projectUuid}/explores/{tableId}/runQuery | Run query
*ProjectApi* | [**run_sql_query**](docs/apis/tags/ProjectApi.md#run_sql_query) | **post** /projects/{projectUuid}/sqlQuery | Run sql query
*ProjectApi* | [**update_project_tables_configuration**](docs/apis/tags/ProjectApi.md#update_project_tables_configuration) | **patch** /projects/{projectUuid}/tablesConfiguration | Update project tables configuration
*SavedApi* | [**create_saved_chart_version**](docs/apis/tags/SavedApi.md#create_saved_chart_version) | **post** /saved/{savedChartUuid}/version | Create a new saved chart version
*SavedApi* | [**delete_saved_chart**](docs/apis/tags/SavedApi.md#delete_saved_chart) | **delete** /saved/{savedChartUuid} | Delete a saved chart
*SavedApi* | [**get_saved_chart**](docs/apis/tags/SavedApi.md#get_saved_chart) | **get** /saved/{savedChartUuid} | Get a saved chart
*SavedApi* | [**patch_saved_chart**](docs/apis/tags/SavedApi.md#patch_saved_chart) | **patch** /saved/{savedChartUuid} | Update a saved chart
*SavedApi* | [**patch_saved_charts**](docs/apis/tags/SavedApi.md#patch_saved_charts) | **patch** /projects/{projectUuid}/saved | Update multiple saved charts in project
*SavedApi* | [**post_saved_chart**](docs/apis/tags/SavedApi.md#post_saved_chart) | **post** /projects/{projectUuid}/saved | Create saved chart in project
*SavedChartApi* | [**get_available_chart_filters**](docs/apis/tags/SavedChartApi.md#get_available_chart_filters) | **get** /saved/{savedChartUuid}/availableFilters | Get available filters for a saved chart
*UserApi* | [**create_invite_link**](docs/apis/tags/UserApi.md#create_invite_link) | **post** /invite-links | Create a new invite link
*UserApi* | [**create_personal_access_token**](docs/apis/tags/UserApi.md#create_personal_access_token) | **post** /user/me/personal-access-tokens | Create a personal access token
*UserApi* | [**create_user**](docs/apis/tags/UserApi.md#create_user) | **post** /user | Create user
*UserApi* | [**delete_invite_links**](docs/apis/tags/UserApi.md#delete_invite_links) | **delete** /invite-links | Delete all invite links
*UserApi* | [**get_invite_link**](docs/apis/tags/UserApi.md#get_invite_link) | **get** /invite-links/{inviteLinkId} | Get an invite link
*UserApi* | [**get_personal_access_tokens**](docs/apis/tags/UserApi.md#get_personal_access_tokens) | **get** /user/me/personal-access-tokens | Get all personal access tokens
*UserApi* | [**get_user**](docs/apis/tags/UserApi.md#get_user) | **get** /user | Get user profile
*UserApi* | [**login_with_password**](docs/apis/tags/UserApi.md#login_with_password) | **post** /login | Login with email and password

## Documentation For Models

 - [ChartConfig](docs/models/ChartConfig.md)
 - [CreateDashboard](docs/models/CreateDashboard.md)
 - [CreateDashboardTile](docs/models/CreateDashboardTile.md)
 - [CreateInviteLink](docs/models/CreateInviteLink.md)
 - [CreatePersonalAccessToken](docs/models/CreatePersonalAccessToken.md)
 - [CreateSavedChart](docs/models/CreateSavedChart.md)
 - [CreateSavedChartVersion](docs/models/CreateSavedChartVersion.md)
 - [CreateUser](docs/models/CreateUser.md)
 - [Dashboard](docs/models/Dashboard.md)
 - [DashboardFilterRule](docs/models/DashboardFilterRule.md)
 - [DashboardFilters](docs/models/DashboardFilters.md)
 - [DashboardListItem](docs/models/DashboardListItem.md)
 - [DashboardTile](docs/models/DashboardTile.md)
 - [Error](docs/models/Error.md)
 - [Field](docs/models/Field.md)
 - [Fields](docs/models/Fields.md)
 - [InviteLink](docs/models/InviteLink.md)
 - [Job](docs/models/Job.md)
 - [LightdashUser](docs/models/LightdashUser.md)
 - [Login](docs/models/Login.md)
 - [LoomTileProperties](docs/models/LoomTileProperties.md)
 - [MarkdownTileProperties](docs/models/MarkdownTileProperties.md)
 - [OrganizationUser](docs/models/OrganizationUser.md)
 - [PersonalAccessToken](docs/models/PersonalAccessToken.md)
 - [PersonalAccessTokenWithSecret](docs/models/PersonalAccessTokenWithSecret.md)
 - [Project](docs/models/Project.md)
 - [ProjectCatalog](docs/models/ProjectCatalog.md)
 - [ProjectTablesConfiguration](docs/models/ProjectTablesConfiguration.md)
 - [QueryResult](docs/models/QueryResult.md)
 - [SavedChart](docs/models/SavedChart.md)
 - [Step](docs/models/Step.md)
 - [Success](docs/models/Success.md)
 - [TilePropertiesChart](docs/models/TilePropertiesChart.md)
 - [UpdateDashboard](docs/models/UpdateDashboard.md)
 - [UpdateMultipleSavedChart](docs/models/UpdateMultipleSavedChart.md)
 - [UpdateSavedChart](docs/models/UpdateSavedChart.md)
 - [UpdatedByUser](docs/models/UpdatedByUser.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## cookieAuth

- **Type**: API key
- **API key parameter name**: connect.sid
- **Location**:


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in lightdash_client.apis and lightdash_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from lightdash_client.apis.default_api import DefaultApi`
- `from lightdash_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import lightdash_client
from lightdash_client.apis import *
from lightdash_client.models import *
```
