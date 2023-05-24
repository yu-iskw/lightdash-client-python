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


class ChartConfig(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:

        class properties:


            class chartType(
                schemas.EnumBase,
                schemas.StrSchema
            ):


                class MetaOapg:
                    enum_value_to_name = {
                        "big_number": "BIG_NUMBER",
                        "table": "TABLE",
                        "cartesian": "CARTESIAN",
                    }

                @schemas.classproperty
                def BIG_NUMBER(cls):
                    return cls("big_number")

                @schemas.classproperty
                def TABLE(cls):
                    return cls("table")

                @schemas.classproperty
                def CARTESIAN(cls):
                    return cls("cartesian")


            class config(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):


                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema


                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)

                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)

                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                ) -> 'config':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "chartType": chartType,
                "config": config,
            }


    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chartType"]) -> MetaOapg.properties.chartType: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chartType", "config", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)


    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chartType"]) -> typing.Union[MetaOapg.properties.chartType, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chartType", "config", ], str]):
        return super().get_item_oapg(name)


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        chartType: typing.Union[MetaOapg.properties.chartType, str, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChartConfig':
        return super().__new__(
            cls,
            *_args,
            chartType=chartType,
            config=config,
            _configuration=_configuration,
            **kwargs,
        )
