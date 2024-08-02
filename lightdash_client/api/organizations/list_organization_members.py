from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_organization_member_profiles import ApiOrganizationMemberProfiles
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_groups: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    page: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeGroups"] = include_groups

    params["pageSize"] = page_size

    params["page"] = page

    params["searchQuery"] = search_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/org/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiOrganizationMemberProfiles]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiOrganizationMemberProfiles.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiOrganizationMemberProfiles]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_groups: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    page: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Response[ApiOrganizationMemberProfiles]:
    """Gets all the members of the current user's organization

    Args:
        include_groups (Union[Unset, float]):
        page_size (Union[Unset, float]):
        page (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationMemberProfiles]
    """

    kwargs = _get_kwargs(
        include_groups=include_groups,
        page_size=page_size,
        page=page,
        search_query=search_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_groups: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    page: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Optional[ApiOrganizationMemberProfiles]:
    """Gets all the members of the current user's organization

    Args:
        include_groups (Union[Unset, float]):
        page_size (Union[Unset, float]):
        page (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationMemberProfiles
    """

    return sync_detailed(
        client=client,
        include_groups=include_groups,
        page_size=page_size,
        page=page,
        search_query=search_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_groups: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    page: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Response[ApiOrganizationMemberProfiles]:
    """Gets all the members of the current user's organization

    Args:
        include_groups (Union[Unset, float]):
        page_size (Union[Unset, float]):
        page (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationMemberProfiles]
    """

    kwargs = _get_kwargs(
        include_groups=include_groups,
        page_size=page_size,
        page=page,
        search_query=search_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_groups: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    page: Union[Unset, float] = UNSET,
    search_query: Union[Unset, str] = UNSET,
) -> Optional[ApiOrganizationMemberProfiles]:
    """Gets all the members of the current user's organization

    Args:
        include_groups (Union[Unset, float]):
        page_size (Union[Unset, float]):
        page (Union[Unset, float]):
        search_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationMemberProfiles
    """

    return (
        await asyncio_detailed(
            client=client,
            include_groups=include_groups,
            page_size=page_size,
            page=page,
            search_query=search_query,
        )
    ).parsed
