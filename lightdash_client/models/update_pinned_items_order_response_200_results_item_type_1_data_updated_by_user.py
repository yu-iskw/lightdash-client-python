from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar

import attr

T = TypeVar("T", bound="UpdatePinnedItemsOrderResponse200ResultsItemType1DataUpdatedByUser")


@attr.s(auto_attribs=True)
class UpdatePinnedItemsOrderResponse200ResultsItemType1DataUpdatedByUser:
    """
    Attributes:
        user_uuid (str):
        first_name (str):
        last_name (str):
    """

    user_uuid: str
    first_name: str
    last_name: str

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid
        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userUuid": user_uuid,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        update_pinned_items_order_response_200_results_item_type_1_data_updated_by_user = cls(
            user_uuid=user_uuid,
            first_name=first_name,
            last_name=last_name,
        )

        return update_pinned_items_order_response_200_results_item_type_1_data_updated_by_user
