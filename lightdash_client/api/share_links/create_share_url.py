from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_share_response import ApiShareResponse
from ...models.pick_share_url_path_or_params import PickShareUrlPathOrParams
from ...types import Response


def _get_kwargs(
    *,
    body: PickShareUrlPathOrParams,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/share",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiShareResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ApiShareResponse.from_dict(response.json())

        return response_201
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickShareUrlPathOrParams,
) -> Response[ApiShareResponse]:
    """Given a full URL generates a short url id that can be used for sharing

    Args:
        body (PickShareUrlPathOrParams): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiShareResponse]
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
    body: PickShareUrlPathOrParams,
) -> Optional[ApiShareResponse]:
    """Given a full URL generates a short url id that can be used for sharing

    Args:
        body (PickShareUrlPathOrParams): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiShareResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickShareUrlPathOrParams,
) -> Response[ApiShareResponse]:
    """Given a full URL generates a short url id that can be used for sharing

    Args:
        body (PickShareUrlPathOrParams): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiShareResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickShareUrlPathOrParams,
) -> Optional[ApiShareResponse]:
    """Given a full URL generates a short url id that can be used for sharing

    Args:
        body (PickShareUrlPathOrParams): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiShareResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
