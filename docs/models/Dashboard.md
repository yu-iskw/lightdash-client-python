# lightdash_client.model.dashboard.Dashboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**spaceName** | str,  | str,  |  |
**[tiles](#tiles)** | list, tuple,  | tuple,  |  |
**spaceUuid** | str,  | str,  |  |
**name** | str,  | str,  |  |
**filters** | [**DashboardFilters**](DashboardFilters.md) | [**DashboardFilters**](DashboardFilters.md) |  |
**uuid** | str, uuid.UUID,  | str,  |  | value must be a uuid
**updatedAt** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**description** | None, str,  | NoneClass, str,  |  | [optional]
**updatedByUser** | [**UpdatedByUser**](UpdatedByUser.md) | [**UpdatedByUser**](UpdatedByUser.md) |  | [optional]
**pinnedListUuid** | str,  | str,  |  | [optional]

# tiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  |

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DashboardTile**](DashboardTile.md) | [**DashboardTile**](DashboardTile.md) | [**DashboardTile**](DashboardTile.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
