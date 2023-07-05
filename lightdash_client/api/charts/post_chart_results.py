from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_chart_results_json_body import PostChartResultsJsonBody
from ...models.post_chart_results_response_200 import PostChartResultsResponse200
from ...types import Response


def _get_kwargs(
    chart_uuid: str,
    *,
    client: Client,
    json_body: PostChartResultsJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/saved/{chartUuid}/results".format(client.base_url, chartUuid=chart_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostChartResultsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostChartResultsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostChartResultsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chart_uuid: str,
    *,
    client: Client,
    json_body: PostChartResultsJsonBody,
) -> Response[PostChartResultsResponse200]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        json_body (PostChartResultsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChartResultsResponse200]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chart_uuid: str,
    *,
    client: Client,
    json_body: PostChartResultsJsonBody,
) -> Optional[PostChartResultsResponse200]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        json_body (PostChartResultsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChartResultsResponse200
    """

    return sync_detailed(
        chart_uuid=chart_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    chart_uuid: str,
    *,
    client: Client,
    json_body: PostChartResultsJsonBody,
) -> Response[PostChartResultsResponse200]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        json_body (PostChartResultsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChartResultsResponse200]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chart_uuid: str,
    *,
    client: Client,
    json_body: PostChartResultsJsonBody,
) -> Optional[PostChartResultsResponse200]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        json_body (PostChartResultsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChartResultsResponse200
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
