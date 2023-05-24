# coding: utf-8
"""
    Lightdash API

    API spec for Lightdash server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightdash.com
    Generated by: https://openapi-generator.tech
"""
from lightdash_client.paths.invite_links.delete import DeleteInviteLinks
from lightdash_client.paths.invite_links.post import CreateInviteLink
from lightdash_client.paths.invite_links_invite_link_id.get import GetInviteLink
from lightdash_client.paths.login.post import LoginWithPassword
from lightdash_client.paths.user.get import GetUser
from lightdash_client.paths.user.post import CreateUser
from lightdash_client.paths.user_me_personal_access_tokens.get import GetPersonalAccessTokens
from lightdash_client.paths.user_me_personal_access_tokens.post import CreatePersonalAccessToken


class UserApi(
    CreateInviteLink,
    CreatePersonalAccessToken,
    CreateUser,
    DeleteInviteLinks,
    GetInviteLink,
    GetPersonalAccessTokens,
    GetUser,
    LoginWithPassword,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
