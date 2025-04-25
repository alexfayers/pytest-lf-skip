# pytest-lf-skip

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
