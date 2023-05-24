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


class CreateDashboard(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:

        class properties:
            name = schemas.StrSchema


            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):


                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )


            class tiles(
                schemas.ListSchema
            ):


                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['CreateDashboardTile']:
                        return CreateDashboardTile

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CreateDashboardTile'], typing.List['CreateDashboardTile']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tiles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'CreateDashboardTile':
                    return super().__getitem__(i)

            @staticmethod
            def filters() -> typing.Type['DashboardFilters']:
                return DashboardFilters
            __annotations__ = {
                "name": name,
                "description": description,
                "tiles": tiles,
                "filters": filters,
            }

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tiles"]) -> MetaOapg.properties.tiles: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> 'DashboardFilters': ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "tiles", "filters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)


    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tiles"]) -> typing.Union[MetaOapg.properties.tiles, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union['DashboardFilters', schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "tiles", "filters", ], str]):
        return super().get_item_oapg(name)


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        tiles: typing.Union[MetaOapg.properties.tiles, list, tuple, schemas.Unset] = schemas.unset,
        filters: typing.Union['DashboardFilters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDashboard':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            tiles=tiles,
            filters=filters,
            _configuration=_configuration,
            **kwargs,
        )

from lightdash_client.model.create_dashboard_tile import CreateDashboardTile
from lightdash_client.model.dashboard_filters import DashboardFilters
