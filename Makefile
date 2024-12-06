# Copyright 2024 yu-iskw
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The latest version in the main branch
LIGHTDASH_VERSION ?= main

# Set up an environment
.PHONEY: setup
setup: setup-python setup-pre-commit

.PHONE: setup-python
setup-python:
	pip install -U pip==24.3.1
	bash ./dev/setup.sh

.PHONE: setup-pre-commit
setup-pre-commit:
	pre-commit install

# Check all the coding style.
.PHONY: lint
lint:
	pre-commit run --all-files

# Run the unit tests.
.PHONEY: test
test:
	bash ./dev/test_python.sh

# Build the package
build: clean lint test
	flit build

clean:
	bash ./dev/clean.sh

# Publish to pypi
publish:
	bash ./dev/publish.sh "pypi"

# Publish to testpypi
test-publish:
	bash ./dev/publish.sh "testpypi"

generate-client:
	rm -fr "lightdash_client/api/" "lightdash_client/models/"
	bash dev/generate_clients.sh

prepare-schema: download-swagger-json dereference-swagger-json

update-client: download-swagger-json dereference-swagger-json generate-client lint

download-swagger-json:
	bash dev/download_swagger_json.sh --version "$(LIGHTDASH_VERSION)"

dereference-swagger-json: build-swagger-cli-image/
	bash dev/dereference_swagger_json.sh

build-swagger-cli-image:
	docker build -t "swagger-cli:latest" -f "docker/swagger-cli/Dockerfile" .
