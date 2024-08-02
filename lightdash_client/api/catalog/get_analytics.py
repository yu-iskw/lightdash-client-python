from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_analytics_response_200 import GetAnalyticsResponse200
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    table: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/projects/{project_uuid}/dataCatalog/{table}/analytics",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAnalyticsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAnalyticsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAnalyticsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetAnalyticsResponse200]:
    """Get catalog analytics for tables

    Args:
        project_uuid (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table=table,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetAnalyticsResponse200]:
    """Get catalog analytics for tables

    Args:
        project_uuid (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        table=table,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetAnalyticsResponse200]:
    """Get catalog analytics for tables

    Args:
        project_uuid (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table=table,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetAnalyticsResponse200]:
    """Get catalog analytics for tables

    Args:
        project_uuid (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            table=table,
            client=client,
        )
    ).parsed
