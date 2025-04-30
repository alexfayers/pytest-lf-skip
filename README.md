# pytest-lf-skip

[![PyPI - Version](https://img.shields.io/pypi/v/pytest-lf-skip)](https://pypi.org/project/pytest-lf-skip/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-lf-skip)](https://pypi.org/project/pytest-lf-skip/)
[![codecov](https://codecov.io/gh/alexfayers/pytest-lf-skip/graph/badge.svg?token=MVADXA06I5)](https://codecov.io/gh/alexfayers/pytest-lf-skip)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/alexfayers/pytest-lf-skip/ci.yml?branch=main&label=CI)](https://github.com/alexfayers/pytest-lf-skip/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/alexfayers/pytest-lf-skip/main.svg)](https://results.pre-commit.ci/latest/github/alexfayers/pytest-lf-skip/main)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-lf-skip)](https://pypistats.org/packages/pytest-lf-skip)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/alexfayers/pytest-lf-skip)](https://github.com/alexfayers/pytest-lf-skip/commits/main/)
[![GitHub last commit](https://img.shields.io/github/last-commit/alexfayers/pytest-lf-skip)](https://github.com/alexfayers/pytest-lf-skip/commits/main/)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/alexfayers/pytest-lf-skip/latest)

A pytest plugin which makes `--last-failed` skip instead of deselect tests.

## Installation

You can install `pytest-lf-skip` from pip:

```bash
pip install pytest-lf-skip
```

## Usage

Just add the `--lf-skip` or `--last-failed-skip` argument to your pytest command when you use `--last-failed`:

```bash
pytest --last-failed --last-failed-skip
```

Now previously passed tests will be skipped instead of being deselected.

### VS Code

If you are using VS Code, you can make use of the `--auto-last-failed-skip-vscode` argument, which will automatically enable `--lf` and `--lf-skip` when running tests from the VS Code test explorer.

To enable this, add the following to your `settings.json`:

```json
{
    "python.testing.pytestArgs": [
        "--auto-last-failed-skip-vscode",
    ]
}
```
