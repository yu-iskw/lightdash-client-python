from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_scheduler_response_201 import UpdateSchedulerResponse201
from ...types import Response


def _get_kwargs(
    scheduler_uuid: str,
    *,
    client: Client,
    json_body: Any,
) -> Dict[str, Any]:
    url = "{}/api/v1/schedulers/{schedulerUuid}".format(client.base_url, schedulerUuid=scheduler_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdateSchedulerResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UpdateSchedulerResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdateSchedulerResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scheduler_uuid: str,
    *,
    client: Client,
    json_body: Any,
) -> Response[UpdateSchedulerResponse201]:
    """Update a scheduler

    Args:
        scheduler_uuid (str):
        json_body (Any): the new scheduler data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSchedulerResponse201]
    """

    kwargs = _get_kwargs(
        scheduler_uuid=scheduler_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scheduler_uuid: str,
    *,
    client: Client,
    json_body: Any,
) -> Optional[UpdateSchedulerResponse201]:
    """Update a scheduler

    Args:
        scheduler_uuid (str):
        json_body (Any): the new scheduler data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSchedulerResponse201
    """

    return sync_detailed(
        scheduler_uuid=scheduler_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    scheduler_uuid: str,
    *,
    client: Client,
    json_body: Any,
) -> Response[UpdateSchedulerResponse201]:
    """Update a scheduler

    Args:
        scheduler_uuid (str):
        json_body (Any): the new scheduler data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSchedulerResponse201]
    """

    kwargs = _get_kwargs(
        scheduler_uuid=scheduler_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scheduler_uuid: str,
    *,
    client: Client,
    json_body: Any,
) -> Optional[UpdateSchedulerResponse201]:
    """Update a scheduler

    Args:
        scheduler_uuid (str):
        json_body (Any): the new scheduler data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSchedulerResponse201
    """

    return (
        await asyncio_detailed(
            scheduler_uuid=scheduler_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
