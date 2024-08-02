from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_get_project_member_response import ApiGetProjectMemberResponse
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    user_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/projects/{project_uuid}/user/{user_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGetProjectMemberResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiGetProjectMemberResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGetProjectMemberResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetProjectMemberResponse]:
    """Get a project explicit member's access.
    There may be users that have access to the project via their organization membership.

    NOTE:
    We don't use the API on the frontend. Instead, we can call the API
    so that we make sure of the user's access to the project.

    Args:
        project_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetProjectMemberResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetProjectMemberResponse]:
    """Get a project explicit member's access.
    There may be users that have access to the project via their organization membership.

    NOTE:
    We don't use the API on the frontend. Instead, we can call the API
    so that we make sure of the user's access to the project.

    Args:
        project_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetProjectMemberResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetProjectMemberResponse]:
    """Get a project explicit member's access.
    There may be users that have access to the project via their organization membership.

    NOTE:
    We don't use the API on the frontend. Instead, we can call the API
    so that we make sure of the user's access to the project.

    Args:
        project_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetProjectMemberResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    user_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetProjectMemberResponse]:
    """Get a project explicit member's access.
    There may be users that have access to the project via their organization membership.

    NOTE:
    We don't use the API on the frontend. Instead, we can call the API
    so that we make sure of the user's access to the project.

    Args:
        project_uuid (str):
        user_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetProjectMemberResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
