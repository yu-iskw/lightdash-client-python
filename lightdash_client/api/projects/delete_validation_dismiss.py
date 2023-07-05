from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_validation_dismiss_response_200 import (
    DeleteValidationDismissResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    validation_id: float,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/validate/{validationId}".format(
        client.base_url, projectUuid=project_uuid, validationId=validation_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[DeleteValidationDismissResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteValidationDismissResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[DeleteValidationDismissResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    validation_id: float,
    *,
    client: Client,
) -> Response[DeleteValidationDismissResponse200]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteValidationDismissResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        validation_id=validation_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    validation_id: float,
    *,
    client: Client,
) -> Optional[DeleteValidationDismissResponse200]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteValidationDismissResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        validation_id=validation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    validation_id: float,
    *,
    client: Client,
) -> Response[DeleteValidationDismissResponse200]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteValidationDismissResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        validation_id=validation_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    validation_id: float,
    *,
    client: Client,
) -> Optional[DeleteValidationDismissResponse200]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteValidationDismissResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            validation_id=validation_id,
            client=client,
        )
    ).parsed
