# CHANGELOG


## v0.2.0 (2025-04-25)

### Bug Fixes

- :wrench: Update version_variables to point to correct path
  ([#5](https://github.com/alexfayers/pytest-lf-skip/pull/5),
  [`6837f22`](https://github.com/alexfayers/pytest-lf-skip/commit/6837f22f0f18f7084e50bf764fc79bb57d743d9d))

### Chores

- :wrench: Enable parse_squash_commits for semantic_release
  ([#4](https://github.com/alexfayers/pytest-lf-skip/pull/4),
  [`93cf5aa`](https://github.com/alexfayers/pytest-lf-skip/commit/93cf5aa73d94591a99a6032bc5670628c6f7c10e))

- :wrench: Remove no-commit-to-branch pre-commit, it was creating false positives and is now
  enforced with branch protection rules
  ([`2f049ff`](https://github.com/alexfayers/pytest-lf-skip/commit/2f049ff8a8c9402806ea75ac50edb1b839520d55))

- :wrench: Update semantic_release build process
  ([#7](https://github.com/alexfayers/pytest-lf-skip/pull/7),
  [`5a3f5d1`](https://github.com/alexfayers/pytest-lf-skip/commit/5a3f5d14cd5e86c4dadfa393432cad54b45c2d87))

Add build and clean commands to justfile and use build in semantic_release `build_command`

- **format**: :art: Reformat pyproject.toml
  ([#3](https://github.com/alexfayers/pytest-lf-skip/pull/3),
  [`2322c5d`](https://github.com/alexfayers/pytest-lf-skip/commit/2322c5d1e52f2147c8566730893c3cbc3fc29f49))

- **tooling**: :heavy_plus_sign: Add python-semantic-release
  ([`d10f106`](https://github.com/alexfayers/pytest-lf-skip/commit/d10f106022fe14efa93ec14f1842952bed548dba))

Add python-semantic-release and initial configuration for it

- **tooling**: :wrench: Update semantic_release commit message format
  ([`7f05a81`](https://github.com/alexfayers/pytest-lf-skip/commit/7f05a814987fb32dd70e4165545f3c50c2f025ce))

Add :bookmark: to the start of the auto-commits for consistency

### Continuous Integration

- :construction_worker: Add initial GitHub actions
  ([#3](https://github.com/alexfayers/pytest-lf-skip/pull/3),
  [`2322c5d`](https://github.com/alexfayers/pytest-lf-skip/commit/2322c5d1e52f2147c8566730893c3cbc3fc29f49))

Will run linting, typechecking, and tests

### Documentation

- :memo: Add project URLs to pyproject.toml
  ([#6](https://github.com/alexfayers/pytest-lf-skip/pull/6),
  [`684f0d3`](https://github.com/alexfayers/pytest-lf-skip/commit/684f0d318389d4f334586cb5e667f72a487ca18e))

### Features

- **tooling**: :wrench: Enforce conventional commits via pre-commit
  ([`d10f106`](https://github.com/alexfayers/pytest-lf-skip/commit/d10f106022fe14efa93ec14f1842952bed548dba))

Add `compilerla/conventional-pre-commit` pre-commit hook to enforce conventional commit format


## v0.1.1 (2025-04-16)
