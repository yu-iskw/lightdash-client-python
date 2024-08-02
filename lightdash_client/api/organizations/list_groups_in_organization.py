from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_group_list_response import ApiGroupListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_members: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeMembers"] = include_members

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
    include_members: Union[Unset, float] = UNSET,
) -> Response[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        include_members (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupListResponse]
    """

    kwargs = _get_kwargs(
        include_members=include_members,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
) -> Optional[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        include_members (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupListResponse
    """

    return sync_detailed(
        client=client,
        include_members=include_members,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
) -> Response[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        include_members (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupListResponse]
    """

    kwargs = _get_kwargs(
        include_members=include_members,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
) -> Optional[ApiGroupListResponse]:
    """Gets all the groups in the current user's organization

    Args:
        include_members (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            include_members=include_members,
        )
    ).parsed
