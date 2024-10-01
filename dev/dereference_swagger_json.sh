#!/bin/bash
set -Eeuo pipefail

# Constants
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Arguments
docker_image="redocly/cli:latest"
output_file="rebuilt-swagger.json"
while (($# > 0)); do
  if [[ "$1" == "--image" ]]; then
    docker_image="${2}"
    shift 2
  elif [[ "$1" == "--output" ]]; then
    output_file="${2}"
    shift 2
  else
    echo "WARN: unrecognized argument ${1}" >&2
    shift 1
  fi
done

# Remove the split-swagger directory if it exists
rm -fr "${SCRIPT_DIR:?}/schemas/split-swagger"

# Split the swagger.json into multiple files to handle recursive references
docker run --rm -v "${SCRIPT_DIR:?}/schemas:/spec" "${docker_image:?}" \
  split --outDir /spec/split-swagger /spec/swagger.json

# Bundle the split swagger.json files into a single file again
docker run --rm -v "${SCRIPT_DIR:?}/schemas:/spec" "${docker_image:?}" \
  bundle --output "/spec/${output_file}" /spec/split-swagger/openapi.json
