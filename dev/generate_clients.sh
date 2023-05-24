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
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Arguments
output_dir="${PROJECT_DIR}/lightdash_client"
schema_json="${PROJECT_DIR}/dev/schemas/lightdash-api.json"
while (($# > 0)); do
  if [[ "$1" == "--output" ]]; then
    output_dir="${2:?}"
    shift 2
  elif [[ "$1" == "--schema-json" ]]; then
    schema_json="${2:?}"
    shift 2
  else
    echo "ERROR: Unrecognized argument ${1}" >&2
    exit 1
  fi
done

openapi-generator generate \
  --input-spec "${schema_json}" \
  --generator-name python \
  --output "${output_dir}" --skip-validate-spec --api-package "lightdash_client"
#  --config "${PROJECT_DIR}/dev/openapi-generator-config.json" \
#  --skip-validate-spec
