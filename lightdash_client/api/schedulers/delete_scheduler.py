from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_scheduler_response_201 import DeleteSchedulerResponse201
from ...types import UNSET, Response


def _get_kwargs(
    scheduler_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/schedulers/{schedulerUuid}".format(
            schedulerUuid=scheduler_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteSchedulerResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DeleteSchedulerResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteSchedulerResponse201]:
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
) -> Response[DeleteSchedulerResponse201]:
    """Delete a scheduler

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSchedulerResponse201]
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
) -> Optional[DeleteSchedulerResponse201]:
    """Delete a scheduler

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSchedulerResponse201
    """

    return sync_detailed(
        scheduler_uuid=scheduler_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    scheduler_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteSchedulerResponse201]:
    """Delete a scheduler

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSchedulerResponse201]
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
) -> Optional[DeleteSchedulerResponse201]:
    """Delete a scheduler

    Args:
        scheduler_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSchedulerResponse201
    """

    return (
        await asyncio_detailed(
            scheduler_uuid=scheduler_uuid,
            client=client,
        )
    ).parsed
