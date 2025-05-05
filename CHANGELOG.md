# CHANGELOG


## v0.3.0 (2025-05-05)

### Chores

- :pushpin: Update uv.lock ([#13](https://github.com/alexfayers/pytest-lf-skip/pull/13),
  [`80e5982`](https://github.com/alexfayers/pytest-lf-skip/commit/80e59823f4502c92a879454a75921ecd901b25b6))

- Add dependabot.yml ([#24](https://github.com/alexfayers/pytest-lf-skip/pull/24),
  [`30989ce`](https://github.com/alexfayers/pytest-lf-skip/commit/30989cefc30a4213dbfa1600240f8b02d3a60944))

- Update dependabot.yml to use uv ([#31](https://github.com/alexfayers/pytest-lf-skip/pull/31),
  [`37ba215`](https://github.com/alexfayers/pytest-lf-skip/commit/37ba2150df5602f3b8a8163e767bd0acbc75dda4))

- **just**: Add publish to release steps
  ([#20](https://github.com/alexfayers/pytest-lf-skip/pull/20),
  [`69d2987`](https://github.com/alexfayers/pytest-lf-skip/commit/69d298779bd17ef5ab5aa43a8bf4d101166863ad))

- **just**: Uninstall pre-commit hooks before installing them
  ([#14](https://github.com/alexfayers/pytest-lf-skip/pull/14),
  [`84b1ff9`](https://github.com/alexfayers/pytest-lf-skip/commit/84b1ff9b4732568b0dc7ba5b0217407223b8c604))

### Continuous Integration

- :construction_worker: Update order of build/release steps
  ([#13](https://github.com/alexfayers/pytest-lf-skip/pull/13),
  [`80e5982`](https://github.com/alexfayers/pytest-lf-skip/commit/80e59823f4502c92a879454a75921ecd901b25b6))

- Add all directories as safe for git ([#17](https://github.com/alexfayers/pytest-lf-skip/pull/17),
  [`8c40070`](https://github.com/alexfayers/pytest-lf-skip/commit/8c40070dc507d2cfaab101279c7561b5da50662c))

- Add cache step for pre-commit in linting step
  ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Add environment specification for semantic release
  ([#21](https://github.com/alexfayers/pytest-lf-skip/pull/21),
  [`0eed1c7`](https://github.com/alexfayers/pytest-lf-skip/commit/0eed1c76eeb5fa236e6a91518d426333468b8af5))

- Adjust CI release workflow to use a dedicated workflow file
  ([#15](https://github.com/alexfayers/pytest-lf-skip/pull/15),
  [`481d1e5`](https://github.com/alexfayers/pytest-lf-skip/commit/481d1e55ff7b1bb6edfcc706dc531d33944532ac))

- Bump version of create-github-app-token
  ([#21](https://github.com/alexfayers/pytest-lf-skip/pull/21),
  [`0eed1c7`](https://github.com/alexfayers/pytest-lf-skip/commit/0eed1c76eeb5fa236e6a91518d426333468b8af5))

- Ensure tags are checked out in build semantic-release step
  ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Implement setup action for environment configuration and dependency management
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))

- Remove codecov ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Remove explicit safe directory setting
  ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Set fetch-depth to 0 for jobs that need git tags
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))

- Set GH_TOKEN for Python Semantic Release workflow step
  ([#16](https://github.com/alexfayers/pytest-lf-skip/pull/16),
  [`08e34aa`](https://github.com/alexfayers/pytest-lf-skip/commit/08e34aa39b020130e62833541ece47506097da34))

- Update environments for finer grain release control
  ([#22](https://github.com/alexfayers/pytest-lf-skip/pull/22),
  [`d5509c1`](https://github.com/alexfayers/pytest-lf-skip/commit/d5509c127560f96d156236258ab230b276c158cb))

- Use `uv publish` for release ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Use alexfayers-py-publisher for releasing
  ([#20](https://github.com/alexfayers/pytest-lf-skip/pull/20),
  [`69d2987`](https://github.com/alexfayers/pytest-lf-skip/commit/69d298779bd17ef5ab5aa43a8bf4d101166863ad))

- Use official python-semantic-release actions
  ([#20](https://github.com/alexfayers/pytest-lf-skip/pull/20),
  [`69d2987`](https://github.com/alexfayers/pytest-lf-skip/commit/69d298779bd17ef5ab5aa43a8bf4d101166863ad))

### Features

- Start using dynamic versioning ([#14](https://github.com/alexfayers/pytest-lf-skip/pull/14),
  [`84b1ff9`](https://github.com/alexfayers/pytest-lf-skip/commit/84b1ff9b4732568b0dc7ba5b0217407223b8c604))

start using dynamic versioning to calculate the package version number from git tags

### Testing

- Add package version test ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Adjust test_package_version to include more versions
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))

- Enhance version assertion message in test_package_version for clarity on failure
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))


## v0.2.4 (2025-05-01)

### Chores

- :wrench: Remove post hooks from pre-commit config
  ([#11](https://github.com/alexfayers/pytest-lf-skip/pull/11),
  [`fb30f0d`](https://github.com/alexfayers/pytest-lf-skip/commit/fb30f0de6c17d634a45d8ff2bcc88226ea65db07))

They were annoying

### Continuous Integration

- :construction_worker: Add codecov step to CI
  ([#12](https://github.com/alexfayers/pytest-lf-skip/pull/12),
  [`23b7e61`](https://github.com/alexfayers/pytest-lf-skip/commit/23b7e610f61dcaed648520578d9f8d8912508ef2))

### Documentation

- :memo: Add new PyPi classifiers ([#12](https://github.com/alexfayers/pytest-lf-skip/pull/12),
  [`23b7e61`](https://github.com/alexfayers/pytest-lf-skip/commit/23b7e610f61dcaed648520578d9f8d8912508ef2))

- :sparkles: Add loads of new badges to the readme!
  ([#12](https://github.com/alexfayers/pytest-lf-skip/pull/12),
  [`23b7e61`](https://github.com/alexfayers/pytest-lf-skip/commit/23b7e610f61dcaed648520578d9f8d8912508ef2))

- Update usage instructions in README.md
  ([#10](https://github.com/alexfayers/pytest-lf-skip/pull/10),
  [`9a3f8dd`](https://github.com/alexfayers/pytest-lf-skip/commit/9a3f8ddf080fcabee3003be2f7bf30d07e225aa0))


## v0.2.3 (2025-04-25)

### Bug Fixes

- :construction_worker: Set path on `Download build artifacts` step in release
  ([`a9781e7`](https://github.com/alexfayers/pytest-lf-skip/commit/a9781e71215f9e9a89ad1cd66f0126e694c5a4bc))


## v0.2.2 (2025-04-25)

### Bug Fixes

- :bug: Fix clean failing if dist file doesn't exist
  ([`cf1c0b8`](https://github.com/alexfayers/pytest-lf-skip/commit/cf1c0b8baa345eb1467d0426660f4bc5b6ac67d7))


## v0.2.1 (2025-04-25)

### Bug Fixes

- :wrench: Fix dist_glob_patterns pattern for release artifacts
  ([#8](https://github.com/alexfayers/pytest-lf-skip/pull/8),
  [`fea0fae`](https://github.com/alexfayers/pytest-lf-skip/commit/fea0fae4747c926b4a3bf132507d34bed794b29b))

- :wrench: Fix release CI stage not running
  ([#8](https://github.com/alexfayers/pytest-lf-skip/pull/8),
  [`fea0fae`](https://github.com/alexfayers/pytest-lf-skip/commit/fea0fae4747c926b4a3bf132507d34bed794b29b))

### Chores

- :wrench: Add just release entry ([#8](https://github.com/alexfayers/pytest-lf-skip/pull/8),
  [`fea0fae`](https://github.com/alexfayers/pytest-lf-skip/commit/fea0fae4747c926b4a3bf132507d34bed794b29b))

### Continuous Integration

- :construction_worker: Add build and release steps for CI
  ([#8](https://github.com/alexfayers/pytest-lf-skip/pull/8),
  [`fea0fae`](https://github.com/alexfayers/pytest-lf-skip/commit/fea0fae4747c926b4a3bf132507d34bed794b29b))


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
