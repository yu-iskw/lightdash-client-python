from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_csv_from_explore_body import DownloadCsvFromExploreBody
from ...models.download_csv_from_explore_response_200 import (
    DownloadCsvFromExploreResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    explore_id: str,
    *,
    body: DownloadCsvFromExploreBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/projects/{project_uuid}/explores/{explore_id}/downloadCsv",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DownloadCsvFromExploreResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DownloadCsvFromExploreResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DownloadCsvFromExploreResponse200]:
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
    client: Union[AuthenticatedClient, Client],
    body: DownloadCsvFromExploreBody,
) -> Response[DownloadCsvFromExploreResponse200]:
    """
    Args:
        project_uuid (str):
        explore_id (str):
        body (DownloadCsvFromExploreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCsvFromExploreResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore_id=explore_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    explore_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadCsvFromExploreBody,
) -> Optional[DownloadCsvFromExploreResponse200]:
    """
    Args:
        project_uuid (str):
        explore_id (str):
        body (DownloadCsvFromExploreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCsvFromExploreResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        explore_id=explore_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    explore_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadCsvFromExploreBody,
) -> Response[DownloadCsvFromExploreResponse200]:
    """
    Args:
        project_uuid (str):
        explore_id (str):
        body (DownloadCsvFromExploreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCsvFromExploreResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        explore_id=explore_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    explore_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadCsvFromExploreBody,
) -> Optional[DownloadCsvFromExploreResponse200]:
    """
    Args:
        project_uuid (str):
        explore_id (str):
        body (DownloadCsvFromExploreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCsvFromExploreResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            explore_id=explore_id,
            client=client,
            body=body,
        )
    ).parsed
