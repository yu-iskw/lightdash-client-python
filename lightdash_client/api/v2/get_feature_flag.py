from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_feature_flag_response_200 import GetFeatureFlagResponse200
from ...types import UNSET, Response


def _get_kwargs(
    feature_flag_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/feature-flag/{featureFlagId}".format(
            featureFlagId=feature_flag_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetFeatureFlagResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFeatureFlagResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetFeatureFlagResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    feature_flag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetFeatureFlagResponse200]:
    """Get feature flag

    Args:
        feature_flag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureFlagResponse200]
    """

    kwargs = _get_kwargs(
        feature_flag_id=feature_flag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature_flag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetFeatureFlagResponse200]:
    """Get feature flag

    Args:
        feature_flag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFeatureFlagResponse200
    """

    return sync_detailed(
        feature_flag_id=feature_flag_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    feature_flag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetFeatureFlagResponse200]:
    """Get feature flag

    Args:
        feature_flag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureFlagResponse200]
    """

    kwargs = _get_kwargs(
        feature_flag_id=feature_flag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature_flag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetFeatureFlagResponse200]:
    """Get feature flag

    Args:
        feature_flag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFeatureFlagResponse200
    """

    return (
        await asyncio_detailed(
            feature_flag_id=feature_flag_id,
            client=client,
        )
    ).parsed
