from enum import Enum


class OpenIdIdentityIssuerType(str, Enum):
    AZUREAD = "azuread"
    GOOGLE = "google"
    OIDC = "oidc"
    OKTA = "okta"
    ONELOGIN = "oneLogin"

    def __str__(self) -> str:
        return str(self.value)
