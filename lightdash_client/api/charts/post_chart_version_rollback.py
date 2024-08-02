from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_success_empty import ApiSuccessEmpty
from ...types import Response


def _get_kwargs(
    chart_uuid: str,
    version_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/saved/{chart_uuid}/rollback/{version_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSuccessEmpty]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSuccessEmpty.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSuccessEmpty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chart_uuid: str,
    version_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSuccessEmpty]:
    """Rollback chart to version

    Args:
        chart_uuid (str):
        version_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        version_uuid=version_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chart_uuid: str,
    version_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSuccessEmpty]:
    """Rollback chart to version

    Args:
        chart_uuid (str):
        version_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return sync_detailed(
        chart_uuid=chart_uuid,
        version_uuid=version_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    chart_uuid: str,
    version_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSuccessEmpty]:
    """Rollback chart to version

    Args:
        chart_uuid (str):
        version_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSuccessEmpty]
    """

    kwargs = _get_kwargs(
        chart_uuid=chart_uuid,
        version_uuid=version_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chart_uuid: str,
    version_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSuccessEmpty]:
    """Rollback chart to version

    Args:
        chart_uuid (str):
        version_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSuccessEmpty
    """

    return (
        await asyncio_detailed(
            chart_uuid=chart_uuid,
            version_uuid=version_uuid,
            client=client,
        )
    ).parsed
