from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_pinned_items_order_json_body_item import (
    UpdatePinnedItemsOrderJsonBodyItem,
)
from ...models.update_pinned_items_order_response_200 import (
    UpdatePinnedItemsOrderResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
    json_body: List["UpdatePinnedItemsOrderJsonBodyItem"],
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/pinned-lists/{pinnedListUuid}/items/order".format(
        client.base_url, projectUuid=project_uuid, pinnedListUuid=pinned_list_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdatePinnedItemsOrderResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdatePinnedItemsOrderResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdatePinnedItemsOrderResponse200]:
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
    json_body: List["UpdatePinnedItemsOrderJsonBodyItem"],
) -> Response[UpdatePinnedItemsOrderResponse200]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        json_body (List['UpdatePinnedItemsOrderJsonBodyItem']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePinnedItemsOrderResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
        json_body=json_body,
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
    json_body: List["UpdatePinnedItemsOrderJsonBodyItem"],
) -> Optional[UpdatePinnedItemsOrderResponse200]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        json_body (List['UpdatePinnedItemsOrderJsonBodyItem']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePinnedItemsOrderResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
    json_body: List["UpdatePinnedItemsOrderJsonBodyItem"],
) -> Response[UpdatePinnedItemsOrderResponse200]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        json_body (List['UpdatePinnedItemsOrderJsonBodyItem']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePinnedItemsOrderResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Client,
    json_body: List["UpdatePinnedItemsOrderJsonBodyItem"],
) -> Optional[UpdatePinnedItemsOrderResponse200]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        json_body (List['UpdatePinnedItemsOrderJsonBodyItem']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePinnedItemsOrderResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            pinned_list_uuid=pinned_list_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
