from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.api_share_response import ApiShareResponse
from ...types import Response


def _get_kwargs(
    nano_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/share/{nanoId}".format(client.base_url, nanoId=nano_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiShareResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiShareResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiShareResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nano_id: str,
    *,
    client: Client,
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
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nano_id: str,
    *,
    client: Client,
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
    client: Client,
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
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nano_id: str,
    *,
    client: Client,
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
