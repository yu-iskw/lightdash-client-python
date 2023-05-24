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


class CreateUser(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "firstName",
            "lastName",
            "password",
            "inviteCode",
            "email",
        }

        class properties:
            inviteCode = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            email = schemas.StrSchema
            password = schemas.StrSchema
            __annotations__ = {
                "inviteCode": inviteCode,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "password": password,
            }

    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    password: MetaOapg.properties.password
    inviteCode: MetaOapg.properties.inviteCode
    email: MetaOapg.properties.email

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inviteCode"]) -> MetaOapg.properties.inviteCode: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inviteCode", "firstName", "lastName", "email", "password", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)


    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inviteCode"]) -> MetaOapg.properties.inviteCode: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inviteCode", "firstName", "lastName", "email", "password", ], str]):
        return super().get_item_oapg(name)


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        inviteCode: typing.Union[MetaOapg.properties.inviteCode, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateUser':
        return super().__new__(
            cls,
            *_args,
            firstName=firstName,
            lastName=lastName,
            password=password,
            inviteCode=inviteCode,
            email=email,
            _configuration=_configuration,
            **kwargs,
        )
