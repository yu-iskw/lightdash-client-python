#!/bin/bash
set -Eeuo pipefail

# Constants
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Arguments
docker_image="swagger-cli:latest"
while (($# > 0)); do
  if [[ "$1" == "--image" ]]; then
    docker_image="${2}"
    shift 2
  else
    echo "WARN: unrecognized argument ${1}" >&2
    shift 1
  fi
done


# NOTE The --output option doesn't work with swagger-cli. Instead, use the '-o' option.
mounted_dir="/data"
docker run --rm -v "${SCRIPT_DIR:?}/schemas:${mounted_dir}" "${docker_image:?}" \
  bundle --dereference -o "${mounted_dir}/dereferenced-swagger.json" "${mounted_dir:?}/swagger.json"
