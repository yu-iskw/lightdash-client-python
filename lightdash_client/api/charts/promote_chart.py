from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_promote_chart_response import ApiPromoteChartResponse
from ...types import Response


def _get_kwargs(
    chart_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/saved/{chart_uuid}/promote",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiPromoteChartResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPromoteChartResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiPromoteChartResponse]:
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
) -> Response[ApiPromoteChartResponse]:
    """Promote chart to its upstream project

    Args:
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPromoteChartResponse]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiPromoteChartResponse]:
    """Promote chart to its upstream project

    Args:
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPromoteChartResponse
    """

    return sync_detailed(
        chart_uuid=chart_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiPromoteChartResponse]:
    """Promote chart to its upstream project

    Args:
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPromoteChartResponse]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiPromoteChartResponse]:
    """Promote chart to its upstream project

    Args:
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPromoteChartResponse
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            client=client,
        )
    ).parsed
