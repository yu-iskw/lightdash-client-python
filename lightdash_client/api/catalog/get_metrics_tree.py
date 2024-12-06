from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_get_metrics_tree import ApiGetMetricsTree
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    *,
    metric_uuids: List[str],
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_metric_uuids = metric_uuids

    params["metricUuids"] = json_metric_uuids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/metrics/tree".format(
            projectUuid=project_uuid,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGetMetricsTree]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGetMetricsTree.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGetMetricsTree]:
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
    metric_uuids: List[str],
) -> Response[ApiGetMetricsTree]:
    """
    Args:
        project_uuid (str):
        metric_uuids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetMetricsTree]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        metric_uuids=metric_uuids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    metric_uuids: List[str],
) -> Optional[ApiGetMetricsTree]:
    """
    Args:
        project_uuid (str):
        metric_uuids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetMetricsTree
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        metric_uuids=metric_uuids,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    metric_uuids: List[str],
) -> Response[ApiGetMetricsTree]:
    """
    Args:
        project_uuid (str):
        metric_uuids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetMetricsTree]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        metric_uuids=metric_uuids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    metric_uuids: List[str],
) -> Optional[ApiGetMetricsTree]:
    """
    Args:
        project_uuid (str):
        metric_uuids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetMetricsTree
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            metric_uuids=metric_uuids,
        )
    ).parsed
