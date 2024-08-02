from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_warehouse_credentials_response_200 import (
    UpdateWarehouseCredentialsResponse200,
)
from ...models.upsert_user_warehouse_credentials import UpsertUserWarehouseCredentials
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    body: UpsertUserWarehouseCredentials,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/user/warehouseCredentials/{uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateWarehouseCredentialsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateWarehouseCredentialsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateWarehouseCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Response[UpdateWarehouseCredentialsResponse200]:
    """Update user warehouse credentials

    Args:
        uuid (str):
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWarehouseCredentialsResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Optional[UpdateWarehouseCredentialsResponse200]:
    """Update user warehouse credentials

    Args:
        uuid (str):
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWarehouseCredentialsResponse200
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Response[UpdateWarehouseCredentialsResponse200]:
    """Update user warehouse credentials

    Args:
        uuid (str):
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWarehouseCredentialsResponse200]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpsertUserWarehouseCredentials,
) -> Optional[UpdateWarehouseCredentialsResponse200]:
    """Update user warehouse credentials

    Args:
        uuid (str):
        body (UpsertUserWarehouseCredentials):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWarehouseCredentialsResponse200
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed
