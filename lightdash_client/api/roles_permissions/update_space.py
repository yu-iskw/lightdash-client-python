from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_space_response import ApiSpaceResponse
from ...models.update_space import UpdateSpace
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    space_uuid: str,
    *,
    body: UpdateSpace,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/projects/{projectUuid}/spaces/{spaceUuid}".format(
            projectUuid=project_uuid,
            spaceUuid=space_uuid,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiSpaceResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSpaceResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiSpaceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSpace,
) -> Response[ApiSpaceResponse]:
    """Update a space in a project

    Args:
        project_uuid (str):
        space_uuid (str):
        body (UpdateSpace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSpaceResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSpace,
) -> Optional[ApiSpaceResponse]:
    """Update a space in a project

    Args:
        project_uuid (str):
        space_uuid (str):
        body (UpdateSpace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSpaceResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSpace,
) -> Response[ApiSpaceResponse]:
    """Update a space in a project

    Args:
        project_uuid (str):
        space_uuid (str):
        body (UpdateSpace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiSpaceResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSpace,
) -> Optional[ApiSpaceResponse]:
    """Update a space in a project

    Args:
        project_uuid (str):
        space_uuid (str):
        body (UpdateSpace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiSpaceResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            space_uuid=space_uuid,
            client=client,
            body=body,
        )
    ).parsed
