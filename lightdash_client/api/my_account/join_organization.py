from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.join_organization_response_200 import JoinOrganizationResponse200
from ...types import Response


def _get_kwargs(
    organization_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/user/me/joinOrganization/{organizationUuid}".format(
        client.base_url, organizationUuid=organization_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[JoinOrganizationResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JoinOrganizationResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[JoinOrganizationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uuid: str,
    *,
    client: Client,
) -> Response[JoinOrganizationResponse200]:
    """Add the current user to an organization that accepts users with a verified email domain.
    This will fail if the organization email domain does not match the user's primary email domain.

    Args:
        organization_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JoinOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        organization_uuid=organization_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uuid: str,
    *,
    client: Client,
) -> Optional[JoinOrganizationResponse200]:
    """Add the current user to an organization that accepts users with a verified email domain.
    This will fail if the organization email domain does not match the user's primary email domain.

    Args:
        organization_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JoinOrganizationResponse200
    """

    return sync_detailed(
        organization_uuid=organization_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_uuid: str,
    *,
    client: Client,
) -> Response[JoinOrganizationResponse200]:
    """Add the current user to an organization that accepts users with a verified email domain.
    This will fail if the organization email domain does not match the user's primary email domain.

    Args:
        organization_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JoinOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        organization_uuid=organization_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uuid: str,
    *,
    client: Client,
) -> Optional[JoinOrganizationResponse200]:
    """Add the current user to an organization that accepts users with a verified email domain.
    This will fail if the organization email domain does not match the user's primary email domain.

    Args:
        organization_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JoinOrganizationResponse200
    """

    return (
        await asyncio_detailed(
            organization_uuid=organization_uuid,
            client=client,
        )
    ).parsed
