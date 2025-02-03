from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_dashboard_as_code_list_response import ApiDashboardAsCodeListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    ids: Union[Unset, List[str]] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/dashboards/code".format(
            projectUuid=project_uuid,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiDashboardAsCodeListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiDashboardAsCodeListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiDashboardAsCodeListResponse]:
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
    ids: Union[Unset, List[str]] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Response[ApiDashboardAsCodeListResponse]:
    """
    Args:
        project_uuid (str):
        ids (Union[Unset, List[str]]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiDashboardAsCodeListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        ids=ids,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, List[str]] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Optional[ApiDashboardAsCodeListResponse]:
    """
    Args:
        project_uuid (str):
        ids (Union[Unset, List[str]]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiDashboardAsCodeListResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        ids=ids,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, List[str]] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Response[ApiDashboardAsCodeListResponse]:
    """
    Args:
        project_uuid (str):
        ids (Union[Unset, List[str]]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiDashboardAsCodeListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        ids=ids,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    ids: Union[Unset, List[str]] = UNSET,
    offset: Union[Unset, float] = UNSET,
) -> Optional[ApiDashboardAsCodeListResponse]:
    """
    Args:
        project_uuid (str):
        ids (Union[Unset, List[str]]):
        offset (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiDashboardAsCodeListResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            ids=ids,
            offset=offset,
        )
    ).parsed
