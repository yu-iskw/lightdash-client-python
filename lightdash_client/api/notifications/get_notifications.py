from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_get_notifications import ApiGetNotifications
from ...models.api_notification_resource_type import ApiNotificationResourceType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    type: ApiNotificationResourceType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_type = type.value
    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGetNotifications]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGetNotifications.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGetNotifications]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: ApiNotificationResourceType,
) -> Response[ApiGetNotifications]:
    """Gets notifications for a user based on the type

    Args:
        type (ApiNotificationResourceType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetNotifications]
    """

    kwargs = _get_kwargs(
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type: ApiNotificationResourceType,
) -> Optional[ApiGetNotifications]:
    """Gets notifications for a user based on the type

    Args:
        type (ApiNotificationResourceType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetNotifications
    """

    return sync_detailed(
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: ApiNotificationResourceType,
) -> Response[ApiGetNotifications]:
    """Gets notifications for a user based on the type

    Args:
        type (ApiNotificationResourceType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetNotifications]
    """

    kwargs = _get_kwargs(
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type: ApiNotificationResourceType,
) -> Optional[ApiGetNotifications]:
    """Gets notifications for a user based on the type

    Args:
        type (ApiNotificationResourceType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetNotifications
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
        )
    ).parsed
