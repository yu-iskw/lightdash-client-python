from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.space_share import SpaceShare


T = TypeVar("T", bound="SpaceSummary")


@_attrs_define
class SpaceSummary:
    """
    Attributes:
        name (str):
        uuid (str):
        project_uuid (str):
        organization_uuid (str):
        pinned_list_uuid (Union[None, str]):
        is_private (bool):
        pinned_list_order (Union[None, float]):
        slug (str):
        dashboard_count (float):
        chart_count (float):
        access (List[str]):
        user_access (Union[Unset, SpaceShare]):
    """

    name: str
    uuid: str
    project_uuid: str
    organization_uuid: str
    pinned_list_uuid: Union[None, str]
    is_private: bool
    pinned_list_order: Union[None, float]
    slug: str
    dashboard_count: float
    chart_count: float
    access: List[str]
    user_access: Union[Unset, "SpaceShare"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        uuid = self.uuid

        project_uuid = self.project_uuid

        organization_uuid = self.organization_uuid

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        is_private = self.is_private

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        slug = self.slug

        dashboard_count = self.dashboard_count

        chart_count = self.chart_count

        access = self.access

        user_access: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_access, Unset):
            user_access = self.user_access.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uuid": uuid,
                "projectUuid": project_uuid,
                "organizationUuid": organization_uuid,
                "pinnedListUuid": pinned_list_uuid,
                "isPrivate": is_private,
                "pinnedListOrder": pinned_list_order,
                "slug": slug,
                "dashboardCount": dashboard_count,
                "chartCount": chart_count,
                "access": access,
            }
        )
        if user_access is not UNSET:
            field_dict["userAccess"] = user_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.space_share import SpaceShare

        d = src_dict.copy()
        name = d.pop("name")

        uuid = d.pop("uuid")

        project_uuid = d.pop("projectUuid")

        organization_uuid = d.pop("organizationUuid")

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        is_private = d.pop("isPrivate")

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        slug = d.pop("slug")

        dashboard_count = d.pop("dashboardCount")

        chart_count = d.pop("chartCount")

        access = cast(List[str], d.pop("access"))

        _user_access = d.pop("userAccess", UNSET)
        user_access: Union[Unset, SpaceShare]
        if isinstance(_user_access, Unset):
            user_access = UNSET
        else:
            user_access = SpaceShare.from_dict(_user_access)

        space_summary = cls(
            name=name,
            uuid=uuid,
            project_uuid=project_uuid,
            organization_uuid=organization_uuid,
            pinned_list_uuid=pinned_list_uuid,
            is_private=is_private,
            pinned_list_order=pinned_list_order,
            slug=slug,
            dashboard_count=dashboard_count,
            chart_count=chart_count,
            access=access,
            user_access=user_access,
        )

        space_summary.additional_properties = d
        return space_summary

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
