from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_warehouse_credentials_response_200 import (
    CreateWarehouseCredentialsResponse200,
)
from ...models.upsert_user_warehouse_credentials import UpsertUserWarehouseCredentials
from ...types import Response


def _get_kwargs(
    *,
    body: UpsertUserWarehouseCredentials,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/user/warehouseCredentials",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWarehouseCredentialsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateWarehouseCredentialsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWarehouseCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Response[CreateWarehouseCredentialsResponse200]:
    """Create user warehouse credentials

    Args:
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWarehouseCredentialsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Optional[CreateWarehouseCredentialsResponse200]:
    """Create user warehouse credentials

    Args:
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWarehouseCredentialsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Response[CreateWarehouseCredentialsResponse200]:
    """Create user warehouse credentials

    Args:
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWarehouseCredentialsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Optional[CreateWarehouseCredentialsResponse200]:
    """Create user warehouse credentials

    Args:
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWarehouseCredentialsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
