from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_success_empty import ApiSuccessEmpty
from ...models.update_catalog_item_icon_body import UpdateCatalogItemIconBody
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    catalog_search_uuid: str,
    *,
    body: UpdateCatalogItemIconBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/{catalogSearchUuid}/icon".format(
            projectUuid=project_uuid,
            catalogSearchUuid=catalog_search_uuid,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSuccessEmpty]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSuccessEmpty.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSuccessEmpty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    catalog_search_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCatalogItemIconBody,
) -> Response[ApiSuccessEmpty]:
    """
    Args:
        project_uuid (str):
        catalog_search_uuid (str):
        body (UpdateCatalogItemIconBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        catalog_search_uuid=catalog_search_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    catalog_search_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCatalogItemIconBody,
) -> Optional[ApiSuccessEmpty]:
    """
    Args:
        project_uuid (str):
        catalog_search_uuid (str):
        body (UpdateCatalogItemIconBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return sync_detailed(
        project_uuid=project_uuid,
        catalog_search_uuid=catalog_search_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    catalog_search_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCatalogItemIconBody,
) -> Response[ApiSuccessEmpty]:
    """
    Args:
        project_uuid (str):
        catalog_search_uuid (str):
        body (UpdateCatalogItemIconBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        catalog_search_uuid=catalog_search_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    catalog_search_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateCatalogItemIconBody,
) -> Optional[ApiSuccessEmpty]:
    """
    Args:
        project_uuid (str):
        catalog_search_uuid (str):
        body (UpdateCatalogItemIconBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            catalog_search_uuid=catalog_search_uuid,
            client=client,
            body=body,
        )
    ).parsed
