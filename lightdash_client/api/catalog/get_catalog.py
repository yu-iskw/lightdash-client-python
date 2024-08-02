from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_filter import CatalogFilter
from ...models.catalog_type import CatalogType
from ...models.get_catalog_response_200 import GetCatalogResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, CatalogType] = UNSET,
    filter_: Union[Unset, CatalogFilter] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["search"] = search

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    json_filter_: Union[Unset, str] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/projects/{project_uuid}/dataCatalog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCatalogResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCatalogResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCatalogResponse200]:
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
    type: Union[Unset, CatalogType] = UNSET,
    filter_: Union[Unset, CatalogFilter] = UNSET,
) -> Response[GetCatalogResponse200]:
    """Get catalog items

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        type (Union[Unset, CatalogType]):
        filter_ (Union[Unset, CatalogFilter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        search=search,
        type=type,
        filter_=filter_,
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
    type: Union[Unset, CatalogType] = UNSET,
    filter_: Union[Unset, CatalogFilter] = UNSET,
) -> Optional[GetCatalogResponse200]:
    """Get catalog items

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        type (Union[Unset, CatalogType]):
        filter_ (Union[Unset, CatalogFilter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCatalogResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        search=search,
        type=type,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, CatalogType] = UNSET,
    filter_: Union[Unset, CatalogFilter] = UNSET,
) -> Response[GetCatalogResponse200]:
    """Get catalog items

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        type (Union[Unset, CatalogType]):
        filter_ (Union[Unset, CatalogFilter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCatalogResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        search=search,
        type=type,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    type: Union[Unset, CatalogType] = UNSET,
    filter_: Union[Unset, CatalogFilter] = UNSET,
) -> Optional[GetCatalogResponse200]:
    """Get catalog items

    Args:
        project_uuid (str):
        search (Union[Unset, str]):
        type (Union[Unset, CatalogType]):
        filter_ (Union[Unset, CatalogFilter]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCatalogResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            search=search,
            type=type,
            filter_=filter_,
        )
    ).parsed
