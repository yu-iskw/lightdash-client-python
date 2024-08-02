from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_get_comments import ApiGetComments
from ...types import Response


def _get_kwargs(
    dashboard_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/comments/dashboards/{dashboard_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGetComments]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGetComments.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGetComments]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetComments]:
    """Gets all comments for a dashboard

    Args:
        dashboard_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetComments]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetComments]:
    """Gets all comments for a dashboard

    Args:
        dashboard_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetComments
    """

    return sync_detailed(
        dashboard_uuid=dashboard_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    dashboard_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetComments]:
    """Gets all comments for a dashboard

    Args:
        dashboard_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetComments]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetComments]:
    """Gets all comments for a dashboard

    Args:
        dashboard_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetComments
    """

    return (
        await asyncio_detailed(
            dashboard_uuid=dashboard_uuid,
            client=client,
        )
    ).parsed
