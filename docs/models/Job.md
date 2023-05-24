# lightdash_client.model.job.Job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**jobStatus** | str,  | str,  |  | must be one of ["STARTED", "DONE", "RUNNING", "ERROR", ]
**jobUuid** | str, uuid.UUID,  | str,  |  | value must be a uuid
**jobType** | str,  | str,  |  | must be one of ["COMPILE_PROJECT", "CREATE_PROJECT", ]
**[steps](#steps)** | list, tuple,  | tuple,  |  |
**updatedAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**projectUuid** | None, str, uuid.UUID,  | NoneClass, str,  |  | [optional] value must be a uuid
**[jobResults](#jobResults)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional]
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# steps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Step**](Step.md) | [**Step**](Step.md) | [**Step**](Step.md) |  |

# jobResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
