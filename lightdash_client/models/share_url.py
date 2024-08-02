from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareUrl")


@_attrs_define
class ShareUrl:
    """A ShareUrl maps a short shareable id to a full URL
    in the Lightdash UI. This allows very long URLs
    to be represented by short ids.

        Attributes:
            params (str):
            path (str): The URL path of the full URL
            nanoid (str): Unique shareable id
            host (Union[Unset, str]):
            url (Union[Unset, str]):
            share_url (Union[Unset, str]):
            organization_uuid (Union[Unset, str]):
            created_by_user_uuid (Union[Unset, str]):
    """

    params: str
    path: str
    nanoid: str
    host: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    share_url: Union[Unset, str] = UNSET
    organization_uuid: Union[Unset, str] = UNSET
    created_by_user_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        params = self.params

        path = self.path

        nanoid = self.nanoid

        host = self.host

        url = self.url

        share_url = self.share_url

        organization_uuid = self.organization_uuid

        created_by_user_uuid = self.created_by_user_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
                "path": path,
                "nanoid": nanoid,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if url is not UNSET:
            field_dict["url"] = url
        if share_url is not UNSET:
            field_dict["shareUrl"] = share_url
        if organization_uuid is not UNSET:
            field_dict["organizationUuid"] = organization_uuid
        if created_by_user_uuid is not UNSET:
            field_dict["createdByUserUuid"] = created_by_user_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        params = d.pop("params")

        path = d.pop("path")

        nanoid = d.pop("nanoid")

        host = d.pop("host", UNSET)

        url = d.pop("url", UNSET)

        share_url = d.pop("shareUrl", UNSET)

        organization_uuid = d.pop("organizationUuid", UNSET)

        created_by_user_uuid = d.pop("createdByUserUuid", UNSET)

        share_url = cls(
            params=params,
            path=path,
            nanoid=nanoid,
            host=host,
            url=url,
            share_url=share_url,
            organization_uuid=organization_uuid,
            created_by_user_uuid=created_by_user_uuid,
        )

        share_url.additional_properties = d
        return share_url

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
