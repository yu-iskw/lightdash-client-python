from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_update_dashboards_response import ApiUpdateDashboardsResponse
from ...models.pick_dashboard_uuid_or_name_or_description_or_space_uuid import (
    PickDashboardUuidOrNameOrDescriptionOrSpaceUuid,
)
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    *,
    body: List["PickDashboardUuidOrNameOrDescriptionOrSpaceUuid"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/projects/{projectUuid}/dashboards".format(
            projectUuid=project_uuid,
        ),
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiUpdateDashboardsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiUpdateDashboardsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiUpdateDashboardsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["PickDashboardUuidOrNameOrDescriptionOrSpaceUuid"],
) -> Response[ApiUpdateDashboardsResponse]:
    """
    Args:
        project_uuid (str):
        body (List['PickDashboardUuidOrNameOrDescriptionOrSpaceUuid']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiUpdateDashboardsResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["PickDashboardUuidOrNameOrDescriptionOrSpaceUuid"],
) -> Optional[ApiUpdateDashboardsResponse]:
    """
    Args:
        project_uuid (str):
        body (List['PickDashboardUuidOrNameOrDescriptionOrSpaceUuid']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiUpdateDashboardsResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["PickDashboardUuidOrNameOrDescriptionOrSpaceUuid"],
) -> Response[ApiUpdateDashboardsResponse]:
    """
    Args:
        project_uuid (str):
        body (List['PickDashboardUuidOrNameOrDescriptionOrSpaceUuid']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiUpdateDashboardsResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: List["PickDashboardUuidOrNameOrDescriptionOrSpaceUuid"],
) -> Optional[ApiUpdateDashboardsResponse]:
    """
    Args:
        project_uuid (str):
        body (List['PickDashboardUuidOrNameOrDescriptionOrSpaceUuid']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiUpdateDashboardsResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            body=body,
        )
    ).parsed
