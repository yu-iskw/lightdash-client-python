from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_pull_request_for_chart_fields_response_200 import CreatePullRequestForChartFieldsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    chart_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/git-integration/pull-requests/chart/{chartUuid}/fields".format(
            projectUuid=project_uuid,
            chartUuid=chart_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreatePullRequestForChartFieldsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreatePullRequestForChartFieldsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreatePullRequestForChartFieldsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreatePullRequestForChartFieldsResponse200]:
    """
    Args:
        project_uuid (str):
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePullRequestForChartFieldsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        chart_uuid=chart_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreatePullRequestForChartFieldsResponse200]:
    """
    Args:
        project_uuid (str):
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePullRequestForChartFieldsResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        chart_uuid=chart_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[CreatePullRequestForChartFieldsResponse200]:
    """
    Args:
        project_uuid (str):
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePullRequestForChartFieldsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        chart_uuid=chart_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    chart_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[CreatePullRequestForChartFieldsResponse200]:
    """
    Args:
        project_uuid (str):
        chart_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePullRequestForChartFieldsResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            chart_uuid=chart_uuid,
            client=client,
        )
    ).parsed
