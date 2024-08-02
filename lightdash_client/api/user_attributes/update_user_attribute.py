from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_create_user_attribute_response import ApiCreateUserAttributeResponse
from ...models.create_user_attribute import CreateUserAttribute
from ...types import Response


def _get_kwargs(
    user_attribute_uuid: str,
    *,
    body: CreateUserAttribute,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/org/attributes/{user_attribute_uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiCreateUserAttributeResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiCreateUserAttributeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiCreateUserAttributeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_attribute_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateUserAttribute,
) -> Response[ApiCreateUserAttributeResponse]:
    """Updates a user attribute

    Args:
        user_attribute_uuid (str):
        body (CreateUserAttribute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateUserAttributeResponse]
    """

    kwargs = _get_kwargs(
        user_attribute_uuid=user_attribute_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_attribute_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateUserAttribute,
) -> Optional[ApiCreateUserAttributeResponse]:
    """Updates a user attribute

    Args:
        user_attribute_uuid (str):
        body (CreateUserAttribute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateUserAttributeResponse
    """

    return sync_detailed(
        user_attribute_uuid=user_attribute_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_attribute_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateUserAttribute,
) -> Response[ApiCreateUserAttributeResponse]:
    """Updates a user attribute

    Args:
        user_attribute_uuid (str):
        body (CreateUserAttribute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateUserAttributeResponse]
    """

    kwargs = _get_kwargs(
        user_attribute_uuid=user_attribute_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_attribute_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateUserAttribute,
) -> Optional[ApiCreateUserAttributeResponse]:
    """Updates a user attribute

    Args:
        user_attribute_uuid (str):
        body (CreateUserAttribute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateUserAttributeResponse
    """

    return (
        await asyncio_detailed(
            user_attribute_uuid=user_attribute_uuid,
            client=client,
            body=body,
        )
    ).parsed
