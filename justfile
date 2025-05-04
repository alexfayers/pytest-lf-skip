# Run linting/formatting, type checking, and tests
@_default: format type-check pre-commit test-cov

# Run all linters and type checkers
check: lint type-check

# make sure uv is installed
@_uv:
    uv -V 2> /dev/null || { echo '{{RED}}Please install uv: https://docs.astral.sh/uv/getting-started/installation/'; exit 1;}

# make sure pre-commit is installed
@_pre-commit: _uv
    uv run pre-commit -V 2> /dev/null || uv pip install pre-commit

# Install the package, development dependencies and pre-commit hooks
install: _uv _pre-commit
    uv sync --locked
    uv run pre-commit uninstall
    uv run pre-commit install --install-hooks

clean:
    # Remove all build artifacts
    rm -rf dist/

# Run all linters against the codebase
lint: _uv
    uv run ruff check
    uv run ruff format --check
    uv run pyproject-fmt --check pyproject.toml
    uv run codespell

# Run all linters and formatters against the codebase, fixing any issues
format: _uv
    uv run ruff check --fix --show-fixes
    uv run ruff format
    uv run pyproject-fmt pyproject.toml
    uv run codespell --write-changes

# Run all type checkers against the codebase
type-check: _uv
    uv run mypy

# Run all tests
test: _uv
    uv run pytest -vv --nf

# Run tests with coverage
test-cov: _uv
    uv run pytest -vv --nf --cov=src --cov-report=term-missing

# Run all pre-commit hooks (this calls the `just check` target)
pre-commit: _pre-commit
    uv run pre-commit run --all-files

build: _uv clean
    # Build the package
    uv build --sdist --wheel

# Release a new version of the package
release: _uv
    uv run semantic-release version
    uv run semantic-release publish

# Release a new version of the package without building first
release-no-build: _uv
    uv run semantic-release version --skip-build
    uv run semantic-release publish
