from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_create_dashboard_response import ApiCreateDashboardResponse
from ...models.create_dashboard import CreateDashboard
from ...models.duplicate_dashboard_params import DuplicateDashboardParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    body: Union["CreateDashboard", "DuplicateDashboardParams"],
    duplicate_from: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["duplicateFrom"] = duplicate_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/projects/{projectUuid}/dashboards".format(
            projectUuid=project_uuid,
        ),
        "params": params,
    }

    _body: Dict[str, Any]
    if isinstance(body, DuplicateDashboardParams):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiCreateDashboardResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ApiCreateDashboardResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiCreateDashboardResponse]:
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
    body: Union["CreateDashboard", "DuplicateDashboardParams"],
    duplicate_from: Union[Unset, str] = UNSET,
) -> Response[ApiCreateDashboardResponse]:
    """
    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, str]):
        body (Union['CreateDashboard', 'DuplicateDashboardParams']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateDashboardResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
        duplicate_from=duplicate_from,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateDashboard", "DuplicateDashboardParams"],
    duplicate_from: Union[Unset, str] = UNSET,
) -> Optional[ApiCreateDashboardResponse]:
    """
    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, str]):
        body (Union['CreateDashboard', 'DuplicateDashboardParams']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateDashboardResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        body=body,
        duplicate_from=duplicate_from,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateDashboard", "DuplicateDashboardParams"],
    duplicate_from: Union[Unset, str] = UNSET,
) -> Response[ApiCreateDashboardResponse]:
    """
    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, str]):
        body (Union['CreateDashboard', 'DuplicateDashboardParams']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateDashboardResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
        duplicate_from=duplicate_from,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["CreateDashboard", "DuplicateDashboardParams"],
    duplicate_from: Union[Unset, str] = UNSET,
) -> Optional[ApiCreateDashboardResponse]:
    """
    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, str]):
        body (Union['CreateDashboard', 'DuplicateDashboardParams']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateDashboardResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            body=body,
            duplicate_from=duplicate_from,
        )
    ).parsed
