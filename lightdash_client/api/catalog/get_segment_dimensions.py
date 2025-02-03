from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_segment_dimensions_response import ApiSegmentDimensionsResponse
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    table_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dataCatalog/{tableName}/segment-dimensions".format(
            projectUuid=project_uuid,
            tableName=table_name,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSegmentDimensionsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSegmentDimensionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSegmentDimensionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSegmentDimensionsResponse]:
    """Get dimensions that can be used to segment metrics

    Args:
        project_uuid (str):
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSegmentDimensionsResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table_name=table_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSegmentDimensionsResponse]:
    """Get dimensions that can be used to segment metrics

    Args:
        project_uuid (str):
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSegmentDimensionsResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        table_name=table_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiSegmentDimensionsResponse]:
    """Get dimensions that can be used to segment metrics

    Args:
        project_uuid (str):
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSegmentDimensionsResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        table_name=table_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    table_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiSegmentDimensionsResponse]:
    """Get dimensions that can be used to segment metrics

    Args:
        project_uuid (str):
        table_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSegmentDimensionsResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            table_name=table_name,
            client=client,
        )
    ).parsed
