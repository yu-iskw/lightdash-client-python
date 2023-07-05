from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_email_verification_status_response_200 import (
    GetEmailVerificationStatusResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    passcode: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/user/me/email/status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["passcode"] = passcode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetEmailVerificationStatusResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetEmailVerificationStatusResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetEmailVerificationStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    passcode: Union[Unset, None, str] = UNSET,
) -> Response[GetEmailVerificationStatusResponse200]:
    """Get the verification status for the current user's primary email

    Args:
        passcode (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEmailVerificationStatusResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        passcode=passcode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    passcode: Union[Unset, None, str] = UNSET,
) -> Optional[GetEmailVerificationStatusResponse200]:
    """Get the verification status for the current user's primary email

    Args:
        passcode (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEmailVerificationStatusResponse200
    """

    return sync_detailed(
        client=client,
        passcode=passcode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    passcode: Union[Unset, None, str] = UNSET,
) -> Response[GetEmailVerificationStatusResponse200]:
    """Get the verification status for the current user's primary email

    Args:
        passcode (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEmailVerificationStatusResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        passcode=passcode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    passcode: Union[Unset, None, str] = UNSET,
) -> Optional[GetEmailVerificationStatusResponse200]:
    """Get the verification status for the current user's primary email

    Args:
        passcode (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEmailVerificationStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            passcode=passcode,
        )
    ).parsed
