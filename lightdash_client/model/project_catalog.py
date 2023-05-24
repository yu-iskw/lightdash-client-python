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


class ProjectCatalog(
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


                class additional_properties(
                    schemas.DictSchema
                ):


                    class MetaOapg:


                        class additional_properties(
                            schemas.DictSchema
                        ):


                            class MetaOapg:
                                required = {
                                    "sqlTable",
                                }

                                class properties:
                                    description = schemas.StrSchema
                                    sqlTable = schemas.StrSchema
                                    __annotations__ = {
                                        "description": description,
                                        "sqlTable": sqlTable,
                                    }

                            sqlTable: MetaOapg.properties.sqlTable

                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...

                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["sqlTable"]) -> MetaOapg.properties.sqlTable: ...

                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "sqlTable", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)


                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...

                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["sqlTable"]) -> MetaOapg.properties.sqlTable: ...

                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "sqlTable", ], str]):
                                return super().get_item_oapg(name)


                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                sqlTable: typing.Union[MetaOapg.properties.sqlTable, str, ],
                                description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'additional_properties':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    sqlTable=sqlTable,
                                    description=description,
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
                    ) -> 'additional_properties':
                        return super().__new__(
                            cls,
                            *_args,
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
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *_args,
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
    ) -> 'ProjectCatalog':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
