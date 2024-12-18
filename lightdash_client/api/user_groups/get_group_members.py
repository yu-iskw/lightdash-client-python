from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_group_members_response import ApiGroupMembersResponse
from ...types import UNSET, Response


def _get_kwargs(
    group_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/groups/{groupUuid}/members".format(
            groupUuid=group_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGroupMembersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGroupMembersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGroupMembersResponse]:
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
) -> Response[ApiGroupMembersResponse]:
    """View members of a group

    Args:
        group_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupMembersResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGroupMembersResponse]:
    """View members of a group

    Args:
        group_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupMembersResponse
    """

    return sync_detailed(
        group_uuid=group_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGroupMembersResponse]:
    """View members of a group

    Args:
        group_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupMembersResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGroupMembersResponse]:
    """View members of a group

    Args:
        group_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupMembersResponse
    """

    return (
        await asyncio_detailed(
            group_uuid=group_uuid,
            client=client,
        )
    ).parsed
