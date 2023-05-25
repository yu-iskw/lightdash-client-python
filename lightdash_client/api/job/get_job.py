from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional

import httpx

from ... import errors
from ...client import Client
from ...models.get_job_response_200 import GetJobResponse200
from ...types import Response


def _get_kwargs(
    job_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/jobs/{jobUuid}".format(client.base_url, jobUuid=job_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GetJobResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetJobResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GetJobResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_uuid: str,
    *,
    client: Client,
) -> Response[GetJobResponse200]:
    """List status of a job

    Args:
        job_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobResponse200]
    """

    kwargs = _get_kwargs(
        job_uuid=job_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_uuid: str,
    *,
    client: Client,
) -> Optional[GetJobResponse200]:
    """List status of a job

    Args:
        job_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobResponse200
    """

    return sync_detailed(
        job_uuid=job_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_uuid: str,
    *,
    client: Client,
) -> Response[GetJobResponse200]:
    """List status of a job

    Args:
        job_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJobResponse200]
    """

    kwargs = _get_kwargs(
        job_uuid=job_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_uuid: str,
    *,
    client: Client,
) -> Optional[GetJobResponse200]:
    """List status of a job

    Args:
        job_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetJobResponse200
    """

    return (
        await asyncio_detailed(
            job_uuid=job_uuid,
            client=client,
        )
    ).parsed
