from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_pinned_items_status import ApiPinnedItemsStatus

if TYPE_CHECKING:
    from ..models.api_pinned_items_results_item_type_0 import (
        ApiPinnedItemsResultsItemType0,
    )
    from ..models.api_pinned_items_results_item_type_1 import (
        ApiPinnedItemsResultsItemType1,
    )
    from ..models.api_pinned_items_results_item_type_2 import (
        ApiPinnedItemsResultsItemType2,
    )


T = TypeVar("T", bound="ApiPinnedItems")


@attr.s(auto_attribs=True)
class ApiPinnedItems:
    """
    Attributes:
        results (List[Union['ApiPinnedItemsResultsItemType0', 'ApiPinnedItemsResultsItemType1',
            'ApiPinnedItemsResultsItemType2']]):
        status (ApiPinnedItemsStatus):
    """

    results: List[
        Union["ApiPinnedItemsResultsItemType0", "ApiPinnedItemsResultsItemType1", "ApiPinnedItemsResultsItemType2"]
    ]
    status: ApiPinnedItemsStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_pinned_items_results_item_type_0 import (
            ApiPinnedItemsResultsItemType0,
        )
        from ..models.api_pinned_items_results_item_type_1 import (
            ApiPinnedItemsResultsItemType1,
        )

        results = []
        for results_item_data in self.results:
            results_item: Dict[str, Any]

            if isinstance(results_item_data, ApiPinnedItemsResultsItemType0):
                results_item = results_item_data.to_dict()

            elif isinstance(results_item_data, ApiPinnedItemsResultsItemType1):
                results_item = results_item_data.to_dict()

            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_pinned_items_results_item_type_0 import (
            ApiPinnedItemsResultsItemType0,
        )
        from ..models.api_pinned_items_results_item_type_1 import (
            ApiPinnedItemsResultsItemType1,
        )
        from ..models.api_pinned_items_results_item_type_2 import (
            ApiPinnedItemsResultsItemType2,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "ApiPinnedItemsResultsItemType0", "ApiPinnedItemsResultsItemType1", "ApiPinnedItemsResultsItemType2"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = ApiPinnedItemsResultsItemType0.from_dict(data)

                    return results_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_1 = ApiPinnedItemsResultsItemType1.from_dict(data)

                    return results_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_2 = ApiPinnedItemsResultsItemType2.from_dict(data)

                return results_item_type_2

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        status = ApiPinnedItemsStatus(d.pop("status"))

        api_pinned_items = cls(
            results=results,
            status=status,
        )

        api_pinned_items.additional_properties = d
        return api_pinned_items

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
