from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_saved_chart_response_200 import GetSavedChartResponse200
from ...types import Response


def _get_kwargs(
    saved_chart_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/saved/{savedChartUuid}".format(client.base_url, savedChartUuid=saved_chart_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetSavedChartResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSavedChartResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetSavedChartResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    saved_chart_uuid: str,
    *,
    client: Client,
) -> Response[GetSavedChartResponse200]:
    """Get a saved chart

    Args:
        saved_chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    saved_chart_uuid: str,
    *,
    client: Client,
) -> Optional[GetSavedChartResponse200]:
    """Get a saved chart

    Args:
        saved_chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedChartResponse200
    """

    return sync_detailed(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    saved_chart_uuid: str,
    *,
    client: Client,
) -> Response[GetSavedChartResponse200]:
    """Get a saved chart

    Args:
        saved_chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    saved_chart_uuid: str,
    *,
    client: Client,
) -> Optional[GetSavedChartResponse200]:
    """Get a saved chart

    Args:
        saved_chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedChartResponse200
    """

    return (
        await asyncio_detailed(
            saved_chart_uuid=saved_chart_uuid,
            client=client,
        )
    ).parsed
