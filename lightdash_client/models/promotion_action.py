from enum import Enum


class PromotionAction(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    NO_CHANGES = "no changes"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
