from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_pinned_items_order_response_200_status import (
    UpdatePinnedItemsOrderResponse200Status,
)

if TYPE_CHECKING:
    from ..models.update_pinned_items_order_response_200_results_item_type_0 import (
        UpdatePinnedItemsOrderResponse200ResultsItemType0,
    )
    from ..models.update_pinned_items_order_response_200_results_item_type_1 import (
        UpdatePinnedItemsOrderResponse200ResultsItemType1,
    )
    from ..models.update_pinned_items_order_response_200_results_item_type_2 import (
        UpdatePinnedItemsOrderResponse200ResultsItemType2,
    )


T = TypeVar("T", bound="UpdatePinnedItemsOrderResponse200")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderResponse200:
    """
    Attributes:
        results (List[Union['UpdatePinnedItemsOrderResponse200ResultsItemType0',
            'UpdatePinnedItemsOrderResponse200ResultsItemType1', 'UpdatePinnedItemsOrderResponse200ResultsItemType2']]):
        status (UpdatePinnedItemsOrderResponse200Status):
    """

    results: List[
        Union[
            "UpdatePinnedItemsOrderResponse200ResultsItemType0",
            "UpdatePinnedItemsOrderResponse200ResultsItemType1",
            "UpdatePinnedItemsOrderResponse200ResultsItemType2",
        ]
    ]
    status: UpdatePinnedItemsOrderResponse200Status
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.update_pinned_items_order_response_200_results_item_type_0 import (
            UpdatePinnedItemsOrderResponse200ResultsItemType0,
        )
        from ..models.update_pinned_items_order_response_200_results_item_type_1 import (
            UpdatePinnedItemsOrderResponse200ResultsItemType1,
        )

        results = []
        for results_item_data in self.results:
            results_item: Dict[str, Any]

            if isinstance(results_item_data, UpdatePinnedItemsOrderResponse200ResultsItemType0):
                results_item = results_item_data.to_dict()

            elif isinstance(results_item_data, UpdatePinnedItemsOrderResponse200ResultsItemType1):
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
        from ..models.update_pinned_items_order_response_200_results_item_type_0 import (
            UpdatePinnedItemsOrderResponse200ResultsItemType0,
        )
        from ..models.update_pinned_items_order_response_200_results_item_type_1 import (
            UpdatePinnedItemsOrderResponse200ResultsItemType1,
        )
        from ..models.update_pinned_items_order_response_200_results_item_type_2 import (
            UpdatePinnedItemsOrderResponse200ResultsItemType2,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "UpdatePinnedItemsOrderResponse200ResultsItemType0",
                "UpdatePinnedItemsOrderResponse200ResultsItemType1",
                "UpdatePinnedItemsOrderResponse200ResultsItemType2",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = UpdatePinnedItemsOrderResponse200ResultsItemType0.from_dict(data)

                    return results_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_1 = UpdatePinnedItemsOrderResponse200ResultsItemType1.from_dict(data)

                    return results_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_2 = UpdatePinnedItemsOrderResponse200ResultsItemType2.from_dict(data)

                return results_item_type_2

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        status = UpdatePinnedItemsOrderResponse200Status(d.pop("status"))

        update_pinned_items_order_response_200 = cls(
            results=results,
            status=status,
        )

        update_pinned_items_order_response_200.additional_properties = d
        return update_pinned_items_order_response_200

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
