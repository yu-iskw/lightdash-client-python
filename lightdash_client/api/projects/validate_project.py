from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_job_scheduled_response import ApiJobScheduledResponse
from ...models.validate_project_body import ValidateProjectBody
from ...types import UNSET, Response


def _get_kwargs(
    project_uuid: str,
    *,
    body: ValidateProjectBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/projects/{projectUuid}/validate".format(
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
) -> Optional[ApiJobScheduledResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiJobScheduledResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiJobScheduledResponse]:
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
    body: ValidateProjectBody,
) -> Response[ApiJobScheduledResponse]:
    """Validate content inside a project. This will start a validation job and return the job id.

    Validation jobs scan all charts and dashboards inside a project to find any broken references
    to metrics or dimensions that aren't available. Results are available after the job is completed.

    Args:
        project_uuid (str):
        body (ValidateProjectBody): the compiled explores to validate against an existing project,
            this is used in the CLI to validate a project without creating a preview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiJobScheduledResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateProjectBody,
) -> Optional[ApiJobScheduledResponse]:
    """Validate content inside a project. This will start a validation job and return the job id.

    Validation jobs scan all charts and dashboards inside a project to find any broken references
    to metrics or dimensions that aren't available. Results are available after the job is completed.

    Args:
        project_uuid (str):
        body (ValidateProjectBody): the compiled explores to validate against an existing project,
            this is used in the CLI to validate a project without creating a preview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiJobScheduledResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateProjectBody,
) -> Response[ApiJobScheduledResponse]:
    """Validate content inside a project. This will start a validation job and return the job id.

    Validation jobs scan all charts and dashboards inside a project to find any broken references
    to metrics or dimensions that aren't available. Results are available after the job is completed.

    Args:
        project_uuid (str):
        body (ValidateProjectBody): the compiled explores to validate against an existing project,
            this is used in the CLI to validate a project without creating a preview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiJobScheduledResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ValidateProjectBody,
) -> Optional[ApiJobScheduledResponse]:
    """Validate content inside a project. This will start a validation job and return the job id.

    Validation jobs scan all charts and dashboards inside a project to find any broken references
    to metrics or dimensions that aren't available. Results are available after the job is completed.

    Args:
        project_uuid (str):
        body (ValidateProjectBody): the compiled explores to validate against an existing project,
            this is used in the CLI to validate a project without creating a preview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiJobScheduledResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            body=body,
        )
    ).parsed
