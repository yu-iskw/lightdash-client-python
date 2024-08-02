from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_basic_details import DashboardBasicDetails
    from ..models.space_group import SpaceGroup
    from ..models.space_query import SpaceQuery
    from ..models.space_share import SpaceShare


T = TypeVar("T", bound="Space")


@_attrs_define
class Space:
    """
    Attributes:
        slug (str):
        pinned_list_order (Union[None, float]):
        pinned_list_uuid (Union[None, str]):
        groups_access (List['SpaceGroup']):
        access (List['SpaceShare']):
        dashboards (List['DashboardBasicDetails']):
        project_uuid (str):
        queries (List['SpaceQuery']):
        is_private (bool):
        name (str):
        uuid (str):
        organization_uuid (str):
    """

    slug: str
    pinned_list_order: Union[None, float]
    pinned_list_uuid: Union[None, str]
    groups_access: List["SpaceGroup"]
    access: List["SpaceShare"]
    dashboards: List["DashboardBasicDetails"]
    project_uuid: str
    queries: List["SpaceQuery"]
    is_private: bool
    name: str
    uuid: str
    organization_uuid: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug

        pinned_list_order: Union[None, float]
        pinned_list_order = self.pinned_list_order

        pinned_list_uuid: Union[None, str]
        pinned_list_uuid = self.pinned_list_uuid

        groups_access = []
        for groups_access_item_data in self.groups_access:
            groups_access_item = groups_access_item_data.to_dict()
            groups_access.append(groups_access_item)

        access = []
        for access_item_data in self.access:
            access_item = access_item_data.to_dict()
            access.append(access_item)

        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()
            dashboards.append(dashboards_item)

        project_uuid = self.project_uuid

        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        is_private = self.is_private

        name = self.name

        uuid = self.uuid

        organization_uuid = self.organization_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "pinnedListOrder": pinned_list_order,
                "pinnedListUuid": pinned_list_uuid,
                "groupsAccess": groups_access,
                "access": access,
                "dashboards": dashboards,
                "projectUuid": project_uuid,
                "queries": queries,
                "isPrivate": is_private,
                "name": name,
                "uuid": uuid,
                "organizationUuid": organization_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dashboard_basic_details import DashboardBasicDetails
        from ..models.space_group import SpaceGroup
        from ..models.space_query import SpaceQuery
        from ..models.space_share import SpaceShare

        d = src_dict.copy()
        slug = d.pop("slug")

        def _parse_pinned_list_order(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        pinned_list_order = _parse_pinned_list_order(d.pop("pinnedListOrder"))

        def _parse_pinned_list_uuid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pinned_list_uuid = _parse_pinned_list_uuid(d.pop("pinnedListUuid"))

        groups_access = []
        _groups_access = d.pop("groupsAccess")
        for groups_access_item_data in _groups_access:
            groups_access_item = SpaceGroup.from_dict(groups_access_item_data)

            groups_access.append(groups_access_item)

        access = []
        _access = d.pop("access")
        for access_item_data in _access:
            access_item = SpaceShare.from_dict(access_item_data)

            access.append(access_item)

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = DashboardBasicDetails.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        project_uuid = d.pop("projectUuid")

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = SpaceQuery.from_dict(queries_item_data)

            queries.append(queries_item)

        is_private = d.pop("isPrivate")

        name = d.pop("name")

        uuid = d.pop("uuid")

        organization_uuid = d.pop("organizationUuid")

        space = cls(
            slug=slug,
            pinned_list_order=pinned_list_order,
            pinned_list_uuid=pinned_list_uuid,
            groups_access=groups_access,
            access=access,
            dashboards=dashboards,
            project_uuid=project_uuid,
            queries=queries,
            is_private=is_private,
            name=name,
            uuid=uuid,
            organization_uuid=organization_uuid,
        )

        space.additional_properties = d
        return space

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
