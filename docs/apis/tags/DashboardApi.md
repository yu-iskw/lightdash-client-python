<a name="__pageTop"></a>
# lightdash_client.apis.tags.dashboard_api.DashboardApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](#create_dashboard) | **post** /projects/{projectUuid}/dashboards | Create dashboard
[**delete_dashboard**](#delete_dashboard) | **delete** /dashboards/{dashboardUuid} | Delete dashboard
[**get_dashboard**](#get_dashboard) | **get** /dashboards/{dashboardUuid} | Get dashboard
[**get_dashboards**](#get_dashboards) | **get** /projects/{projectUuid}/dashboards | List dashboards
[**patch_dashboard**](#patch_dashboard) | **patch** /dashboards/{dashboardUuid} | Update dashboard

# **create_dashboard**
<a name="create_dashboard"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_dashboard(project_uuid)

Create dashboard

Create new dashboard on project

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.create_dashboard import CreateDashboard
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.dashboard import Dashboard
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
    }
    try:
        # Create dashboard
        api_response = api_instance.create_dashboard(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
        'duplicateFrom': "duplicateFrom_example",
    }
    body = CreateDashboard(
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
    )
    try:
        # Create dashboard
        api_response = api_instance.create_dashboard(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDashboard**](../../models/CreateDashboard.md) |  |


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
duplicateFrom | DuplicateFromSchema | | optional


# DuplicateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUuid | ProjectUuidSchema | |

# ProjectUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_dashboard.ApiResponseFor201) | Successfully created dashboard
default | [ApiResponseForDefault](#create_dashboard.ApiResponseForDefault) | Error

#### create_dashboard.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Success]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) |  |
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**results** | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_dashboard.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  |


### Authorization

[cookieAuth](../../../README.md#cookieAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_dashboard**
<a name="delete_dashboard"></a>
> Success delete_dashboard(dashboard_uuid)

Delete dashboard

Delete a single dashboard by dashboard_id

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    path_params = {
        'dashboardUuid': "dashboardUuid_example",
    }
    try:
        # Delete dashboard
        api_response = api_instance.delete_dashboard(
            path_params=path_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dashboardUuid | DashboardUuidSchema | |

# DashboardUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_dashboard.ApiResponseFor200) | Success
default | [ApiResponseForDefault](#delete_dashboard.ApiResponseForDefault) | Error

#### delete_dashboard.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Success**](../../models/Success.md) |  |


#### delete_dashboard.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  |


### Authorization

[cookieAuth](../../../README.md#cookieAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_dashboard**
<a name="get_dashboard"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_dashboard(dashboard_uuid)

Get dashboard

Get details for a single dashboard by dashboard_id

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.dashboard import Dashboard
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    path_params = {
        'dashboardUuid': "dashboardUuid_example",
    }
    try:
        # Get dashboard
        api_response = api_instance.get_dashboard(
            path_params=path_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dashboardUuid | DashboardUuidSchema | |

# DashboardUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dashboard.ApiResponseFor200) | Details for a single dashboard
default | [ApiResponseForDefault](#get_dashboard.ApiResponseForDefault) | Error

#### get_dashboard.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Success]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) |  |
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**results** | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_dashboard.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  |


### Authorization

[cookieAuth](../../../README.md#cookieAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_dashboards**
<a name="get_dashboards"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_dashboards(project_uuid)

List dashboards

List all dashboards in a project

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.dashboard_list_item import DashboardListItem
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
    }
    try:
        # List dashboards
        api_response = api_instance.get_dashboards(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->get_dashboards: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
        'chartUuid': "chartUuid_example",
    }
    try:
        # List dashboards
        api_response = api_instance.get_dashboards(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->get_dashboards: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
chartUuid | ChartUuidSchema | | optional


# ChartUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectUuid | ProjectUuidSchema | |

# ProjectUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dashboards.ApiResponseFor200) | List of all dashboards in project
default | [ApiResponseForDefault](#get_dashboards.ApiResponseForDefault) | Error

#### get_dashboards.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Success]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) |  |
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[results](#results)** | list, tuple,  | tuple,  |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DashboardListItem**]({{complexTypePrefix}}DashboardListItem.md) | [**DashboardListItem**]({{complexTypePrefix}}DashboardListItem.md) | [**DashboardListItem**]({{complexTypePrefix}}DashboardListItem.md) |  |

#### get_dashboards.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  |


### Authorization

[cookieAuth](../../../README.md#cookieAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_dashboard**
<a name="patch_dashboard"></a>
> bool, date, datetime, dict, float, int, list, str, none_type patch_dashboard(dashboard_uuidupdate_dashboard)

Update dashboard

Update details for a single dashboard by dashboard_id

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import dashboard_api
from lightdash_client.model.update_dashboard import UpdateDashboard
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.dashboard import Dashboard
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    path_params = {
        'dashboardUuid': "dashboardUuid_example",
    }
    body = UpdateDashboard(None)
    try:
        # Update dashboard
        api_response = api_instance.patch_dashboard(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling DashboardApi->patch_dashboard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateDashboard**](../../models/UpdateDashboard.md) |  |


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dashboardUuid | DashboardUuidSchema | |

# DashboardUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_dashboard.ApiResponseFor200) | Details for a single dashboard
default | [ApiResponseForDefault](#patch_dashboard.ApiResponseForDefault) | Error

#### patch_dashboard.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Success]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) | [**Success**]({{complexTypePrefix}}Success.md) |  |
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**results** | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) | [**Dashboard**]({{complexTypePrefix}}Dashboard.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### patch_dashboard.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  |


### Authorization

[cookieAuth](../../../README.md#cookieAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
