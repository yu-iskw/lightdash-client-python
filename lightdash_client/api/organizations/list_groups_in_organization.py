from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_group_list_response import ApiGroupListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    include_members: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["includeMembers"] = include_members

    params["searchQuery"] = search_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/org/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGroupListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGroupListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGroupListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    include_members: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Response[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        include_members (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_members=include_members,
        search_query=search_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    include_members: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Optional[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        include_members (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        include_members=include_members,
        search_query=search_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    include_members: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Response[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        include_members (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_members=include_members,
        search_query=search_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    include_members: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Optional[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        include_members (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            include_members=include_members,
            search_query=search_query,
        )
    ).parsed
