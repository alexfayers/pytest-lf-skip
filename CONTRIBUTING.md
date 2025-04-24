# Contributing

## Prerequisites

- Python >= 3.10 installed
- `uv` installed (`pipx install uv`)
- `just` installed (`uv tool install rust-just`)

## Development

1. Fork the repository on GitHub and clone it to your local machine

```bash
git clone https://github.com/<your-username>/pytest-lf-skip
cd pytest-lf-skip
```

2. Install the project using `just`

```bash
just install
```

3. Checkout a new branch and make your changes

```bash
git checkout -b my-feature-branch
# Make your changes here...
```

4. Run tests and linters

```bash
# Format the code
just format
# Run linters, type checks, and tests
just
```

5. Commit and push your changes

Commit your changes with a descriptive message and push to your forked repository. Then create a pull request against the main repository.

6. Wait for review

Once you have created the pull request, wait for me to review your changes. I might ask for changes or clarifications before merging :)
