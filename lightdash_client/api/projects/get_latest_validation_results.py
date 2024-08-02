from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_validate_response import ApiValidateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_uuid: str,
    *,
    from_settings: Union[Unset, bool] = UNSET,
    job_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["fromSettings"] = from_settings

    params["jobId"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/projects/{project_uuid}/validate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiValidateResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiValidateResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiValidateResponse]:
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
    from_settings: Union[Unset, bool] = UNSET,
    job_id: Union[Unset, str] = UNSET,
) -> Response[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, bool]):
        job_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidateResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        from_settings=from_settings,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_settings: Union[Unset, bool] = UNSET,
    job_id: Union[Unset, str] = UNSET,
) -> Optional[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, bool]):
        job_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiValidateResponse
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        from_settings=from_settings,
        job_id=job_id,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_settings: Union[Unset, bool] = UNSET,
    job_id: Union[Unset, str] = UNSET,
) -> Response[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, bool]):
        job_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidateResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        from_settings=from_settings,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_settings: Union[Unset, bool] = UNSET,
    job_id: Union[Unset, str] = UNSET,
) -> Optional[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, bool]):
        job_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiValidateResponse
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            from_settings=from_settings,
            job_id=job_id,
        )
    ).parsed
