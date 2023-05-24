# coding: utf-8

"""
    Lightdash API

    API spec for Lightdash server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightdash.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lightdash_client import schemas  # noqa: F401


class QueryResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:


        class additional_properties(
            schemas.DictSchema
        ):


            class MetaOapg:

                class properties:


                    class value(
                        schemas.DictSchema
                    ):


                        class MetaOapg:

                            class properties:
                                raw = schemas.AnyTypeSchema
                                formatted = schemas.AnyTypeSchema
                                __annotations__ = {
                                    "raw": raw,
                                    "formatted": formatted,
                                }

                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["raw"]) -> MetaOapg.properties.raw: ...

                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["formatted"]) -> MetaOapg.properties.formatted: ...

                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["raw", "formatted", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)


                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union[MetaOapg.properties.raw, schemas.Unset]: ...

                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["formatted"]) -> typing.Union[MetaOapg.properties.formatted, schemas.Unset]: ...

                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["raw", "formatted", ], str]):
                            return super().get_item_oapg(name)


                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            raw: typing.Union[MetaOapg.properties.raw, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                            formatted: typing.Union[MetaOapg.properties.formatted, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'value':
                            return super().__new__(
                                cls,
                                *_args,
                                raw=raw,
                                formatted=formatted,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "value": value,
                    }

            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...

            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

            def __getitem__(self, name: typing.Union[typing_extensions.Literal["value", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)


            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...

            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["value", ], str]):
                return super().get_item_oapg(name)


            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *_args,
                    value=value,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
    ) -> 'QueryResult':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
