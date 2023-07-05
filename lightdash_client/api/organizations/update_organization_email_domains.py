from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_organization_email_domains_json_body import (
    UpdateOrganizationEmailDomainsJsonBody,
)
from ...models.update_organization_email_domains_response_200 import (
    UpdateOrganizationEmailDomainsResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: UpdateOrganizationEmailDomainsJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/org/allowedEmailDomains".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdateOrganizationEmailDomainsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateOrganizationEmailDomainsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdateOrganizationEmailDomainsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: UpdateOrganizationEmailDomainsJsonBody,
) -> Response[UpdateOrganizationEmailDomainsResponse200]:
    """Updates the allowed email domains for the current user's organization

    Args:
        json_body (UpdateOrganizationEmailDomainsJsonBody): the new allowed email domains

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrganizationEmailDomainsResponse200]
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
    json_body: UpdateOrganizationEmailDomainsJsonBody,
) -> Optional[UpdateOrganizationEmailDomainsResponse200]:
    """Updates the allowed email domains for the current user's organization

    Args:
        json_body (UpdateOrganizationEmailDomainsJsonBody): the new allowed email domains

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrganizationEmailDomainsResponse200
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: UpdateOrganizationEmailDomainsJsonBody,
) -> Response[UpdateOrganizationEmailDomainsResponse200]:
    """Updates the allowed email domains for the current user's organization

    Args:
        json_body (UpdateOrganizationEmailDomainsJsonBody): the new allowed email domains

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrganizationEmailDomainsResponse200]
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
    json_body: UpdateOrganizationEmailDomainsJsonBody,
) -> Optional[UpdateOrganizationEmailDomainsResponse200]:
    """Updates the allowed email domains for the current user's organization

    Args:
        json_body (UpdateOrganizationEmailDomainsJsonBody): the new allowed email domains

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrganizationEmailDomainsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
