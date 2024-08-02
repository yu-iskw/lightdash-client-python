from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_dbt_cloud_settings_delete_success import (
    ApiDbtCloudSettingsDeleteSuccess,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/projects/{project_uuid}/integrations/dbt-cloud/settings",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiDbtCloudSettingsDeleteSuccess]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiDbtCloudSettingsDeleteSuccess.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiDbtCloudSettingsDeleteSuccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiDbtCloudSettingsDeleteSuccess]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiDbtCloudSettingsDeleteSuccess]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiDbtCloudSettingsDeleteSuccess]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiDbtCloudSettingsDeleteSuccess
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiDbtCloudSettingsDeleteSuccess]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiDbtCloudSettingsDeleteSuccess]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiDbtCloudSettingsDeleteSuccess]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiDbtCloudSettingsDeleteSuccess
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
