from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.local_issuer_types import LocalIssuerTypes
from ..models.open_id_identity_issuer_type import OpenIdIdentityIssuerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginOptions")


@_attrs_define
class LoginOptions:
    """
    Attributes:
        show_options (List[Union[LocalIssuerTypes, OpenIdIdentityIssuerType]]):
        redirect_uri (Union[Unset, str]):
        force_redirect (Union[Unset, bool]):
    """

    show_options: List[Union[LocalIssuerTypes, OpenIdIdentityIssuerType]]
    redirect_uri: Union[Unset, str] = UNSET
    force_redirect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        show_options = []
        for show_options_item_data in self.show_options:
            show_options_item: str
            if isinstance(show_options_item_data, OpenIdIdentityIssuerType):
                show_options_item = show_options_item_data.value
            else:
                show_options_item = show_options_item_data.value

            show_options.append(show_options_item)

        redirect_uri = self.redirect_uri

        force_redirect = self.force_redirect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "showOptions": show_options,
            }
        )
        if redirect_uri is not UNSET:
            field_dict["redirectUri"] = redirect_uri
        if force_redirect is not UNSET:
            field_dict["forceRedirect"] = force_redirect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        show_options = []
        _show_options = d.pop("showOptions")
        for show_options_item_data in _show_options:

            def _parse_show_options_item(data: object) -> Union[LocalIssuerTypes, OpenIdIdentityIssuerType]:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    componentsschemas_login_option_types_type_0 = OpenIdIdentityIssuerType(data)

                    return componentsschemas_login_option_types_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_login_option_types_type_1 = LocalIssuerTypes(data)

                return componentsschemas_login_option_types_type_1

            show_options_item = _parse_show_options_item(show_options_item_data)

            show_options.append(show_options_item)

        redirect_uri = d.pop("redirectUri", UNSET)

        force_redirect = d.pop("forceRedirect", UNSET)

        login_options = cls(
            show_options=show_options,
            redirect_uri=redirect_uri,
            force_redirect=force_redirect,
        )

        login_options.additional_properties = d
        return login_options

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
