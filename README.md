# pytest-lf-skip

A pytest plugin which makes --last-failed skip instead of deselect tests.

## Installation

You can install `pytest-lf-skip` from pip:

```bash
pip install pytest-lf-skip
```

## Usage

First, install the plugin.

Then add the `--lf-skip` or `--last-failed-skip` argument to your pytest command when you use `--last-failed`:

```bash
pytest --last-failed --last-failed-skip
```
