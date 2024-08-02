from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_organization_member_profile import ApiOrganizationMemberProfile
from ...types import Response


def _get_kwargs(
    user_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/org/users/{user_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiOrganizationMemberProfile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiOrganizationMemberProfile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiOrganizationMemberProfile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiOrganizationMemberProfile]:
    """Get the member profile for a user in the current user's organization by uuid

    Args:
        user_uuid (str): Stringified UUIDv4.
            See [RFC 4112](https://tools.ietf.org/html/rfc4122)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationMemberProfile]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiOrganizationMemberProfile]:
    """Get the member profile for a user in the current user's organization by uuid

    Args:
        user_uuid (str): Stringified UUIDv4.
            See [RFC 4112](https://tools.ietf.org/html/rfc4122)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationMemberProfile
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiOrganizationMemberProfile]:
    """Get the member profile for a user in the current user's organization by uuid

    Args:
        user_uuid (str): Stringified UUIDv4.
            See [RFC 4112](https://tools.ietf.org/html/rfc4122)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationMemberProfile]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiOrganizationMemberProfile]:
    """Get the member profile for a user in the current user's organization by uuid

    Args:
        user_uuid (str): Stringified UUIDv4.
            See [RFC 4112](https://tools.ietf.org/html/rfc4122)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationMemberProfile
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
