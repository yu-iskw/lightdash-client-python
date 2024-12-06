from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_csv_from_saved_chart_body import DownloadCsvFromSavedChartBody
from ...models.download_csv_from_saved_chart_response_200 import DownloadCsvFromSavedChartResponse200
from ...types import UNSET, Response


def _get_kwargs(
    chart_uuid: str,
    *,
    body: DownloadCsvFromSavedChartBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/saved/{chartUuid}/downloadCsv".format(
            chartUuid=chart_uuid,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DownloadCsvFromSavedChartResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DownloadCsvFromSavedChartResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DownloadCsvFromSavedChartResponse200]:
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
    body: DownloadCsvFromSavedChartBody,
) -> Response[DownloadCsvFromSavedChartResponse200]:
    """Download a CSV from a saved chart uuid

    Args:
        chart_uuid (str):
        body (DownloadCsvFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCsvFromSavedChartResponse200]
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
    body: DownloadCsvFromSavedChartBody,
) -> Optional[DownloadCsvFromSavedChartResponse200]:
    """Download a CSV from a saved chart uuid

    Args:
        chart_uuid (str):
        body (DownloadCsvFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCsvFromSavedChartResponse200
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
    body: DownloadCsvFromSavedChartBody,
) -> Response[DownloadCsvFromSavedChartResponse200]:
    """Download a CSV from a saved chart uuid

    Args:
        chart_uuid (str):
        body (DownloadCsvFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCsvFromSavedChartResponse200]
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
    body: DownloadCsvFromSavedChartBody,
) -> Optional[DownloadCsvFromSavedChartResponse200]:
    """Download a CSV from a saved chart uuid

    Args:
        chart_uuid (str):
        body (DownloadCsvFromSavedChartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCsvFromSavedChartResponse200
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            client=client,
            body=body,
        )
    ).parsed
