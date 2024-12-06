from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_metrics_catalog import ApiMetricsCatalog
from ...models.api_sort_direction import ApiSortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    search: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, ApiSortDirection] = UNSET,
    categories: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search"] = search

    params["page"] = page

    params["pageSize"] = page_size

    params["sort"] = sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_categories: Union[Unset, List[str]] = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories

    params["categories"] = json_categories

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/metrics".format(
            projectUuid=project_uuid,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiMetricsCatalog]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiMetricsCatalog.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiMetricsCatalog]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, ApiSortDirection] = UNSET,
    categories: Union[Unset, List[str]] = UNSET,
) -> Response[ApiMetricsCatalog]:
    """Get metrics catalog

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        sort (Union[Unset, str]):
        order (Union[Unset, ApiSortDirection]):
        categories (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMetricsCatalog]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        search=search,
        page=page,
        page_size=page_size,
        sort=sort,
        order=order,
        categories=categories,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, ApiSortDirection] = UNSET,
    categories: Union[Unset, List[str]] = UNSET,
) -> Optional[ApiMetricsCatalog]:
    """Get metrics catalog

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        sort (Union[Unset, str]):
        order (Union[Unset, ApiSortDirection]):
        categories (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMetricsCatalog
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        search=search,
        page=page,
        page_size=page_size,
        sort=sort,
        order=order,
        categories=categories,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, ApiSortDirection] = UNSET,
    categories: Union[Unset, List[str]] = UNSET,
) -> Response[ApiMetricsCatalog]:
    """Get metrics catalog

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        sort (Union[Unset, str]):
        order (Union[Unset, ApiSortDirection]):
        categories (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiMetricsCatalog]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        search=search,
        page=page,
        page_size=page_size,
        sort=sort,
        order=order,
        categories=categories,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    page: Union[Unset, float] = UNSET,
    page_size: Union[Unset, float] = UNSET,
    sort: Union[Unset, str] = UNSET,
    order: Union[Unset, ApiSortDirection] = UNSET,
    categories: Union[Unset, List[str]] = UNSET,
) -> Optional[ApiMetricsCatalog]:
    """Get metrics catalog

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        page (Union[Unset, float]):
        page_size (Union[Unset, float]):
        sort (Union[Unset, str]):
        order (Union[Unset, ApiSortDirection]):
        categories (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiMetricsCatalog
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            search=search,
            page=page,
            page_size=page_size,
            sort=sort,
            order=order,
            categories=categories,
        )
    ).parsed
