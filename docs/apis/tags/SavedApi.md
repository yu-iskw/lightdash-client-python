<a name="__pageTop"></a>
# lightdash_client.apis.tags.saved_api.SavedApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_chart_version**](#create_saved_chart_version) | **post** /saved/{savedChartUuid}/version | Create a new saved chart version
[**delete_saved_chart**](#delete_saved_chart) | **delete** /saved/{savedChartUuid} | Delete a saved chart
[**get_saved_chart**](#get_saved_chart) | **get** /saved/{savedChartUuid} | Get a saved chart
[**patch_saved_chart**](#patch_saved_chart) | **patch** /saved/{savedChartUuid} | Update a saved chart
[**patch_saved_charts**](#patch_saved_charts) | **patch** /projects/{projectUuid}/saved | Update multiple saved charts in project
[**post_saved_chart**](#post_saved_chart) | **post** /projects/{projectUuid}/saved | Create saved chart in project

# **create_saved_chart_version**
<a name="create_saved_chart_version"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_saved_chart_version(saved_chart_uuidcreate_saved_chart_version)

Create a new saved chart version

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
from lightdash_client.model.create_saved_chart_version import CreateSavedChartVersion
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.saved_chart import SavedChart
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'savedChartUuid': "savedChartUuid_example",
    }
    body = CreateSavedChartVersion(
        table_name="table_name_example",
        metric_query=dict(),
        chart_config=ChartConfig(None),
        table_config=dict(
            column_order=[
                "column_order_example"
            ],
        ),
        pivot_config=dict(
,
        ),
    )
    try:
        # Create a new saved chart version
        api_response = api_instance.create_saved_chart_version(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->create_saved_chart_version: %s\n" % e)
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
[**CreateSavedChartVersion**](../../models/CreateSavedChartVersion.md) |  |


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
savedChartUuid | SavedChartUuidSchema | |

# SavedChartUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_saved_chart_version.ApiResponseFor200) | Details for a saved chart
default | [ApiResponseForDefault](#create_saved_chart_version.ApiResponseForDefault) | Error

#### create_saved_chart_version.ApiResponseFor200
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
**results** | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_saved_chart_version.ApiResponseForDefault
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

# **delete_saved_chart**
<a name="delete_saved_chart"></a>
> Success delete_saved_chart(saved_chart_uuid)

Delete a saved chart

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'savedChartUuid': "savedChartUuid_example",
    }
    try:
        # Delete a saved chart
        api_response = api_instance.delete_saved_chart(
            path_params=path_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->delete_saved_chart: %s\n" % e)
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
savedChartUuid | SavedChartUuidSchema | |

# SavedChartUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_saved_chart.ApiResponseFor200) | Acknowledge success
default | [ApiResponseForDefault](#delete_saved_chart.ApiResponseForDefault) | Error

#### delete_saved_chart.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Success**](../../models/Success.md) |  |


#### delete_saved_chart.ApiResponseForDefault
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

# **get_saved_chart**
<a name="get_saved_chart"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_saved_chart(saved_chart_uuid)

Get a saved chart

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.saved_chart import SavedChart
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'savedChartUuid': "savedChartUuid_example",
    }
    try:
        # Get a saved chart
        api_response = api_instance.get_saved_chart(
            path_params=path_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->get_saved_chart: %s\n" % e)
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
savedChartUuid | SavedChartUuidSchema | |

# SavedChartUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_saved_chart.ApiResponseFor200) | Details for a saved chart
default | [ApiResponseForDefault](#get_saved_chart.ApiResponseForDefault) | Error

#### get_saved_chart.ApiResponseFor200
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
**results** | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_saved_chart.ApiResponseForDefault
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

# **patch_saved_chart**
<a name="patch_saved_chart"></a>
> bool, date, datetime, dict, float, int, list, str, none_type patch_saved_chart(saved_chart_uuidupdate_saved_chart)

Update a saved chart

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.saved_chart import SavedChart
from lightdash_client.model.update_saved_chart import UpdateSavedChart
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'savedChartUuid': "savedChartUuid_example",
    }
    body = UpdateSavedChart(
        name="name_example",
        description="description_example",
        space_uuid="space_uuid_example",
    )
    try:
        # Update a saved chart
        api_response = api_instance.patch_saved_chart(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->patch_saved_chart: %s\n" % e)
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
[**UpdateSavedChart**](../../models/UpdateSavedChart.md) |  |


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
savedChartUuid | SavedChartUuidSchema | |

# SavedChartUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_saved_chart.ApiResponseFor200) | Details for a saved chart
default | [ApiResponseForDefault](#patch_saved_chart.ApiResponseForDefault) | Error

#### patch_saved_chart.ApiResponseFor200
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
**results** | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### patch_saved_chart.ApiResponseForDefault
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

# **patch_saved_charts**
<a name="patch_saved_charts"></a>
> bool, date, datetime, dict, float, int, list, str, none_type patch_saved_charts(project_uuid)

Update multiple saved charts in project

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
from lightdash_client.model.update_multiple_saved_chart import UpdateMultipleSavedChart
from lightdash_client.model.error import Error
from lightdash_client.model.success import Success
from lightdash_client.model.saved_chart import SavedChart
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    try:
        # Update multiple saved charts in project
        api_response = api_instance.patch_saved_charts(
            path_params=path_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->patch_saved_charts: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    body = [
        UpdateMultipleSavedChart(
            uuid="uuid_example",
            name="name_example",
            description="description_example",
            space_uuid="space_uuid_example",
        )
    ]
    try:
        # Update multiple saved charts in project
        api_response = api_instance.patch_saved_charts(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->patch_saved_charts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateMultipleSavedChart**]({{complexTypePrefix}}UpdateMultipleSavedChart.md) | [**UpdateMultipleSavedChart**]({{complexTypePrefix}}UpdateMultipleSavedChart.md) | [**UpdateMultipleSavedChart**]({{complexTypePrefix}}UpdateMultipleSavedChart.md) |  |

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
200 | [ApiResponseFor200](#patch_saved_charts.ApiResponseFor200) | Details for saved charts
default | [ApiResponseForDefault](#patch_saved_charts.ApiResponseForDefault) | Error

#### patch_saved_charts.ApiResponseFor200
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
[**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) |  |

#### patch_saved_charts.ApiResponseForDefault
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

# **post_saved_chart**
<a name="post_saved_chart"></a>
> bool, date, datetime, dict, float, int, list, str, none_type post_saved_chart(project_uuid)

Create saved chart in project

### Example

* Api Key Authentication (cookieAuth):
```python
import lightdash_client
from lightdash_client.apis.tags import saved_api
from lightdash_client.model.error import Error
from lightdash_client.model.create_saved_chart import CreateSavedChart
from lightdash_client.model.success import Success
from lightdash_client.model.saved_chart import SavedChart
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
    api_instance = saved_api.SavedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
    }
    try:
        # Create saved chart in project
        api_response = api_instance.post_saved_chart(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->post_saved_chart: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectUuid': "projectUuid_example",
    }
    query_params = {
        'duplicateFrom': "duplicateFrom_example",
    }
    body = CreateSavedChart(
        name="name_example",
        description="description_example",
        table_name="table_name_example",
        metric_query=dict(),
        chart_config=ChartConfig(None),
        table_config=dict(
            column_order=[
                "column_order_example"
            ],
        ),
        pivot_config=dict(
,
        ),
    )
    try:
        # Create saved chart in project
        api_response = api_instance.post_saved_chart(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except lightdash_client.ApiException as e:
        print("Exception when calling SavedApi->post_saved_chart: %s\n" % e)
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
[**CreateSavedChart**](../../models/CreateSavedChart.md) |  |


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
200 | [ApiResponseFor200](#post_saved_chart.ApiResponseFor200) | Details for a saved chart
default | [ApiResponseForDefault](#post_saved_chart.ApiResponseForDefault) | Error

#### post_saved_chart.ApiResponseFor200
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
**results** | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) | [**SavedChart**]({{complexTypePrefix}}SavedChart.md) |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### post_saved_chart.ApiResponseForDefault
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
