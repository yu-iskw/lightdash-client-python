# lightdash_client.model.update_dashboard.UpdateDashboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  |
[one_of_1](#one_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  |
[one_of_2](#one_of_2) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional]
**description** | None, str,  | NoneClass, str,  |  | [optional]
**spaceUuid** | None, str,  | NoneClass, str,  |  | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tiles](#tiles)** | list, tuple,  | tuple,  |  |
**filters** | [**DashboardFilters**](DashboardFilters.md) | [**DashboardFilters**](DashboardFilters.md) |  |

# tiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreateDashboardTile**](CreateDashboardTile.md) | [**CreateDashboardTile**](CreateDashboardTile.md) | [**CreateDashboardTile**](CreateDashboardTile.md) |  |

# one_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tiles](#tiles)** | list, tuple,  | tuple,  |  |
**name** | str,  | str,  |  |
**filters** | [**DashboardFilters**](DashboardFilters.md) | [**DashboardFilters**](DashboardFilters.md) |  |
**description** | None, str,  | NoneClass, str,  |  | [optional]

# tiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreateDashboardTile**](CreateDashboardTile.md) | [**CreateDashboardTile**](CreateDashboardTile.md) | [**CreateDashboardTile**](CreateDashboardTile.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
