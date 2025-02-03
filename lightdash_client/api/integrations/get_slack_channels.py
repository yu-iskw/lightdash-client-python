from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_slack_channels_response import ApiSlackChannelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: Union[Unset, str] = UNSET,
    exclude_archived: Union[Unset, bool] = UNSET,
    force_refresh: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search"] = search

    params["excludeArchived"] = exclude_archived

    params["forceRefresh"] = force_refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/slack/channels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSlackChannelsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSlackChannelsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSlackChannelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    exclude_archived: Union[Unset, bool] = UNSET,
    force_refresh: Union[Unset, bool] = UNSET,
) -> Response[ApiSlackChannelsResponse]:
    """Get slack channels

    Args:
        search (Union[Unset, str]):
        exclude_archived (Union[Unset, bool]):
        force_refresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSlackChannelsResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        exclude_archived=exclude_archived,
        force_refresh=force_refresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    exclude_archived: Union[Unset, bool] = UNSET,
    force_refresh: Union[Unset, bool] = UNSET,
) -> Optional[ApiSlackChannelsResponse]:
    """Get slack channels

    Args:
        search (Union[Unset, str]):
        exclude_archived (Union[Unset, bool]):
        force_refresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSlackChannelsResponse
    """

    return sync_detailed(
        client=client,
        search=search,
        exclude_archived=exclude_archived,
        force_refresh=force_refresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    exclude_archived: Union[Unset, bool] = UNSET,
    force_refresh: Union[Unset, bool] = UNSET,
) -> Response[ApiSlackChannelsResponse]:
    """Get slack channels

    Args:
        search (Union[Unset, str]):
        exclude_archived (Union[Unset, bool]):
        force_refresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSlackChannelsResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        exclude_archived=exclude_archived,
        force_refresh=force_refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    exclude_archived: Union[Unset, bool] = UNSET,
    force_refresh: Union[Unset, bool] = UNSET,
) -> Optional[ApiSlackChannelsResponse]:
    """Get slack channels

    Args:
        search (Union[Unset, str]):
        exclude_archived (Union[Unset, bool]):
        force_refresh (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSlackChannelsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            exclude_archived=exclude_archived,
            force_refresh=force_refresh,
        )
    ).parsed
