# coding: utf-8
"""
    Lightdash API

    API spec for Lightdash server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightdash.com
    Generated by: https://openapi-generator.tech
"""
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date
from datetime import datetime

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401

from lightdash_client import schemas  # noqa: F401


class CreateSavedChartVersion(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tableConfig",
            "chartConfig",
            "metricQuery",
            "tableName",
        }

        class properties:
            tableName = schemas.StrSchema
            metricQuery = schemas.DictSchema

            @staticmethod
            def chartConfig() -> typing.Type['ChartConfig']:
                return ChartConfig


            class tableConfig(
                schemas.DictSchema
            ):


                class MetaOapg:
                    required = {
                        "columnOrder",
                    }

                    class properties:


                        class columnOrder(
                            schemas.ListSchema
                        ):


                            class MetaOapg:
                                items = schemas.StrSchema

                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'columnOrder':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )

                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "columnOrder": columnOrder,
                        }
                    additional_properties = schemas.NotAnyTypeSchema

                columnOrder: MetaOapg.properties.columnOrder

                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["columnOrder"]) -> MetaOapg.properties.columnOrder: ...

                def __getitem__(self, name: typing.Union[typing_extensions.Literal["columnOrder"], ]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)

                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["columnOrder"]) -> MetaOapg.properties.columnOrder: ...

                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columnOrder"], ]):
                    return super().get_item_oapg(name)

                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    columnOrder: typing.Union[MetaOapg.properties.columnOrder, list, tuple, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tableConfig':
                    return super().__new__(
                        cls,
                        *_args,
                        columnOrder=columnOrder,
                        _configuration=_configuration,
                    )


            class pivotConfig(
                schemas.DictSchema
            ):


                class MetaOapg:
                    required = {
                        "columns",
                    }

                    class properties:


                        class columns(
                            schemas.ListSchema
                        ):


                            class MetaOapg:
                                items = schemas.StrSchema

                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'columns':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )

                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "columns": columns,
                        }

                columns: MetaOapg.properties.columns

                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...

                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

                def __getitem__(self, name: typing.Union[typing_extensions.Literal["columns", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)


                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...

                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columns", ], str]):
                    return super().get_item_oapg(name)


                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    columns: typing.Union[MetaOapg.properties.columns, list, tuple, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'pivotConfig':
                    return super().__new__(
                        cls,
                        *_args,
                        columns=columns,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "tableName": tableName,
                "metricQuery": metricQuery,
                "chartConfig": chartConfig,
                "tableConfig": tableConfig,
                "pivotConfig": pivotConfig,
            }
        additional_properties = schemas.NotAnyTypeSchema

    tableConfig: MetaOapg.properties.tableConfig
    chartConfig: 'ChartConfig'
    metricQuery: MetaOapg.properties.metricQuery
    tableName: MetaOapg.properties.tableName

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tableConfig"]) -> MetaOapg.properties.tableConfig: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chartConfig"]) -> 'ChartConfig': ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metricQuery"]) -> MetaOapg.properties.metricQuery: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pivotConfig"]) -> MetaOapg.properties.pivotConfig: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tableConfig"], typing_extensions.Literal["chartConfig"], typing_extensions.Literal["metricQuery"], typing_extensions.Literal["tableName"], typing_extensions.Literal["pivotConfig"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tableConfig"]) -> MetaOapg.properties.tableConfig: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chartConfig"]) -> 'ChartConfig': ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metricQuery"]) -> MetaOapg.properties.metricQuery: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pivotConfig"]) -> typing.Union[MetaOapg.properties.pivotConfig, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tableConfig"], typing_extensions.Literal["chartConfig"], typing_extensions.Literal["metricQuery"], typing_extensions.Literal["tableName"], typing_extensions.Literal["pivotConfig"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tableConfig: typing.Union[MetaOapg.properties.tableConfig, dict, frozendict.frozendict, ],
        chartConfig: 'ChartConfig',
        metricQuery: typing.Union[MetaOapg.properties.metricQuery, dict, frozendict.frozendict, ],
        tableName: typing.Union[MetaOapg.properties.tableName, str, ],
        pivotConfig: typing.Union[MetaOapg.properties.pivotConfig, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreateSavedChartVersion':
        return super().__new__(
            cls,
            *_args,
            tableConfig=tableConfig,
            chartConfig=chartConfig,
            metricQuery=metricQuery,
            tableName=tableName,
            pivotConfig=pivotConfig,
            _configuration=_configuration,
        )

from lightdash_client.model.chart_config import ChartConfig
