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


class Step(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "jobUuid",
            "stepType",
            "startedAt",
            "stepStatus",
            "stepLabel",
            "updatedAt",
        }

        class properties:
            jobUuid = schemas.UUIDSchema
            createdAt = schemas.DateTimeSchema
            updatedAt = schemas.DateTimeSchema


            class startedAt(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):


                class MetaOapg:
                    format = 'date-time'


                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'startedAt':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )


            class stepStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):


                class MetaOapg:
                    enum_value_to_name = {
                        "DONE": "DONE",
                        "RUNNING": "RUNNING",
                        "ERROR": "ERROR",
                        "PENDING": "PENDING",
                        "SKIPPED": "SKIPPED",
                    }

                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")

                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")

                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")

                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")

                @schemas.classproperty
                def SKIPPED(cls):
                    return cls("SKIPPED")
            stepType = schemas.StrSchema
            stepLabel = schemas.StrSchema


            class error(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):


                class MetaOapg:

                    class properties:
                        name = schemas.StrSchema
                        message = schemas.StrSchema
                        __annotations__ = {
                            "name": name,
                            "message": message,
                        }


                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...

                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...

                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "message", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)


                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...

                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...

                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "message", ], str]):
                    return super().get_item_oapg(name)


                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *_args,
                        name=name,
                        message=message,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "jobUuid": jobUuid,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "startedAt": startedAt,
                "stepStatus": stepStatus,
                "stepType": stepType,
                "stepLabel": stepLabel,
                "error": error,
            }

    createdAt: MetaOapg.properties.createdAt
    jobUuid: MetaOapg.properties.jobUuid
    stepType: MetaOapg.properties.stepType
    startedAt: MetaOapg.properties.startedAt
    stepStatus: MetaOapg.properties.stepStatus
    stepLabel: MetaOapg.properties.stepLabel
    updatedAt: MetaOapg.properties.updatedAt

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobUuid"]) -> MetaOapg.properties.jobUuid: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepStatus"]) -> MetaOapg.properties.stepStatus: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepType"]) -> MetaOapg.properties.stepType: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepLabel"]) -> MetaOapg.properties.stepLabel: ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobUuid", "createdAt", "updatedAt", "startedAt", "stepStatus", "stepType", "stepLabel", "error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)


    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobUuid"]) -> MetaOapg.properties.jobUuid: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepStatus"]) -> MetaOapg.properties.stepStatus: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepType"]) -> MetaOapg.properties.stepType: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepLabel"]) -> MetaOapg.properties.stepLabel: ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobUuid", "createdAt", "updatedAt", "startedAt", "stepStatus", "stepType", "stepLabel", "error", ], str]):
        return super().get_item_oapg(name)


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, ],
        jobUuid: typing.Union[MetaOapg.properties.jobUuid, str, uuid.UUID, ],
        stepType: typing.Union[MetaOapg.properties.stepType, str, ],
        startedAt: typing.Union[MetaOapg.properties.startedAt, None, str, datetime, ],
        stepStatus: typing.Union[MetaOapg.properties.stepStatus, str, ],
        stepLabel: typing.Union[MetaOapg.properties.stepLabel, str, ],
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, datetime, ],
        error: typing.Union[MetaOapg.properties.error, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Step':
        return super().__new__(
            cls,
            *_args,
            createdAt=createdAt,
            jobUuid=jobUuid,
            stepType=stepType,
            startedAt=startedAt,
            stepStatus=stepStatus,
            stepLabel=stepLabel,
            updatedAt=updatedAt,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )
