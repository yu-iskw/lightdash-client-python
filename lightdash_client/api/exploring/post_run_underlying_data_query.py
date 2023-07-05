from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.post_run_underlying_data_query_json_body import (
    PostRunUnderlyingDataQueryJsonBody,
)
from ...models.post_run_underlying_data_query_response_200 import (
    PostRunUnderlyingDataQueryResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    explore_id: str,
    *,
    client: Client,
    json_body: PostRunUnderlyingDataQueryJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/explores/{exploreId}/runUnderlyingDataQuery".format(
        client.base_url, projectUuid=project_uuid, exploreId=explore_id
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostRunUnderlyingDataQueryResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostRunUnderlyingDataQueryResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostRunUnderlyingDataQueryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    explore_id: str,
    *,
    client: Client,
    json_body: PostRunUnderlyingDataQueryJsonBody,
) -> Response[PostRunUnderlyingDataQueryResponse200]:
    """Run a query for underlying data results

    Args:
        project_uuid (str):
        explore_id (str):
        json_body (PostRunUnderlyingDataQueryJsonBody): metricQuery for the chart to run

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRunUnderlyingDataQueryResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore_id=explore_id,
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
    explore_id: str,
    *,
    client: Client,
    json_body: PostRunUnderlyingDataQueryJsonBody,
) -> Optional[PostRunUnderlyingDataQueryResponse200]:
    """Run a query for underlying data results

    Args:
        project_uuid (str):
        explore_id (str):
        json_body (PostRunUnderlyingDataQueryJsonBody): metricQuery for the chart to run

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRunUnderlyingDataQueryResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        explore_id=explore_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    explore_id: str,
    *,
    client: Client,
    json_body: PostRunUnderlyingDataQueryJsonBody,
) -> Response[PostRunUnderlyingDataQueryResponse200]:
    """Run a query for underlying data results

    Args:
        project_uuid (str):
        explore_id (str):
        json_body (PostRunUnderlyingDataQueryJsonBody): metricQuery for the chart to run

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRunUnderlyingDataQueryResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore_id=explore_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    explore_id: str,
    *,
    client: Client,
    json_body: PostRunUnderlyingDataQueryJsonBody,
) -> Optional[PostRunUnderlyingDataQueryResponse200]:
    """Run a query for underlying data results

    Args:
        project_uuid (str):
        explore_id (str):
        json_body (PostRunUnderlyingDataQueryJsonBody): metricQuery for the chart to run

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRunUnderlyingDataQueryResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            explore_id=explore_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
