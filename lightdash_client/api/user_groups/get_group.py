from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_group_response import ApiGroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_uuid: str,
    *,
    include_members: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeMembers"] = include_members

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGroupResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGroupResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Response[ApiGroupResponse]:
    """Get group details

    Args:
        group_uuid (str):
        include_members (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        include_members=include_members,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Optional[ApiGroupResponse]:
    """Get group details

    Args:
        group_uuid (str):
        include_members (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupResponse
    """

    return sync_detailed(
        group_uuid=group_uuid,
        client=client,
        include_members=include_members,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Response[ApiGroupResponse]:
    """Get group details

    Args:
        group_uuid (str):
        include_members (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        include_members=include_members,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_members: Union[Unset, float] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Optional[ApiGroupResponse]:
    """Get group details

    Args:
        group_uuid (str):
        include_members (Union[Unset, float]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupResponse
    """

    return (
        await asyncio_detailed(
            group_uuid=group_uuid,
            client=client,
            include_members=include_members,
            offset=offset,
        )
    ).parsed
