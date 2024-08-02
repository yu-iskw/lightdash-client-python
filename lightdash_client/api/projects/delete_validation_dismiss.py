from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_validation_dismiss_response import ApiValidationDismissResponse
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    validation_id: float,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/projects/{project_uuid}/validate/{validation_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiValidationDismissResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiValidationDismissResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiValidationDismissResponse]:
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
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiValidationDismissResponse]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidationDismissResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        validation_id=validation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    validation_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiValidationDismissResponse]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiValidationDismissResponse
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
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiValidationDismissResponse]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidationDismissResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        validation_id=validation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    validation_id: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiValidationDismissResponse]:
    """Deletes a single validation error.

    Args:
        project_uuid (str):
        validation_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiValidationDismissResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            validation_id=validation_id,
            client=client,
        )
    ).parsed
