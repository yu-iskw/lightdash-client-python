from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.update_group_json_body import UpdateGroupJsonBody
from ...models.update_group_response_200 import UpdateGroupResponse200
from ...types import Response


def _get_kwargs(
    group_uuid: str,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v1/groups/{groupUuid}".format(client.base_url, groupUuid=group_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UpdateGroupResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateGroupResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UpdateGroupResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_uuid: str,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Response[UpdateGroupResponse200]:
    """Update a group

    Args:
        group_uuid (str):
        json_body (UpdateGroupJsonBody): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateGroupResponse200]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_uuid: str,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Optional[UpdateGroupResponse200]:
    """Update a group

    Args:
        group_uuid (str):
        json_body (UpdateGroupJsonBody): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateGroupResponse200
    """

    return sync_detailed(
        group_uuid=group_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    group_uuid: str,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Response[UpdateGroupResponse200]:
    """Update a group

    Args:
        group_uuid (str):
        json_body (UpdateGroupJsonBody): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateGroupResponse200]
    """

    kwargs = _get_kwargs(
        group_uuid=group_uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_uuid: str,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Optional[UpdateGroupResponse200]:
    """Update a group

    Args:
        group_uuid (str):
        json_body (UpdateGroupJsonBody): From T, pick a set of properties whose keys are in the
            union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateGroupResponse200
    """

    return (
        await asyncio_detailed(
            group_uuid=group_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
