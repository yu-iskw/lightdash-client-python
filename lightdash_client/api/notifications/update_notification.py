from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_success_empty import ApiSuccessEmpty
from ...models.pick_notification_viewed import PickNotificationViewed
from ...types import Response


def _get_kwargs(
    notification_id: str,
    *,
    body: PickNotificationViewed,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/notifications/{notification_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSuccessEmpty]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSuccessEmpty.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSuccessEmpty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notification_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickNotificationViewed,
) -> Response[ApiSuccessEmpty]:
    """Update notification

    Args:
        notification_id (str):
        body (PickNotificationViewed): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickNotificationViewed,
) -> Optional[ApiSuccessEmpty]:
    """Update notification

    Args:
        notification_id (str):
        body (PickNotificationViewed): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return sync_detailed(
        notification_id=notification_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    notification_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickNotificationViewed,
) -> Response[ApiSuccessEmpty]:
    """Update notification

    Args:
        notification_id (str):
        body (PickNotificationViewed): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickNotificationViewed,
) -> Optional[ApiSuccessEmpty]:
    """Update notification

    Args:
        notification_id (str):
        body (PickNotificationViewed): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
            body=body,
        )
    ).parsed
