from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_run_query_response import ApiRunQueryResponse
from ...models.post_chart_results_body import PostChartResultsBody
from ...types import Response


def _get_kwargs(
    chart_uuid: str,
    *,
    body: PostChartResultsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/saved/{chart_uuid}/results",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiRunQueryResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiRunQueryResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiRunQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChartResultsBody,
) -> Response[ApiRunQueryResponse]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        body (PostChartResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRunQueryResponse]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChartResultsBody,
) -> Optional[ApiRunQueryResponse]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        body (PostChartResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRunQueryResponse
    """

    return sync_detailed(
        chart_uuid=chart_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChartResultsBody,
) -> Response[ApiRunQueryResponse]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        body (PostChartResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiRunQueryResponse]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChartResultsBody,
) -> Optional[ApiRunQueryResponse]:
    """Run a query for a chart

    Args:
        chart_uuid (str):
        body (PostChartResultsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiRunQueryResponse
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            client=client,
            body=body,
        )
    ).parsed
