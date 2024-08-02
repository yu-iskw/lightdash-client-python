from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_pinned_items import ApiPinnedItems
from ...models.update_pinned_item_order import UpdatePinnedItemOrder
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    body: List["UpdatePinnedItemOrder"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/projects/{project_uuid}/pinned-lists/{pinned_list_uuid}/items/order",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiPinnedItems]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPinnedItems.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiPinnedItems]:
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
    client: Union[AuthenticatedClient, Client],
    body: List["UpdatePinnedItemOrder"],
) -> Response[ApiPinnedItems]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        body (List['UpdatePinnedItemOrder']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPinnedItems]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["UpdatePinnedItemOrder"],
) -> Optional[ApiPinnedItems]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        body (List['UpdatePinnedItemOrder']): the new order of the pinned items

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
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["UpdatePinnedItemOrder"],
) -> Response[ApiPinnedItems]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        body (List['UpdatePinnedItemOrder']): the new order of the pinned items

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPinnedItems]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        pinned_list_uuid=pinned_list_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    pinned_list_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["UpdatePinnedItemOrder"],
) -> Optional[ApiPinnedItems]:
    """Update pinned items order

    Args:
        project_uuid (str):
        pinned_list_uuid (str):
        body (List['UpdatePinnedItemOrder']): the new order of the pinned items

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
            body=body,
        )
    ).parsed
