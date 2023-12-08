from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.api_calculate_total_response import ApiCalculateTotalResponse
from ...models.calculate_total_from_query import CalculateTotalFromQuery
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    *,
    client: Client,
    json_body: CalculateTotalFromQuery,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/calculate-total".format(client.base_url, projectUuid=project_uuid)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiCalculateTotalResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiCalculateTotalResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiCalculateTotalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    *,
    client: Client,
    json_body: CalculateTotalFromQuery,
) -> Response[ApiCalculateTotalResponse]:
    """Calculate all metric totals from a metricQuery

    Args:
        project_uuid (str):
        json_body (CalculateTotalFromQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCalculateTotalResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Client,
    json_body: CalculateTotalFromQuery,
) -> Optional[ApiCalculateTotalResponse]:
    """Calculate all metric totals from a metricQuery

    Args:
        project_uuid (str):
        json_body (CalculateTotalFromQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCalculateTotalResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Client,
    json_body: CalculateTotalFromQuery,
) -> Response[ApiCalculateTotalResponse]:
    """Calculate all metric totals from a metricQuery

    Args:
        project_uuid (str):
        json_body (CalculateTotalFromQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCalculateTotalResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Client,
    json_body: CalculateTotalFromQuery,
) -> Optional[ApiCalculateTotalResponse]:
    """Calculate all metric totals from a metricQuery

    Args:
        project_uuid (str):
        json_body (CalculateTotalFromQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCalculateTotalResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
