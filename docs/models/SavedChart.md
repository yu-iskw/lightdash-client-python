# lightdash_client.model.saved_chart.SavedChart

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**spaceName** | str,  | str,  |  |
**[tableConfig](#tableConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  |
**chartConfig** | [**ChartConfig**](ChartConfig.md) | [**ChartConfig**](ChartConfig.md) |  |
**[metricQuery](#metricQuery)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  |
**spaceUuid** | str,  | str,  |  |
**name** | str,  | str,  |  |
**uuid** | str,  | str,  |  |
**projectUuid** | str,  | str,  |  |
**tableName** | str,  | str,  |  |
**updatedAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**description** | None, str,  | NoneClass, str,  |  | [optional]
**updatedByUser** | [**UpdatedByUser**](UpdatedByUser.md) | [**UpdatedByUser**](UpdatedByUser.md) |  | [optional]
**[pivotConfig](#pivotConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional]
**pinnedListUuid** | str,  | str,  |  | [optional]

# metricQuery

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

# tableConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[columnOrder](#columnOrder)** | list, tuple,  | tuple,  |  |

# columnOrder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  |

# pivotConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[columns](#columns)** | list, tuple,  | tuple,  |  |
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# columns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
