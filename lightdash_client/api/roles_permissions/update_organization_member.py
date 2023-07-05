from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_organization_member_json_body import (
    UpdateOrganizationMemberJsonBody,
)
from ...models.update_organization_member_response_200 import (
    UpdateOrganizationMemberResponse200,
)
from ...types import Response


def _get_kwargs(
    user_uuid: str,
    *,
    client: Client,
    json_body: UpdateOrganizationMemberJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/org/users/{userUuid}".format(client.base_url, userUuid=user_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdateOrganizationMemberResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateOrganizationMemberResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdateOrganizationMemberResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uuid: str,
    *,
    client: Client,
    json_body: UpdateOrganizationMemberJsonBody,
) -> Response[UpdateOrganizationMemberResponse200]:
    """Updates the membership profile for a user in the current user's organization

    Args:
        user_uuid (str):
        json_body (UpdateOrganizationMemberJsonBody): the new membership profile

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrganizationMemberResponse200]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: str,
    *,
    client: Client,
    json_body: UpdateOrganizationMemberJsonBody,
) -> Optional[UpdateOrganizationMemberResponse200]:
    """Updates the membership profile for a user in the current user's organization

    Args:
        user_uuid (str):
        json_body (UpdateOrganizationMemberJsonBody): the new membership profile

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrganizationMemberResponse200
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_uuid: str,
    *,
    client: Client,
    json_body: UpdateOrganizationMemberJsonBody,
) -> Response[UpdateOrganizationMemberResponse200]:
    """Updates the membership profile for a user in the current user's organization

    Args:
        user_uuid (str):
        json_body (UpdateOrganizationMemberJsonBody): the new membership profile

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrganizationMemberResponse200]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: str,
    *,
    client: Client,
    json_body: UpdateOrganizationMemberJsonBody,
) -> Optional[UpdateOrganizationMemberResponse200]:
    """Updates the membership profile for a user in the current user's organization

    Args:
        user_uuid (str):
        json_body (UpdateOrganizationMemberJsonBody): the new membership profile

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrganizationMemberResponse200
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
