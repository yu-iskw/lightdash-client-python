import os

from lightdash_client.api.organizations import get_my_organization
from lightdash_client.client import AuthenticatedClient

# Usage:
#   export LIGHTDASH_URL="YOUR_LIGHTDASH_URL"
#   export LIGHTDASH_API_KEY="YOUR_API_KEY"
#   python examples/get_my_organization.py


def main():
    client = AuthenticatedClient(
        base_url=os.environ["LIGHTDASH_URL"],
        token=os.environ["LIGHTDASH_API_KEY"],
    )
    response = get_my_organization.sync(client=client)
    print("Organization Name:", response.results.name)
    print("Organization UUID:", response.results.organization_uuid)


if __name__ == "__main__":
    main()
