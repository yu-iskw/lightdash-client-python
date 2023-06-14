from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_validate_response import ApiValidateResponse
from ...types import Response
from ...types import UNSET
from ...types import Unset


def _get_kwargs(
    project_uuid: str,
    *,
    client: Client,
    from_settings: Union[Unset, None, bool] = UNSET,
    job_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/projects/{projectUuid}/validate".format(client.base_url, projectUuid=project_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fromSettings"] = from_settings

    params["jobId"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiValidateResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiValidateResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiValidateResponse]:
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
    from_settings: Union[Unset, None, bool] = UNSET,
    job_id: Union[Unset, None, str] = UNSET,
) -> Response[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, None, bool]):
        job_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidateResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        from_settings=from_settings,
        job_id=job_id,
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
    from_settings: Union[Unset, None, bool] = UNSET,
    job_id: Union[Unset, None, str] = UNSET,
) -> Optional[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, None, bool]):
        job_id (Union[Unset, None, str]):

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
    client: Client,
    from_settings: Union[Unset, None, bool] = UNSET,
    job_id: Union[Unset, None, str] = UNSET,
) -> Response[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, None, bool]):
        job_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiValidateResponse]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        from_settings=from_settings,
        job_id=job_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Client,
    from_settings: Union[Unset, None, bool] = UNSET,
    job_id: Union[Unset, None, str] = UNSET,
) -> Optional[ApiValidateResponse]:
    """Get validation results for a project. This will return the results of the latest validation job.

    Args:
        project_uuid (str):
        from_settings (Union[Unset, None, bool]):
        job_id (Union[Unset, None, str]):

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
