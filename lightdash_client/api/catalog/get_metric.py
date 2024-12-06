from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    table_name: str,
    metric_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/metrics/{tableName}/{metricName}".format(
            projectUuid=project_uuid,
            tableName=table_name,
            metricName=metric_name,
        ),
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    table_name: str,
    metric_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Get metric by table and metric name

    Args:
        project_uuid (str):
        table_name (str):
        metric_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table_name=table_name,
        metric_name=metric_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_uuid: str,
    table_name: str,
    metric_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Get metric by table and metric name

    Args:
        project_uuid (str):
        table_name (str):
        metric_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table_name=table_name,
        metric_name=metric_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
