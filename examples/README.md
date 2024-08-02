# Examples

## Use `.env`

[.env.example](./.env.example) is a template for the `.env` file for the examples.
We copy `.env.example` to `.env` and set the environment variables for your Lightdash environment.

```
# Copy .env.example to .env
cp examples/.env.example .env

# Source .env
source .env

# Run the example
bun run examples/get_my_organization.py
```
