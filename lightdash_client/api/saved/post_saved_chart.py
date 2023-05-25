from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import httpx

from ... import errors
from ...client import Client
from ...models.create_saved_chart import CreateSavedChart
from ...models.post_saved_chart_response_200 import PostSavedChartResponse200
from ...types import Response
from ...types import UNSET
from ...types import Unset


def _get_kwargs(
    project_uuid: str,
    *,
    client: Client,
    json_body: CreateSavedChart,
    duplicate_from: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects/{projectUuid}/saved".format(client.base_url, projectUuid=project_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["duplicateFrom"] = duplicate_from

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PostSavedChartResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostSavedChartResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PostSavedChartResponse200]:
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
    json_body: CreateSavedChart,
    duplicate_from: Union[Unset, None, str] = UNSET,
) -> Response[PostSavedChartResponse200]:
    """Create saved chart in project

    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, None, str]):
        json_body (CreateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
        duplicate_from=duplicate_from,
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
    json_body: CreateSavedChart,
    duplicate_from: Union[Unset, None, str] = UNSET,
) -> Optional[PostSavedChartResponse200]:
    """Create saved chart in project

    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, None, str]):
        json_body (CreateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSavedChartResponse200
    """

    return sync_detailed(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
        duplicate_from=duplicate_from,
    ).parsed


async def asyncio_detailed(
    project_uuid: str,
    *,
    client: Client,
    json_body: CreateSavedChart,
    duplicate_from: Union[Unset, None, str] = UNSET,
) -> Response[PostSavedChartResponse200]:
    """Create saved chart in project

    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, None, str]):
        json_body (CreateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSavedChartResponse200]
    """

    kwargs = _get_kwargs(
        project_uuid=project_uuid,
        client=client,
        json_body=json_body,
        duplicate_from=duplicate_from,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_uuid: str,
    *,
    client: Client,
    json_body: CreateSavedChart,
    duplicate_from: Union[Unset, None, str] = UNSET,
) -> Optional[PostSavedChartResponse200]:
    """Create saved chart in project

    Args:
        project_uuid (str):
        duplicate_from (Union[Unset, None, str]):
        json_body (CreateSavedChart):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSavedChartResponse200
    """

    return (
        await asyncio_detailed(
            project_uuid=project_uuid,
            client=client,
            json_body=json_body,
            duplicate_from=duplicate_from,
        )
    ).parsed
