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
    #!/usr/bin/env bash
    uv sync --locked
    uv run pre-commit uninstall
    uv run pre-commit install --install-hooks

    source .venv/bin/activate
    scripts/sync-scripts.sh

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
    uv run coverage run --source=pytest_lf_skip -m pytest -vv --nf -s
    uv run coverage report --show-missing

# Run tests with coverage. Mainly for CI.
test-cov-build-artifact dist-path="dist/": _uv
    #!/usr/bin/env bash
    install_file=$(ls {{dist-path}}/*.whl)
    uv pip install "$install_file"
    package_name=$(basename "$install_file" | cut -d'-' -f1)
    package_path=$(python -c "import pathlib, $package_name; print(str(pathlib.Path($package_name.__file__).resolve().parent))")
    uv run --no-sync coverage run --source="$package_path" -m pytest -vv --nf
    uv run --no-sync coverage report --show-missing

# Run all pre-commit hooks (this calls the `just check` target)
pre-commit: _pre-commit
    uv run pre-commit run --all-files

build: _uv clean
    # Build the package
    uv build --sdist --wheel

# Release a new version of the package
release: _uv && build gh-publish
    uv run semantic-release -v version --skip-build

# Locally release a new version of the package (mainly for CI)
release-local: _uv
    uv run semantic-release -v version --no-commit --no-push --no-tag --no-vcs-release

# Make a github release using semantic-release
gh-publish: _uv
    uv run semantic-release publish

# Publish the package to PyPI using trusted publishing
pypi-publish: _uv
    uv publish --trusted-publishing always
