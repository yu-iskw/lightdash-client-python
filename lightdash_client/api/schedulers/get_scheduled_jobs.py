from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_scheduled_jobs_response import ApiScheduledJobsResponse
from ...types import Response


def _get_kwargs(
    scheduler_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/schedulers/{scheduler_uuid}/jobs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiScheduledJobsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiScheduledJobsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiScheduledJobsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scheduler_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiScheduledJobsResponse]:
    """Get scheduled jobs

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiScheduledJobsResponse]
    """

    kwargs = _get_kwargs(
        scheduler_uuid=scheduler_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scheduler_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiScheduledJobsResponse]:
    """Get scheduled jobs

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiScheduledJobsResponse
    """

    return sync_detailed(
        scheduler_uuid=scheduler_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    scheduler_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiScheduledJobsResponse]:
    """Get scheduled jobs

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiScheduledJobsResponse]
    """

    kwargs = _get_kwargs(
        scheduler_uuid=scheduler_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scheduler_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiScheduledJobsResponse]:
    """Get scheduled jobs

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiScheduledJobsResponse
    """

    return (
        await asyncio_detailed(
            scheduler_uuid=scheduler_uuid,
            client=client,
        )
    ).parsed
