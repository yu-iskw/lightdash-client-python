from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.space_access_item import SpaceAccessItem
    from ..models.space_dashboards_item import SpaceDashboardsItem
    from ..models.space_queries_item import SpaceQueriesItem


T = TypeVar("T", bound="Space")


@attr.s(auto_attribs=True)
class Space:
    """
    Attributes:
        access (List['SpaceAccessItem']):
        dashboards (List['SpaceDashboardsItem']):
        project_uuid (str):
        queries (List['SpaceQueriesItem']):
        is_private (bool):
        name (str):
        uuid (str):
        organization_uuid (str):
        pinned_list_order (Optional[float]):
        pinned_list_uuid (Optional[str]):
    """

    access: List["SpaceAccessItem"]
    dashboards: List["SpaceDashboardsItem"]
    project_uuid: str
    queries: List["SpaceQueriesItem"]
    is_private: bool
    name: str
    uuid: str
    organization_uuid: str
    pinned_list_order: Optional[float]
    pinned_list_uuid: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        pinned_list_order = self.pinned_list_order
        pinned_list_uuid = self.pinned_list_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "dashboards": dashboards,
                "projectUuid": project_uuid,
                "queries": queries,
                "isPrivate": is_private,
                "name": name,
                "uuid": uuid,
                "organizationUuid": organization_uuid,
                "pinnedListOrder": pinned_list_order,
                "pinnedListUuid": pinned_list_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.space_access_item import SpaceAccessItem
        from ..models.space_dashboards_item import SpaceDashboardsItem
        from ..models.space_queries_item import SpaceQueriesItem

        d = src_dict.copy()
        access = []
        _access = d.pop("access")
        for access_item_data in _access:
            access_item = SpaceAccessItem.from_dict(access_item_data)

            access.append(access_item)

        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = SpaceDashboardsItem.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        project_uuid = d.pop("projectUuid")

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = SpaceQueriesItem.from_dict(queries_item_data)

            queries.append(queries_item)

        is_private = d.pop("isPrivate")

        name = d.pop("name")

        uuid = d.pop("uuid")

        organization_uuid = d.pop("organizationUuid")

        pinned_list_order = d.pop("pinnedListOrder")

        pinned_list_uuid = d.pop("pinnedListUuid")

        space = cls(
            access=access,
            dashboards=dashboards,
            project_uuid=project_uuid,
            queries=queries,
            is_private=is_private,
            name=name,
            uuid=uuid,
            organization_uuid=organization_uuid,
            pinned_list_order=pinned_list_order,
            pinned_list_uuid=pinned_list_uuid,
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
