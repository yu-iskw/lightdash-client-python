from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_project_access_list_response import ApiProjectAccessListResponse
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/projects/{projectUuid}/access".format(
            projectUuid=project_uuid,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiProjectAccessListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiProjectAccessListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiProjectAccessListResponse]:
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
) -> Response[ApiProjectAccessListResponse]:
    """Get access list for a project. This is a list of users that have been explictly granted access to
    the project.
    There may be other users that have access to the project via their organization membership.

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiProjectAccessListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiProjectAccessListResponse]:
    """Get access list for a project. This is a list of users that have been explictly granted access to
    the project.
    There may be other users that have access to the project via their organization membership.

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiProjectAccessListResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiProjectAccessListResponse]:
    """Get access list for a project. This is a list of users that have been explictly granted access to
    the project.
    There may be other users that have access to the project via their organization membership.

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiProjectAccessListResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiProjectAccessListResponse]:
    """Get access list for a project. This is a list of users that have been explictly granted access to
    the project.
    There may be other users that have access to the project via their organization membership.

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiProjectAccessListResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
