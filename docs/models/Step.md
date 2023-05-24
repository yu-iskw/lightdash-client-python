# lightdash_client.model.step.Step

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**jobUuid** | str, uuid.UUID,  | str,  |  | value must be a uuid
**stepType** | str,  | str,  |  |
**startedAt** | None, str, datetime,  | NoneClass, str,  |  | value must conform to RFC-3339 date-time
**stepStatus** | str,  | str,  |  | must be one of ["DONE", "RUNNING", "ERROR", "PENDING", "SKIPPED", ]
**stepLabel** | str,  | str,  |  |
**updatedAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**[error](#error)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional]
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional]
**message** | str,  | str,  |  | [optional]
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
