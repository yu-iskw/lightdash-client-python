from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rotate_personal_access_token_body import RotatePersonalAccessTokenBody
from ...models.rotate_personal_access_token_response_200 import RotatePersonalAccessTokenResponse200
from ...types import UNSET, Response


def _get_kwargs(
    personal_access_token_uuid: str,
    *,
    body: RotatePersonalAccessTokenBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/user/me/personal-access-tokens/{personalAccessTokenUuid}/rotate".format(
            personalAccessTokenUuid=personal_access_token_uuid,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RotatePersonalAccessTokenResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RotatePersonalAccessTokenResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RotatePersonalAccessTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    personal_access_token_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RotatePersonalAccessTokenBody,
) -> Response[RotatePersonalAccessTokenResponse200]:
    """Rotate personal access token

    Args:
        personal_access_token_uuid (str):
        body (RotatePersonalAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotatePersonalAccessTokenResponse200]
    """

    kwargs = _get_kwargs(
        personal_access_token_uuid=personal_access_token_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    personal_access_token_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RotatePersonalAccessTokenBody,
) -> Optional[RotatePersonalAccessTokenResponse200]:
    """Rotate personal access token

    Args:
        personal_access_token_uuid (str):
        body (RotatePersonalAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotatePersonalAccessTokenResponse200
    """

    return sync_detailed(
        personal_access_token_uuid=personal_access_token_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    personal_access_token_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RotatePersonalAccessTokenBody,
) -> Response[RotatePersonalAccessTokenResponse200]:
    """Rotate personal access token

    Args:
        personal_access_token_uuid (str):
        body (RotatePersonalAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RotatePersonalAccessTokenResponse200]
    """

    kwargs = _get_kwargs(
        personal_access_token_uuid=personal_access_token_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    personal_access_token_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RotatePersonalAccessTokenBody,
) -> Optional[RotatePersonalAccessTokenResponse200]:
    """Rotate personal access token

    Args:
        personal_access_token_uuid (str):
        body (RotatePersonalAccessTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RotatePersonalAccessTokenResponse200
    """

    return (
        await asyncio_detailed(
            personal_access_token_uuid=personal_access_token_uuid,
            client=client,
            body=body,
        )
    ).parsed
