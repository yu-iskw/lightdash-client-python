from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_calculate_total_response import ApiCalculateTotalResponse
from ...models.calculate_total_from_saved_chart_body import (
    CalculateTotalFromSavedChartBody,
)
from ...types import Response


def _get_kwargs(
    chart_uuid: str,
    *,
    body: CalculateTotalFromSavedChartBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/saved/{chart_uuid}/calculate-total",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiCalculateTotalResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiCalculateTotalResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiCalculateTotalResponse]:
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
    body: CalculateTotalFromSavedChartBody,
) -> Response[ApiCalculateTotalResponse]:
    """Calculate metric totals from a saved chart

    Args:
        chart_uuid (str):
        body (CalculateTotalFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCalculateTotalResponse]
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
    body: CalculateTotalFromSavedChartBody,
) -> Optional[ApiCalculateTotalResponse]:
    """Calculate metric totals from a saved chart

    Args:
        chart_uuid (str):
        body (CalculateTotalFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCalculateTotalResponse
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
    body: CalculateTotalFromSavedChartBody,
) -> Response[ApiCalculateTotalResponse]:
    """Calculate metric totals from a saved chart

    Args:
        chart_uuid (str):
        body (CalculateTotalFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCalculateTotalResponse]
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
    body: CalculateTotalFromSavedChartBody,
) -> Optional[ApiCalculateTotalResponse]:
    """Calculate metric totals from a saved chart

    Args:
        chart_uuid (str):
        body (CalculateTotalFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCalculateTotalResponse
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            client=client,
            body=body,
        )
    ).parsed
