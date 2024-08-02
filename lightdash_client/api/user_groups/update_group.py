from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_group_response import ApiGroupResponse
from ...models.update_group_with_members import UpdateGroupWithMembers
from ...types import Response


def _get_kwargs(
    group_uuid: str,
    *,
    body: UpdateGroupWithMembers,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/groups/{group_uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateGroupWithMembers,
) -> Response[ApiGroupResponse]:
    """Update a group

    Args:
        group_uuid (str):
        body (UpdateGroupWithMembers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateGroupWithMembers,
) -> Optional[ApiGroupResponse]:
    """Update a group

    Args:
        group_uuid (str):
        body (UpdateGroupWithMembers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGroupResponse
    """

    return sync_detailed(
        group_uuid=group_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateGroupWithMembers,
) -> Response[ApiGroupResponse]:
    """Update a group

    Args:
        group_uuid (str):
        body (UpdateGroupWithMembers):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGroupResponse]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateGroupWithMembers,
) -> Optional[ApiGroupResponse]:
    """Update a group

    Args:
        group_uuid (str):
        body (UpdateGroupWithMembers):

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
            body=body,
        )
    ).parsed
