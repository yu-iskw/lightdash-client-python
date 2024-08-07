# Set up an environment
.PHONEY: setup
setup: setup-python setup-pre-commit

.PHONE: setup-python
setup-python:
	pip install -U pip==23.1.0
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
	bash dev/generate_clients.sh --skip-validate-spec 1

prepare-schema: download-swagger-json dereference-swagger-json

download-swagger-json: check-lightdash-version
	bash dev/download_swagger_json.sh --version "$(VERSION)"

dereference-swagger-json: build-swagger-cli-image
	bash dev/dereference_swagger_json.sh

build-swagger-cli-image:
	docker build -t "swagger-cli:latest" -f "docker/swagger-cli/Dockerfile" .

check-lightdash-version:
ifndef VERSION
	$(error VERSION is undefined)
endif
