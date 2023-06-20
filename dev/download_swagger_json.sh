#!/bin/bash
set -Eeuo pipefail

# Constants
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Arguments
while (($# > 0)); do
  if [[ "$1" == "--version" ]]; then
    lightdash_version="${2}"
    shift 2
  else
    echo "WARN: unrecognized argument ${1}" >&2
    shift 1
  fi
done


# Download swagger.json from the GitHub repository
url="https://raw.githubusercontent.com/lightdash/lightdash/${lightdash_version:?}/packages/backend/src/generated/swagger.json"
curl "${url:?}" --output "${SCRIPT_DIR}/schemas/swagger.json"
