# Set up an environment
.PHONEY: setup
setup: setup-python setup-pre-commit

.PHONE: setup-python
setup-python:
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

config-schema-json:
	dbt-dependency-graph config-schema --output ./dev/schemas/graph_config.json
