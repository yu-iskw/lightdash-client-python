from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.remove_user_attribute_response_200 import RemoveUserAttributeResponse200
from ...types import Response


def _get_kwargs(
    user_attribute_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/org/attributes/{userAttributeUuid}".format(client.base_url, userAttributeUuid=user_attribute_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RemoveUserAttributeResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RemoveUserAttributeResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RemoveUserAttributeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_attribute_uuid: str,
    *,
    client: Client,
) -> Response[RemoveUserAttributeResponse200]:
    """Remove a user attribute

    Args:
        user_attribute_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUserAttributeResponse200]
    """

    kwargs = _get_kwargs(
        user_attribute_uuid=user_attribute_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_attribute_uuid: str,
    *,
    client: Client,
) -> Optional[RemoveUserAttributeResponse200]:
    """Remove a user attribute

    Args:
        user_attribute_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUserAttributeResponse200
    """

    return sync_detailed(
        user_attribute_uuid=user_attribute_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_attribute_uuid: str,
    *,
    client: Client,
) -> Response[RemoveUserAttributeResponse200]:
    """Remove a user attribute

    Args:
        user_attribute_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveUserAttributeResponse200]
    """

    kwargs = _get_kwargs(
        user_attribute_uuid=user_attribute_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_attribute_uuid: str,
    *,
    client: Client,
) -> Optional[RemoveUserAttributeResponse200]:
    """Remove a user attribute

    Args:
        user_attribute_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveUserAttributeResponse200
    """

    return (
        await asyncio_detailed(
            user_attribute_uuid=user_attribute_uuid,
            client=client,
        )
    ).parsed
