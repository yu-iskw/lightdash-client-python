from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_organization_json_body import CreateOrganizationJsonBody
from ...models.create_organization_response_200 import CreateOrganizationResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/org".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateOrganizationResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateOrganizationResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateOrganizationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Response[CreateOrganizationResponse200]:
    """Creates a new organization, the current user becomes the Admin of the new organization.
    This is only available to users that are not already in an organization.

    Args:
        json_body (CreateOrganizationJsonBody): the new organization settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Optional[CreateOrganizationResponse200]:
    """Creates a new organization, the current user becomes the Admin of the new organization.
    This is only available to users that are not already in an organization.

    Args:
        json_body (CreateOrganizationJsonBody): the new organization settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Response[CreateOrganizationResponse200]:
    """Creates a new organization, the current user becomes the Admin of the new organization.
    This is only available to users that are not already in an organization.

    Args:
        json_body (CreateOrganizationJsonBody): the new organization settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrganizationResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateOrganizationJsonBody,
) -> Optional[CreateOrganizationResponse200]:
    """Creates a new organization, the current user becomes the Admin of the new organization.
    This is only available to users that are not already in an organization.

    Args:
        json_body (CreateOrganizationJsonBody): the new organization settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrganizationResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
