from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.api_pinned_items import ApiPinnedItems
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/pinned-lists/{pinnedListUuid}/items".format(
        client.base_url, projectUuid=project_uuid, pinnedListUuid=pinned_list_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiPinnedItems]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPinnedItems.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiPinnedItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
) -> Response[ApiPinnedItems]:
    """Get pinned items

    Args:
        project_uuid (str):
        pinned_list_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPinnedItems]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
) -> Optional[ApiPinnedItems]:
    """Get pinned items

    Args:
        project_uuid (str):
        pinned_list_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPinnedItems
    """

    return sync_detailed(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
) -> Response[ApiPinnedItems]:
    """Get pinned items

    Args:
        project_uuid (str):
        pinned_list_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPinnedItems]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
) -> Optional[ApiPinnedItems]:
    """Get pinned items

    Args:
        project_uuid (str):
        pinned_list_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPinnedItems
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            client=client,
        )
    ).parsed
