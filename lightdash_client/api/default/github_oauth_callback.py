from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    installation_id: Union[Unset, str] = UNSET,
    setup_action: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["code"] = code

    params["state"] = state

    params["installation_id"] = installation_id

    params["setup_action"] = setup_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/github/oauth/callback",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    installation_id: Union[Unset, str] = UNSET,
    setup_action: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Callback URL for GitHub App Authorization also used for GitHub App Installation with combined
    Authorization

    Args:
        code (Union[Unset, str]):
        state (Union[Unset, str]):
        installation_id (Union[Unset, str]):
        setup_action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        state=state,
        installation_id=installation_id,
        setup_action=setup_action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    state: Union[Unset, str] = UNSET,
    installation_id: Union[Unset, str] = UNSET,
    setup_action: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Callback URL for GitHub App Authorization also used for GitHub App Installation with combined
    Authorization

    Args:
        code (Union[Unset, str]):
        state (Union[Unset, str]):
        installation_id (Union[Unset, str]):
        setup_action (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        state=state,
        installation_id=installation_id,
        setup_action=setup_action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
