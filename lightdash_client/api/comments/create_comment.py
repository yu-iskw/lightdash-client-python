from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_create_comment import ApiCreateComment
from ...models.pick_comment_text_or_reply_to_or_mentions_or_text_html import (
    PickCommentTextOrReplyToOrMentionsOrTextHtml,
)
from ...types import Response


def _get_kwargs(
    dashboard_uuid: str,
    dashboard_tile_uuid: str,
    *,
    body: PickCommentTextOrReplyToOrMentionsOrTextHtml,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/comments/dashboards/{dashboard_uuid}/{dashboard_tile_uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiCreateComment]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiCreateComment.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiCreateComment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_uuid: str,
    dashboard_tile_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickCommentTextOrReplyToOrMentionsOrTextHtml,
) -> Response[ApiCreateComment]:
    """Creates a comment on a dashboard tile

    Args:
        dashboard_uuid (str):
        dashboard_tile_uuid (str):
        body (PickCommentTextOrReplyToOrMentionsOrTextHtml): From T, pick a set of properties
            whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateComment]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
        dashboard_tile_uuid=dashboard_tile_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_uuid: str,
    dashboard_tile_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickCommentTextOrReplyToOrMentionsOrTextHtml,
) -> Optional[ApiCreateComment]:
    """Creates a comment on a dashboard tile

    Args:
        dashboard_uuid (str):
        dashboard_tile_uuid (str):
        body (PickCommentTextOrReplyToOrMentionsOrTextHtml): From T, pick a set of properties
            whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateComment
    """

    return sync_detailed(
        dashboard_uuid=dashboard_uuid,
        dashboard_tile_uuid=dashboard_tile_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dashboard_uuid: str,
    dashboard_tile_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickCommentTextOrReplyToOrMentionsOrTextHtml,
) -> Response[ApiCreateComment]:
    """Creates a comment on a dashboard tile

    Args:
        dashboard_uuid (str):
        dashboard_tile_uuid (str):
        body (PickCommentTextOrReplyToOrMentionsOrTextHtml): From T, pick a set of properties
            whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCreateComment]
    """

    kwargs = _get_kwargs(
        dashboard_uuid=dashboard_uuid,
        dashboard_tile_uuid=dashboard_tile_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_uuid: str,
    dashboard_tile_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PickCommentTextOrReplyToOrMentionsOrTextHtml,
) -> Optional[ApiCreateComment]:
    """Creates a comment on a dashboard tile

    Args:
        dashboard_uuid (str):
        dashboard_tile_uuid (str):
        body (PickCommentTextOrReplyToOrMentionsOrTextHtml): From T, pick a set of properties
            whose keys are in the union K

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCreateComment
    """

    return (
        await asyncio_detailed(
            dashboard_uuid=dashboard_uuid,
            dashboard_tile_uuid=dashboard_tile_uuid,
            client=client,
            body=body,
        )
    ).parsed
