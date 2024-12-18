from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_update_project_group_access import ApiUpdateProjectGroupAccess
from ...models.pick_db_project_group_access_role import PickDBProjectGroupAccessRole
from ...types import UNSET, Response


def _get_kwargs(
    group_uuid: str,
    project_uuid: str,
    *,
    body: PickDBProjectGroupAccessRole,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/groups/{groupUuid}/projects/{projectUuid}".format(
            groupUuid=group_uuid,
            projectUuid=project_uuid,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiUpdateProjectGroupAccess]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiUpdateProjectGroupAccess.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiUpdateProjectGroupAccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_uuid: str,
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickDBProjectGroupAccessRole,
) -> Response[ApiUpdateProjectGroupAccess]:
    """Update project access for a group

    Args:
        group_uuid (str):
        project_uuid (str):
        body (PickDBProjectGroupAccessRole): From T, pick a set of properties whose keys are in
            the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiUpdateProjectGroupAccess]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        project_uuid=project_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickDBProjectGroupAccessRole,
) -> Optional[ApiUpdateProjectGroupAccess]:
    """Update project access for a group

    Args:
        group_uuid (str):
        project_uuid (str):
        body (PickDBProjectGroupAccessRole): From T, pick a set of properties whose keys are in
            the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiUpdateProjectGroupAccess
    """

    return sync_detailed(
        group_uuid=group_uuid,
        project_uuid=project_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickDBProjectGroupAccessRole,
) -> Response[ApiUpdateProjectGroupAccess]:
    """Update project access for a group

    Args:
        group_uuid (str):
        project_uuid (str):
        body (PickDBProjectGroupAccessRole): From T, pick a set of properties whose keys are in
            the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiUpdateProjectGroupAccess]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        project_uuid=project_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickDBProjectGroupAccessRole,
) -> Optional[ApiUpdateProjectGroupAccess]:
    """Update project access for a group

    Args:
        group_uuid (str):
        project_uuid (str):
        body (PickDBProjectGroupAccessRole): From T, pick a set of properties whose keys are in
            the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiUpdateProjectGroupAccess
    """

    return (
        await asyncio_detailed(
            group_uuid=group_uuid,
            project_uuid=project_uuid,
            client=client,
            body=body,
        )
    ).parsed
