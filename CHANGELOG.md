# CHANGELOG


## v0.4.0 (2025-05-18)

### Build System

- **just**: Update coverage commands to use coverage directly
  ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))

### Chores

- Add coverage as a direct test dependency
  ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))

- Ensure validation job only runs for non-cd bot users
  ([#79](https://github.com/alexfayers/pytest-lf-skip/pull/79),
  [`32dfcdf`](https://github.com/alexfayers/pytest-lf-skip/commit/32dfcdff45c63ecb1d0dd7f44935c08989f57d8d))

### Code Style

- Update coverage version constraint in test dependencies
  ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))

### Continuous Integration

- Make commitlint validation only run for PRs
  ([#81](https://github.com/alexfayers/pytest-lf-skip/pull/81),
  [`4c42117`](https://github.com/alexfayers/pytest-lf-skip/commit/4c421173df8cda2bd575c2bd1f694ff9fc243bd3))

### Features

- Add optional logging to the plugin ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))

### Testing

- Add pragma comment to exception handling and factory_test_plugin to improve coverage
  ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))

- Add warnings and logging tests for LF skip functionality
  ([#80](https://github.com/alexfayers/pytest-lf-skip/pull/80),
  [`0c5ee73`](https://github.com/alexfayers/pytest-lf-skip/commit/0c5ee73dbc2e8a9556684a95fd80746ad627b763))


## v0.3.1 (2025-05-18)

### Bug Fixes

- Update publish glob pattern so release artifacts actually get added to github
  ([#67](https://github.com/alexfayers/pytest-lf-skip/pull/67),
  [`0ce91a2`](https://github.com/alexfayers/pytest-lf-skip/commit/0ce91a261d0c533607182d2245f6b2ab427c1792))

- **ci**: Don't skip ci on release ([#71](https://github.com/alexfayers/pytest-lf-skip/pull/71),
  [`1d275f7`](https://github.com/alexfayers/pytest-lf-skip/commit/1d275f798121b3ecd85f4fc8bfaa81698ee2c4b2))

### Build System

- Update commit message format and exclude old pattern for semantic release
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- **just**: Update test-cov-build-artifact recipe to call pytest with uv
  ([#61](https://github.com/alexfayers/pytest-lf-skip/pull/61),
  [`bb85282`](https://github.com/alexfayers/pytest-lf-skip/commit/bb852828a6fa68405182a6081470f6b49eeea79e))

- **just**: Use sync-scripts in `just install`
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

- **pre-commit**: Remove uv-export hook to prevent generation of requirements.txt
  ([#65](https://github.com/alexfayers/pytest-lf-skip/pull/65),
  [`49a1cbe`](https://github.com/alexfayers/pytest-lf-skip/commit/49a1cbe6bf1b9a4f67c8ccc5d83333714b7443ec))

- **scripts**: Add conventional commit message validation script
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

- **scripts**: Add script dependency management and commit message validation
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

- **scripts**: Add sync-scripts.sh file to add script deps to venv
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

- **scripts**: Adjust get_supported_py_versions header
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

### Chores

- Add initial commitlint configuration to ignore specific commit messages
  ([#55](https://github.com/alexfayers/pytest-lf-skip/pull/55),
  [`f7ae45f`](https://github.com/alexfayers/pytest-lf-skip/commit/f7ae45f85143412e759fb64377cae16dec5511e4))

---------

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

- Add initial commitlint configuration to ignore specific commit messages
  ([#55](https://github.com/alexfayers/pytest-lf-skip/pull/55),
  [`f7ae45f`](https://github.com/alexfayers/pytest-lf-skip/commit/f7ae45f85143412e759fb64377cae16dec5511e4))

- Configure Renovate ([#43](https://github.com/alexfayers/pytest-lf-skip/pull/43),
  [`bab51fd`](https://github.com/alexfayers/pytest-lf-skip/commit/bab51fd4eab615b145531a98b6950a82819a8273))

- Correct formatting of auto-approve review message in CI workflow
  ([#78](https://github.com/alexfayers/pytest-lf-skip/pull/78),
  [`0183a80`](https://github.com/alexfayers/pytest-lf-skip/commit/0183a8014b34fd895fb92fd6f8abe67a25248f4b))

- Remove requirements.txt ([#65](https://github.com/alexfayers/pytest-lf-skip/pull/65),
  [`49a1cbe`](https://github.com/alexfayers/pytest-lf-skip/commit/49a1cbe6bf1b9a4f67c8ccc5d83333714b7443ec))

- **config**: Adjust ruff linting config to allow prints in scripts
  ([#40](https://github.com/alexfayers/pytest-lf-skip/pull/40),
  [`852294b`](https://github.com/alexfayers/pytest-lf-skip/commit/852294b7f2e900f715404dfc5b35a74ca06b20e2))

- **deps**: Add renovate.json ([#43](https://github.com/alexfayers/pytest-lf-skip/pull/43),
  [`bab51fd`](https://github.com/alexfayers/pytest-lf-skip/commit/bab51fd4eab615b145531a98b6950a82819a8273))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Lock file maintenance ([#59](https://github.com/alexfayers/pytest-lf-skip/pull/59),
  [`cb1bd3d`](https://github.com/alexfayers/pytest-lf-skip/commit/cb1bd3d6b84cffa22c4446994272b04260b86781))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Lock file maintenance ([#73](https://github.com/alexfayers/pytest-lf-skip/pull/73),
  [`92c3ac7`](https://github.com/alexfayers/pytest-lf-skip/commit/92c3ac704078f6d7ac3dc8230962e99c2d4bbd87))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update astral-sh/setup-uv action to v6
  ([#56](https://github.com/alexfayers/pytest-lf-skip/pull/56),
  [`c392b2f`](https://github.com/alexfayers/pytest-lf-skip/commit/c392b2f4f3c12e370aa3c949622f4bd59ef7e904))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update pre-commit hook astral-sh/uv-pre-commit to v0.7.2
  ([#51](https://github.com/alexfayers/pytest-lf-skip/pull/51),
  [`7c47ed0`](https://github.com/alexfayers/pytest-lf-skip/commit/7c47ed093c8386f37cf04eb78355feb2bade84fe))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update pre-commit hook astral-sh/uv-pre-commit to v0.7.3
  ([#64](https://github.com/alexfayers/pytest-lf-skip/pull/64),
  [`bf29c59`](https://github.com/alexfayers/pytest-lf-skip/commit/bf29c59403471d8309844e35766f3e2edda412f7))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update pre-commit hook astral-sh/uv-pre-commit to v0.7.4
  ([#74](https://github.com/alexfayers/pytest-lf-skip/pull/74),
  [`5eab38f`](https://github.com/alexfayers/pytest-lf-skip/commit/5eab38ffc2a36a9a4a83cd253d6fde6310f5d107))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update pre-commit hook astral-sh/uv-pre-commit to v0.7.5
  ([#75](https://github.com/alexfayers/pytest-lf-skip/pull/75),
  [`f8abd6b`](https://github.com/alexfayers/pytest-lf-skip/commit/f8abd6ba58c65a47e3ccc4c51c4e237f341f1120))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update pre-commit hook compilerla/conventional-pre-commit to v4.2.0
  ([#52](https://github.com/alexfayers/pytest-lf-skip/pull/52),
  [`8bd492c`](https://github.com/alexfayers/pytest-lf-skip/commit/8bd492c8ce9e625a80e1e136f37cad7fee9521eb))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update python docker tag to v3.13
  ([#53](https://github.com/alexfayers/pytest-lf-skip/pull/53),
  [`6122187`](https://github.com/alexfayers/pytest-lf-skip/commit/61221879e1c2c3ce5b42b699b686f059d65d6069))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

### Continuous Integration

- Add commitlint job to validate commit messages
  ([#41](https://github.com/alexfayers/pytest-lf-skip/pull/41),
  [`08fa671`](https://github.com/alexfayers/pytest-lf-skip/commit/08fa67184a82ea39f8ad4a4e86e841f8b536b420))

- Add coverage job to `check` action dependencies
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Add GitHub Actions updates to Dependabot configuration
  ([#42](https://github.com/alexfayers/pytest-lf-skip/pull/42),
  [`66ebcf7`](https://github.com/alexfayers/pytest-lf-skip/commit/66ebcf70348f52a01e61a0b99fca31f75effec7a))

- Auto-approve PRs by the repository owner
  ([`8b0a86a`](https://github.com/alexfayers/pytest-lf-skip/commit/8b0a86a75389ada03a56ff715118645d80767191))

- Configure bot user for auto-approval of pull requests (implements #66)
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Implement setup-bot action for GitHub App token generation and configuration
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Inherit secrets for _validate.yml ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Reduce ci time by not waiting for linting + typechecking before build
  ([#69](https://github.com/alexfayers/pytest-lf-skip/pull/69),
  [`4e19994`](https://github.com/alexfayers/pytest-lf-skip/commit/4e19994d9b76d04393fb05ef9032277e0026f7ca))

- Remove redundant test-all-oses job from workflow
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Reorder coverage artifact storage in workflow
  ([#69](https://github.com/alexfayers/pytest-lf-skip/pull/69),
  [`4e19994`](https://github.com/alexfayers/pytest-lf-skip/commit/4e19994d9b76d04393fb05ef9032277e0026f7ca))

- Simplify coverage jobs ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Use CI bot for most public CI things ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Use ci bot user for coverage-related github actions
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

- Use correct variables in release git config setup
  ([#70](https://github.com/alexfayers/pytest-lf-skip/pull/70),
  [`df5ceb9`](https://github.com/alexfayers/pytest-lf-skip/commit/df5ceb99000bdb33d5a02b5cdeae868ee68db202))

- **pre-commit**: Configure pre-commit.ci
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))

### Documentation

- **readme**: Update badges for coverage and commits since release
  ([#39](https://github.com/alexfayers/pytest-lf-skip/pull/39),
  [`295a1d9`](https://github.com/alexfayers/pytest-lf-skip/commit/295a1d97a8d053ef75ad1bbf2c06042f3fd03b4e))

### Refactoring

- Update artifact naming and release process in CI/CD workflows
  ([#77](https://github.com/alexfayers/pytest-lf-skip/pull/77),
  [`2b4fbf9`](https://github.com/alexfayers/pytest-lf-skip/commit/2b4fbf9c579ab86d4aea4da0074926d3e0f08db2))

- **just**: Move dist-path arg for test-cov-build-artifact recipe into the recipe itself
  ([#68](https://github.com/alexfayers/pytest-lf-skip/pull/68),
  [`ed4e6f5`](https://github.com/alexfayers/pytest-lf-skip/commit/ed4e6f54b8c2ac51d82cdfde4e4207f7a88b9be8))


## v0.3.0 (2025-05-06)

### Build System

- **just**: Add release-local recipe ([#37](https://github.com/alexfayers/pytest-lf-skip/pull/37),
  [`020ee22`](https://github.com/alexfayers/pytest-lf-skip/commit/020ee2284a1c55b55af4a26e83f85a8795d1c72f))

- **just**: Add test-cov-build-artifact recipe for use in CI
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

### Chores

- :pushpin: Update uv.lock ([#13](https://github.com/alexfayers/pytest-lf-skip/pull/13),
  [`80e5982`](https://github.com/alexfayers/pytest-lf-skip/commit/80e59823f4502c92a879454a75921ecd901b25b6))

- Add dependabot.yml ([#24](https://github.com/alexfayers/pytest-lf-skip/pull/24),
  [`30989ce`](https://github.com/alexfayers/pytest-lf-skip/commit/30989cefc30a4213dbfa1600240f8b02d3a60944))

- Add mypy overrides for silent import handling in scripts
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Create cicd.yml workflow to prevent PRs from trying to release
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Drop python version in .python-version
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Move UV_FROZEN environment variable to _validate.yml
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Remove pytest -rP flag from addopts ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Update dependabot.yml to use uv ([#31](https://github.com/alexfayers/pytest-lf-skip/pull/31),
  [`37ba215`](https://github.com/alexfayers/pytest-lf-skip/commit/37ba2150df5602f3b8a8163e767bd0acbc75dda4))

- **just**: Add publish to release steps
  ([#20](https://github.com/alexfayers/pytest-lf-skip/pull/20),
  [`69d2987`](https://github.com/alexfayers/pytest-lf-skip/commit/69d298779bd17ef5ab5aa43a8bf4d101166863ad))

- **just**: Uninstall pre-commit hooks before installing them
  ([#14](https://github.com/alexfayers/pytest-lf-skip/pull/14),
  [`84b1ff9`](https://github.com/alexfayers/pytest-lf-skip/commit/84b1ff9b4732568b0dc7ba5b0217407223b8c604))

- **scripts**: Add get-supported-py-versions script for use in CI
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

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

- Add more test runners ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Add pull-requests write permission to the validate job
  ([#33](https://github.com/alexfayers/pytest-lf-skip/pull/33),
  [`013c0be`](https://github.com/alexfayers/pytest-lf-skip/commit/013c0be58a669fadc407640c747f77c50c5d5c58))

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

- Install just and uv before running release build
  ([#36](https://github.com/alexfayers/pytest-lf-skip/pull/36),
  [`e7903dd`](https://github.com/alexfayers/pytest-lf-skip/commit/e7903ddcd4ded8c946ce4c288f876461300e4ddf))

- Move main validation steps into _validate.yml and refactor ci.yml and release.yml due to that
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

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

- Tidy setup/action.yml ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Update environments for finer grain release control
  ([#22](https://github.com/alexfayers/pytest-lf-skip/pull/22),
  [`d5509c1`](https://github.com/alexfayers/pytest-lf-skip/commit/d5509c127560f96d156236258ab230b276c158cb))

- Update job names for consistency and clarity in Python version calculations
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Update setup action to ensure virtual environment exists
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Use `uv publish` for release ([#18](https://github.com/alexfayers/pytest-lf-skip/pull/18),
  [`91db5b7`](https://github.com/alexfayers/pytest-lf-skip/commit/91db5b7381c189c77e81188a1898fe4abe591d40))

- Use alexfayers-py-publisher for releasing
  ([#20](https://github.com/alexfayers/pytest-lf-skip/pull/20),
  [`69d2987`](https://github.com/alexfayers/pytest-lf-skip/commit/69d298779bd17ef5ab5aa43a8bf4d101166863ad))

- Use bot token on cicd release checkout
  ([#38](https://github.com/alexfayers/pytest-lf-skip/pull/38),
  [`fbb79e4`](https://github.com/alexfayers/pytest-lf-skip/commit/fbb79e46f70ae601cae8ecb7f55f56b27626e3ea))

- Use just/uv for build step in validate workflow
  ([#37](https://github.com/alexfayers/pytest-lf-skip/pull/37),
  [`020ee22`](https://github.com/alexfayers/pytest-lf-skip/commit/020ee2284a1c55b55af4a26e83f85a8795d1c72f))

- Use just/uv for building in release ([#37](https://github.com/alexfayers/pytest-lf-skip/pull/37),
  [`020ee22`](https://github.com/alexfayers/pytest-lf-skip/commit/020ee2284a1c55b55af4a26e83f85a8795d1c72f))

- Use just/uv for building release ([#37](https://github.com/alexfayers/pytest-lf-skip/pull/37),
  [`020ee22`](https://github.com/alexfayers/pytest-lf-skip/commit/020ee2284a1c55b55af4a26e83f85a8795d1c72f))

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

- Add unit tests for version calculation functions in get_supported_py_versions
  ([#23](https://github.com/alexfayers/pytest-lf-skip/pull/23),
  [`ca11500`](https://github.com/alexfayers/pytest-lf-skip/commit/ca115005397ee57deb29146fa7bcf75dc15d77c3))

- Adjust test_package_version to include more versions
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))

- Enhance version assertion message in test_package_version for clarity on failure
  ([#19](https://github.com/alexfayers/pytest-lf-skip/pull/19),
  [`5737b70`](https://github.com/alexfayers/pytest-lf-skip/commit/5737b70bb2a6381c32d0f4c6d3b7c07ff930081e))

- **cov**: Add path mappings to prevent ci errors during `coverage combine`
  ([#35](https://github.com/alexfayers/pytest-lf-skip/pull/35),
  [`c085ad5`](https://github.com/alexfayers/pytest-lf-skip/commit/c085ad5b3337b811156a64a40f3d1701969a12dc))


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
