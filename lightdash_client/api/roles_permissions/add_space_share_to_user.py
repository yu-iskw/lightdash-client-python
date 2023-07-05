from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.add_space_share_to_user_json_body import AddSpaceShareToUserJsonBody
from ...models.add_space_share_to_user_response_200 import (
    AddSpaceShareToUserResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Client,
    json_body: AddSpaceShareToUserJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/spaces/{spaceUuid}/share".format(
        client.base_url, projectUuid=project_uuid, spaceUuid=space_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[AddSpaceShareToUserResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AddSpaceShareToUserResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[AddSpaceShareToUserResponse200]:
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
    client: Client,
    json_body: AddSpaceShareToUserJsonBody,
) -> Response[AddSpaceShareToUserResponse200]:
    """Grant a user access to a space

    Args:
        project_uuid (str):
        space_uuid (str):
        json_body (AddSpaceShareToUserJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSpaceShareToUserResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Client,
    json_body: AddSpaceShareToUserJsonBody,
) -> Optional[AddSpaceShareToUserResponse200]:
    """Grant a user access to a space

    Args:
        project_uuid (str):
        space_uuid (str):
        json_body (AddSpaceShareToUserJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSpaceShareToUserResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Client,
    json_body: AddSpaceShareToUserJsonBody,
) -> Response[AddSpaceShareToUserResponse200]:
    """Grant a user access to a space

    Args:
        project_uuid (str):
        space_uuid (str):
        json_body (AddSpaceShareToUserJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddSpaceShareToUserResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        space_uuid=space_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    space_uuid: str,
    *,
    client: Client,
    json_body: AddSpaceShareToUserJsonBody,
) -> Optional[AddSpaceShareToUserResponse200]:
    """Grant a user access to a space

    Args:
        project_uuid (str):
        space_uuid (str):
        json_body (AddSpaceShareToUserJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddSpaceShareToUserResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            space_uuid=space_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
