from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_analytics_field_response_200 import GetAnalyticsFieldResponse200
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    table: str,
    field: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/{table}/analytics/{field}".format(
            projectUuid=project_uuid,
            table=table,
            field=field,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAnalyticsFieldResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAnalyticsFieldResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAnalyticsFieldResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    table: str,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetAnalyticsFieldResponse200]:
    """Get catalog analytics for fields

    Args:
        project_uuid (str):
        table (str):
        field (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsFieldResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table=table,
        field=field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    table: str,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetAnalyticsFieldResponse200]:
    """Get catalog analytics for fields

    Args:
        project_uuid (str):
        table (str):
        field (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsFieldResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        table=table,
        field=field,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    table: str,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetAnalyticsFieldResponse200]:
    """Get catalog analytics for fields

    Args:
        project_uuid (str):
        table (str):
        field (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAnalyticsFieldResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table=table,
        field=field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    table: str,
    field: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetAnalyticsFieldResponse200]:
    """Get catalog analytics for fields

    Args:
        project_uuid (str):
        table (str):
        field (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAnalyticsFieldResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            table=table,
            field=field,
            client=client,
        )
    ).parsed
