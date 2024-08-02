from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_share_response import ApiShareResponse
from ...types import Response


def _get_kwargs(
    nano_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/share/{nano_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiShareResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiShareResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiShareResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nano_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiShareResponse]:
    """Get a share url from a short url id

    Args:
        nano_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiShareResponse]
    """

    kwargs = _get_kwargs(
        nano_id=nano_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nano_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiShareResponse]:
    """Get a share url from a short url id

    Args:
        nano_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiShareResponse
    """

    return sync_detailed(
        nano_id=nano_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    nano_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiShareResponse]:
    """Get a share url from a short url id

    Args:
        nano_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiShareResponse]
    """

    kwargs = _get_kwargs(
        nano_id=nano_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nano_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiShareResponse]:
    """Get a share url from a short url id

    Args:
        nano_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiShareResponse
    """

    return (
        await asyncio_detailed(
            nano_id=nano_id,
            client=client,
        )
    ).parsed
