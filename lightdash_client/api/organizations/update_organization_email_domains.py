from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_organization_allowed_email_domains import ApiOrganizationAllowedEmailDomains
from ...models.pick_allowed_email_domains_exclude_keyof_allowed_email_domains_organization_uuid import (
    PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/org/allowedEmailDomains",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiOrganizationAllowedEmailDomains]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiOrganizationAllowedEmailDomains.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiOrganizationAllowedEmailDomains]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
) -> Response[ApiOrganizationAllowedEmailDomains]:
    """Updates the allowed email domains for the current user's organization

    Args:
        body (PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid): From T,
            pick a set of properties whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationAllowedEmailDomains]
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
    body: PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
) -> Optional[ApiOrganizationAllowedEmailDomains]:
    """Updates the allowed email domains for the current user's organization

    Args:
        body (PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid): From T,
            pick a set of properties whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationAllowedEmailDomains
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
) -> Response[ApiOrganizationAllowedEmailDomains]:
    """Updates the allowed email domains for the current user's organization

    Args:
        body (PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid): From T,
            pick a set of properties whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiOrganizationAllowedEmailDomains]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid,
) -> Optional[ApiOrganizationAllowedEmailDomains]:
    """Updates the allowed email domains for the current user's organization

    Args:
        body (PickAllowedEmailDomainsExcludeKeyofAllowedEmailDomainsOrganizationUuid): From T,
            pick a set of properties whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiOrganizationAllowedEmailDomains
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
