from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.run_metric_total_body import RunMetricTotalBody
from ...models.time_frames import TimeFrames
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    explore: str,
    metric: str,
    *,
    body: RunMetricTotalBody,
    time_frame: TimeFrames,
    start_date: str,
    end_date: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_time_frame = time_frame.value
    params["timeFrame"] = json_time_frame

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/projects/{projectUuid}/metricsExplorer/{explore}/{metric}/runMetricTotal".format(
            projectUuid=project_uuid,
            explore=explore,
            metric=metric,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    explore: str,
    metric: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RunMetricTotalBody,
    time_frame: TimeFrames,
    start_date: str,
    end_date: str,
) -> Response[Any]:
    """
    Args:
        project_uuid (str):
        explore (str):
        metric (str):
        time_frame (TimeFrames):
        start_date (str):
        end_date (str):
        body (RunMetricTotalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore=explore,
        metric=metric,
        body=body,
        time_frame=time_frame,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_uuid: str,
    explore: str,
    metric: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RunMetricTotalBody,
    time_frame: TimeFrames,
    start_date: str,
    end_date: str,
) -> Response[Any]:
    """
    Args:
        project_uuid (str):
        explore (str):
        metric (str):
        time_frame (TimeFrames):
        start_date (str):
        end_date (str):
        body (RunMetricTotalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore=explore,
        metric=metric,
        body=body,
        time_frame=time_frame,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
