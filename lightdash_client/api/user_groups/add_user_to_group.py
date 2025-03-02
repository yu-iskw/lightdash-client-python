from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_success_empty import ApiSuccessEmpty
from ...types import UNSET, Response


def _get_kwargs(
    group_uuid: str,
    user_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/groups/{groupUuid}/members/{userUuid}".format(
            groupUuid=group_uuid,
            userUuid=user_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSuccessEmpty]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSuccessEmpty.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSuccessEmpty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSuccessEmpty]:
    """Add a Lightdash user to a group

    Args:
        group_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSuccessEmpty]:
    """Add a Lightdash user to a group

    Args:
        group_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return sync_detailed(
        group_uuid=group_uuid,
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSuccessEmpty]:
    """Add a Lightdash user to a group

    Args:
        group_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSuccessEmpty]:
    """Add a Lightdash user to a group

    Args:
        group_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return (
        await asyncio_detailed(
            group_uuid=group_uuid,
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
