.DEFAULT_GOAL := help

.PHONY: clean-tox
clean-tox: ## Remove tox testing artifacts
	@echo "+ $@"
	@rm -rf .tox/

.PHONY: clean-build
clean-build: ## Remove build artifacts
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

.PHONY: clean-pytest
clean-pytest: ## Remove pytest artifacts
	@echo "+ $@"
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +

.PHONY: clean-coverage
clean-coverage: ## Remove coverage artifacts
	@echo "+ $@"
	@find . -type d -name 'htmlcov' -exec rm -rf {} +
	@coverage erase

.PHONY: clean
clean: clean-tox clean-build clean-pyc clean-pytest clean-coverage ## Remove all file artifacts

.PHONY: clobber-caches
clobber-caches: ## Remove cache for downloaded plugins
	@echo "+ $@"
	@rm -fr .eggs/

.PHONY: clobber
clobber: clean clobber-caches ## Remove all file artifacts and empty caches

.PHONY: lint
lint: ## Check code style
	@echo "+ $@"
	@tox -e lint

.PHONY: test
test: ## Run tests quickly with the default Python
	@echo "+ $@"
	@tox -e py-info

.PHONY: test-all
test-all: ## Run tests on every Python version with tox
	@echo "+ $@"
	@tox

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
