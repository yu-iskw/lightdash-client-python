from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_chart_summary_list_response import ApiChartSummaryListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    exclude_charts_saved_in_dashboard: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["excludeChartsSavedInDashboard"] = exclude_charts_saved_in_dashboard

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/chart-summaries".format(
            projectUuid=project_uuid,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiChartSummaryListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiChartSummaryListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiChartSummaryListResponse]:
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
    exclude_charts_saved_in_dashboard: Union[Unset, bool] = UNSET,
) -> Response[ApiChartSummaryListResponse]:
    """List all charts summaries in a project

    Args:
        project_uuid (str):
        exclude_charts_saved_in_dashboard (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiChartSummaryListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        exclude_charts_saved_in_dashboard=exclude_charts_saved_in_dashboard,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    exclude_charts_saved_in_dashboard: Union[Unset, bool] = UNSET,
) -> Optional[ApiChartSummaryListResponse]:
    """List all charts summaries in a project

    Args:
        project_uuid (str):
        exclude_charts_saved_in_dashboard (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiChartSummaryListResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        exclude_charts_saved_in_dashboard=exclude_charts_saved_in_dashboard,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    exclude_charts_saved_in_dashboard: Union[Unset, bool] = UNSET,
) -> Response[ApiChartSummaryListResponse]:
    """List all charts summaries in a project

    Args:
        project_uuid (str):
        exclude_charts_saved_in_dashboard (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiChartSummaryListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        exclude_charts_saved_in_dashboard=exclude_charts_saved_in_dashboard,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    exclude_charts_saved_in_dashboard: Union[Unset, bool] = UNSET,
) -> Optional[ApiChartSummaryListResponse]:
    """List all charts summaries in a project

    Args:
        project_uuid (str):
        exclude_charts_saved_in_dashboard (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiChartSummaryListResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            exclude_charts_saved_in_dashboard=exclude_charts_saved_in_dashboard,
        )
    ).parsed
