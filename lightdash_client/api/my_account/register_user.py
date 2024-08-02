from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_user_with_invite_code import ActivateUserWithInviteCode
from ...models.api_register_user_response import ApiRegisterUserResponse
from ...models.create_user_args import CreateUserArgs
from ...types import Response


def _get_kwargs(
    *,
    body: Union["ActivateUserWithInviteCode", "CreateUserArgs"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/user",
    }

    _body: Dict[str, Any]
    if isinstance(body, ActivateUserWithInviteCode):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiRegisterUserResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiRegisterUserResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiRegisterUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ActivateUserWithInviteCode", "CreateUserArgs"],
) -> Response[ApiRegisterUserResponse]:
    """Register user

    Args:
        body (Union['ActivateUserWithInviteCode', 'CreateUserArgs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRegisterUserResponse]
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
    body: Union["ActivateUserWithInviteCode", "CreateUserArgs"],
) -> Optional[ApiRegisterUserResponse]:
    """Register user

    Args:
        body (Union['ActivateUserWithInviteCode', 'CreateUserArgs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRegisterUserResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ActivateUserWithInviteCode", "CreateUserArgs"],
) -> Response[ApiRegisterUserResponse]:
    """Register user

    Args:
        body (Union['ActivateUserWithInviteCode', 'CreateUserArgs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRegisterUserResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["ActivateUserWithInviteCode", "CreateUserArgs"],
) -> Optional[ApiRegisterUserResponse]:
    """Register user

    Args:
        body (Union['ActivateUserWithInviteCode', 'CreateUserArgs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRegisterUserResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
