#!/bin/bash
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

# Constants
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
PROJECT_DIR="$(dirname "${SCRIPT_DIR}")"

# Arguments
schema_json="${PROJECT_DIR}/dev/schemas/rebuilt-swagger.json"
config_yaml="${PROJECT_DIR}/dev/openapi-python-client.yml"
output_dir="${PROJECT_DIR}"
meta="setup"
while (($# > 0)); do
  if [[ "$1" == "--schema-json" ]]; then
    schema_json="${2:?}"
    shift 2
  elif [[ "$1" == "--output" ]]; then
    output_dir="${2:?}"
    shift 2
  elif [[ "$1" == "--config" ]]; then
    config_yaml="${2:?}"
    shift 2
  elif [[ "$1" == "--meta" ]]; then
    meta="${2:?}"
    shift 2
  else
    echo "ERROR: Unrecognized argument ${1}" >&2
    exit 1
  fi
done

options=()

# Generate the client in the temporary directory.
temp_dir="$(mktemp -d -t openapi-python-client-XXXXXXXXXX)"
cd "${temp_dir:?}" || exit 1
openapi-python-client generate \
  --path "${schema_json:?}" \
  --config "${config_yaml:?}" \
  --meta "${meta:?}" \
  "${options[@]}"

# Check the generated project
generated_project_dir="${temp_dir:?}/lightdash-client-python"
ls -la "${generated_project_dir:?}"

# Replace the default auth method from Bearer to ApiKey
sed -i -e "s/Bearer/ApiKey/" "${generated_project_dir:?}/lightdash_client/client.py"

# Copy the files
rsync -a -r --delete-after "${generated_project_dir:?}/lightdash_client/models/" "${output_dir:?}/lightdash_client/models/"
rsync -a -r --delete-after "${generated_project_dir:?}/lightdash_client/api/" "${output_dir:?}/lightdash_client/api/"
rsync -a -r --delete-after "${generated_project_dir:?}/lightdash_client/client.py" "${output_dir:?}/lightdash_client/client.py"

# Remove the temporary directory
rm -fr "${temp_dir:?}"
