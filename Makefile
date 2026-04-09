APP_NAME="jericho"
APP_VERSION="0.1.0"
BUILD_DIRECTORY="dist"

.PHONY: setup build run run-debug test package-list package-install package-uninstall coverage sca list

all: setup build

setup:
	@rm -rf ${BUILD_DIRECTORY}/*
	@mkdir -p ${BUILD_DIRECTORY}/

build: setup
	@echo "Building ${APP_NAME} in ${APP_VERSION}..."
	@mkdir -p "${BUILD_DIRECTORY}"

	@poetry run pyinstaller ${APP_NAME}.py --icon="./assets/logo.ico" --onedir -y --clean --log-level ERROR

	@cp ./config.example.json ./${BUILD_DIRECTORY}/${APP_NAME}/config.json
	@echo "Build successful"

run:
	poetry run python .

run-debug:
	poetry run python . --debug

test:
	poetry run pytest

# Handle packages
package-list:
	poetry show --tree

package-install:
	poetry install --no-root

package-uninstall:
	poetry env remove python

coverage:
	poetry run pytest --cov=. --cov-report=html

sca:
	poetry run pip-audit

# list all target in makefile
list:
	@grep '^[^#[:space:]].*:' Makefile | grep -v '\.PHONY'