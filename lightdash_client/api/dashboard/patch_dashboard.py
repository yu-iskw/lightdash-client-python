from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import httpx

from ... import errors
from ...client import Client
from ...models.all_fields import AllFields
from ...models.unversioned_fields import UnversionedFields
from ...models.versioned_fields import VersionedFields
from ...types import Response


def _get_kwargs(
    dashboard_uuid: str,
    *,
    client: Client,
    json_body: Union["AllFields", "UnversionedFields", "VersionedFields"],
) -> Dict[str, Any]:
    url = "{}/dashboards/{dashboardUuid}".format(client.base_url, dashboardUuid=dashboard_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, UnversionedFields):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, VersionedFields):
        json_json_body = json_body.to_dict()

    else:
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_uuid: str,
    *,
    client: Client,
    json_body: Union["AllFields", "UnversionedFields", "VersionedFields"],
) -> Response[Any]:
    """Update dashboard

     Update details for a single dashboard by dashboard_id

    Args:
        dashboard_uuid (str):
        json_body (Union['AllFields', 'UnversionedFields', 'VersionedFields']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dashboard_uuid: str,
    *,
    client: Client,
    json_body: Union["AllFields", "UnversionedFields", "VersionedFields"],
) -> Response[Any]:
    """Update dashboard

     Update details for a single dashboard by dashboard_id

    Args:
        dashboard_uuid (str):
        json_body (Union['AllFields', 'UnversionedFields', 'VersionedFields']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
