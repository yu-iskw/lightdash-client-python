from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_test_scheduler_response import ApiTestSchedulerResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: Any,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/schedulers/send",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiTestSchedulerResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiTestSchedulerResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiTestSchedulerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[ApiTestSchedulerResponse]:
    """Send a scheduler now before saving it

    Args:
        body (Any): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTestSchedulerResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[ApiTestSchedulerResponse]:
    """Send a scheduler now before saving it

    Args:
        body (Any): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTestSchedulerResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[ApiTestSchedulerResponse]:
    """Send a scheduler now before saving it

    Args:
        body (Any): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTestSchedulerResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[ApiTestSchedulerResponse]:
    """Send a scheduler now before saving it

    Args:
        body (Any): This AnyType is an alias for any
            The goal is to make it easier to identify any type in the codebase
            without having to eslint-disable all the time
            These are only used on legacy `any` types, don't use it for new types.
            This is added on a separate file to avoid circular dependencies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTestSchedulerResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
