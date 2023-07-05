from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.delete_dbt_cloud_integration_settings_response_200 import (
    DeleteDbtCloudIntegrationSettingsResponse200,
)
from ...types import Response


def _get_kwargs(
    project_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/integrations/dbt-cloud/settings".format(
        client.base_url, projectUuid=project_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[DeleteDbtCloudIntegrationSettingsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteDbtCloudIntegrationSettingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[DeleteDbtCloudIntegrationSettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_uuid: str,
    *,
    client: Client,
) -> Response[DeleteDbtCloudIntegrationSettingsResponse200]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDbtCloudIntegrationSettingsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Client,
) -> Optional[DeleteDbtCloudIntegrationSettingsResponse200]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDbtCloudIntegrationSettingsResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Client,
) -> Response[DeleteDbtCloudIntegrationSettingsResponse200]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteDbtCloudIntegrationSettingsResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Client,
) -> Optional[DeleteDbtCloudIntegrationSettingsResponse200]:
    """Remove the dbt Cloud integration settings for a project

    Args:
        project_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteDbtCloudIntegrationSettingsResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
        )
    ).parsed
