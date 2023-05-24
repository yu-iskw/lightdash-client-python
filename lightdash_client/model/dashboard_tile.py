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


class DashboardTile(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:


        class all_of_1(
            schemas.DictSchema
        ):


            class MetaOapg:
                required = {
                    "uuid",
                }

                class properties:
                    uuid = schemas.UUIDSchema
                    __annotations__ = {
                        "uuid": uuid,
                    }

            uuid: MetaOapg.properties.uuid

            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...

            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

            def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)


            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...

            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", ], str]):
                return super().get_item_oapg(name)


            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    uuid=uuid,
                    _configuration=_configuration,
                    **kwargs,
                )

        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                CreateDashboardTile,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DashboardTile':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from lightdash_client.model.create_dashboard_tile import CreateDashboardTile
