from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patch_saved_chart_response_200 import PatchSavedChartResponse200
from ...models.update_saved_chart import UpdateSavedChart
from ...types import Response


def _get_kwargs(
    saved_chart_uuid: str,
    *,
    client: Client,
    json_body: UpdateSavedChart,
) -> Dict[str, Any]:
    url = "{}/saved/{savedChartUuid}".format(client.base_url, savedChartUuid=saved_chart_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PatchSavedChartResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchSavedChartResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PatchSavedChartResponse200]:
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
    json_body: UpdateSavedChart,
) -> Response[PatchSavedChartResponse200]:
    """Update a saved chart

    Args:
        saved_chart_uuid (str):
        json_body (UpdateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
        json_body=json_body,
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
    json_body: UpdateSavedChart,
) -> Optional[PatchSavedChartResponse200]:
    """Update a saved chart

    Args:
        saved_chart_uuid (str):
        json_body (UpdateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSavedChartResponse200
    """

    return sync_detailed(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    saved_chart_uuid: str,
    *,
    client: Client,
    json_body: UpdateSavedChart,
) -> Response[PatchSavedChartResponse200]:
    """Update a saved chart

    Args:
        saved_chart_uuid (str):
        json_body (UpdateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        saved_chart_uuid=saved_chart_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    saved_chart_uuid: str,
    *,
    client: Client,
    json_body: UpdateSavedChart,
) -> Optional[PatchSavedChartResponse200]:
    """Update a saved chart

    Args:
        saved_chart_uuid (str):
        json_body (UpdateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSavedChartResponse200
    """

    return (
        await asyncio_detailed(
            saved_chart_uuid=saved_chart_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
