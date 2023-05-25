from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_saved_chart_version import CreateSavedChartVersion
from ...models.create_saved_chart_version_response_200 import CreateSavedChartVersionResponse200
from ...types import Response


def _get_kwargs(
    saved_chart_uuid: str,
    *,
    client: Client,
    json_body: CreateSavedChartVersion,
) -> Dict[str, Any]:
    url = "{}/saved/{savedChartUuid}/version".format(client.base_url, savedChartUuid=saved_chart_uuid)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateSavedChartVersionResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateSavedChartVersionResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateSavedChartVersionResponse200]:
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
    json_body: CreateSavedChartVersion,
) -> Response[CreateSavedChartVersionResponse200]:
    """Create a new saved chart version

    Args:
        saved_chart_uuid (str):
        json_body (CreateSavedChartVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSavedChartVersionResponse200]
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
    json_body: CreateSavedChartVersion,
) -> Optional[CreateSavedChartVersionResponse200]:
    """Create a new saved chart version

    Args:
        saved_chart_uuid (str):
        json_body (CreateSavedChartVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSavedChartVersionResponse200
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
    json_body: CreateSavedChartVersion,
) -> Response[CreateSavedChartVersionResponse200]:
    """Create a new saved chart version

    Args:
        saved_chart_uuid (str):
        json_body (CreateSavedChartVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSavedChartVersionResponse200]
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
    json_body: CreateSavedChartVersion,
) -> Optional[CreateSavedChartVersionResponse200]:
    """Create a new saved chart version

    Args:
        saved_chart_uuid (str):
        json_body (CreateSavedChartVersion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSavedChartVersionResponse200
    """

    return (
        await asyncio_detailed(
            saved_chart_uuid=saved_chart_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
