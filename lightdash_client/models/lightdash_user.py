import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET
from ..types import Unset

if TYPE_CHECKING:
    from ..models.lightdash_user_ability_rules_item import LightdashUserAbilityRulesItem


T = TypeVar("T", bound="LightdashUser")


@attr.s(auto_attribs=True)
class LightdashUser:
    """
    Attributes:
        user_uuid (str):
        first_name (str):
        last_name (str):
        organization_uuid (str):
        organization_name (str):
        is_tracking_anonymized (bool):
        is_marketing_opted_in (bool):
        is_setup_complete (bool):
        role (str):
        email (Union[Unset, str]):
        organization_created_at (Union[Unset, datetime.datetime]):
        ability_rules (Union[Unset, List['LightdashUserAbilityRulesItem']]):
    """

    user_uuid: str
    first_name: str
    last_name: str
    organization_uuid: str
    organization_name: str
    is_tracking_anonymized: bool
    is_marketing_opted_in: bool
    is_setup_complete: bool
    role: str
    email: Union[Unset, str] = UNSET
    organization_created_at: Union[Unset, datetime.datetime] = UNSET
    ability_rules: Union[Unset, List["LightdashUserAbilityRulesItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        user_uuid = self.user_uuid
        first_name = self.first_name
        last_name = self.last_name
        organization_uuid = self.organization_uuid
        organization_name = self.organization_name
        is_tracking_anonymized = self.is_tracking_anonymized
        is_marketing_opted_in = self.is_marketing_opted_in
        is_setup_complete = self.is_setup_complete
        role = self.role
        email = self.email
        organization_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.organization_created_at, Unset):
            organization_created_at = self.organization_created_at.isoformat()

        ability_rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ability_rules, Unset):
            ability_rules = []
            for ability_rules_item_data in self.ability_rules:
                ability_rules_item = ability_rules_item_data.to_dict()

                ability_rules.append(ability_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userUuid": user_uuid,
                "firstName": first_name,
                "lastName": last_name,
                "organizationUuid": organization_uuid,
                "organizationName": organization_name,
                "isTrackingAnonymized": is_tracking_anonymized,
                "isMarketingOptedIn": is_marketing_opted_in,
                "isSetupComplete": is_setup_complete,
                "role": role,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if organization_created_at is not UNSET:
            field_dict["organizationCreatedAt"] = organization_created_at
        if ability_rules is not UNSET:
            field_dict["abilityRules"] = ability_rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lightdash_user_ability_rules_item import LightdashUserAbilityRulesItem

        d = src_dict.copy()
        user_uuid = d.pop("userUuid")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        organization_uuid = d.pop("organizationUuid")

        organization_name = d.pop("organizationName")

        is_tracking_anonymized = d.pop("isTrackingAnonymized")

        is_marketing_opted_in = d.pop("isMarketingOptedIn")

        is_setup_complete = d.pop("isSetupComplete")

        role = d.pop("role")

        email = d.pop("email", UNSET)

        _organization_created_at = d.pop("organizationCreatedAt", UNSET)
        organization_created_at: Union[Unset, datetime.datetime]
        if isinstance(_organization_created_at, Unset):
            organization_created_at = UNSET
        else:
            organization_created_at = isoparse(_organization_created_at)

        ability_rules = []
        _ability_rules = d.pop("abilityRules", UNSET)
        for ability_rules_item_data in _ability_rules or []:
            ability_rules_item = LightdashUserAbilityRulesItem.from_dict(ability_rules_item_data)

            ability_rules.append(ability_rules_item)

        lightdash_user = cls(
            user_uuid=user_uuid,
            first_name=first_name,
            last_name=last_name,
            organization_uuid=organization_uuid,
            organization_name=organization_name,
            is_tracking_anonymized=is_tracking_anonymized,
            is_marketing_opted_in=is_marketing_opted_in,
            is_setup_complete=is_setup_complete,
            role=role,
            email=email,
            organization_created_at=organization_created_at,
            ability_rules=ability_rules,
        )

        return lightdash_user
