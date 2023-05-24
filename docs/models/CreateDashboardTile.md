# lightdash_client.model.create_dashboard_tile.CreateDashboardTile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**w** | decimal.Decimal, int, float,  | decimal.Decimal,  |  |
**h** | decimal.Decimal, int, float,  | decimal.Decimal,  |  |
**x** | decimal.Decimal, int, float,  | decimal.Decimal,  |  |
**y** | decimal.Decimal, int, float,  | decimal.Decimal,  |  |
**type** | str,  | str,  |  | must be one of ["saved_chart", "markdown", "loom", ]
**[properties](#properties)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |
**uuid** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  |

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TilePropertiesChart](TilePropertiesChart.md) | [**TilePropertiesChart**](TilePropertiesChart.md) | [**TilePropertiesChart**](TilePropertiesChart.md) |  |
[LoomTileProperties](LoomTileProperties.md) | [**LoomTileProperties**](LoomTileProperties.md) | [**LoomTileProperties**](LoomTileProperties.md) |  |
[MarkdownTileProperties](MarkdownTileProperties.md) | [**MarkdownTileProperties**](MarkdownTileProperties.md) | [**MarkdownTileProperties**](MarkdownTileProperties.md) |  |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
