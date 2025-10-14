from __future__ import annotations

from io import StringIO
import logging
from typing import TYPE_CHECKING

import pytest

from pytest_lf_skip import __version__
from pytest_lf_skip.hooks import logger
from tests._constants import (
    ASSERT_FALSE_TRUE_REPLACE,
    NO_PREVIOUSLY_FAILED_MESSAGE,
    RERUN_PREVIOUS_MESSAGE,
)
from tests._types import ExpectedResult, LineSearch, Outcome

if TYPE_CHECKING:
    from collections.abc import Callable


@pytest.mark.parametrize(
    ("run_args", "expected_results"),
    [
        (
            ["--lf"],
            [
                ExpectedResult(
                    Outcome(passed=1, failed=1),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(failed=1, deselected=1),
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(passed=1, deselected=1),
                    test_file_replace=ASSERT_FALSE_TRUE_REPLACE,
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(passed=2),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
            ],
        ),
        (
            ["--lf", "--lf-skip"],
            [
                ExpectedResult(
                    Outcome(passed=1, failed=1),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(
                        skipped=1,
                        failed=1,
                    ),
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(
                        passed=1,
                        skipped=1,
                    ),
                    test_file_replace=ASSERT_FALSE_TRUE_REPLACE,
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(passed=2),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
            ],
        ),
    ],
    ids=("lf", "lf+skip"),
)
def test_lf(
    factory_test_plugin: Callable[..., None],
    run_args: list[str],
    expected_results: list[ExpectedResult],
) -> None:
    factory_test_plugin(
        run_args,
        expected_results,
    )


@pytest.mark.parametrize(
    ("run_args", "expected_results"),
    [
        (
            ["--lf"],
            [
                ExpectedResult(
                    Outcome(passed=1, failed=1),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(failed=1, deselected=1),
                ),
                ExpectedResult(
                    Outcome(passed=1, deselected=1),
                    test_file_replace=ASSERT_FALSE_TRUE_REPLACE,
                    prepend_args=["--lfnf", "none"],
                ),
                ExpectedResult(
                    Outcome(deselected=2),
                    line_searches=(
                        LineSearch(
                            search="run-last-failure: no previously failed tests, deselecting all items.",
                        ),
                    ),
                ),
            ],
        ),
        (
            ["--lf", "--lf-skip"],
            [
                ExpectedResult(
                    Outcome(passed=1, failed=1),
                    line_searches=(
                        LineSearch(
                            search=NO_PREVIOUSLY_FAILED_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(
                        skipped=1,
                        failed=1,
                    ),
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                ),
                ExpectedResult(
                    Outcome(
                        passed=1,
                        skipped=1,
                    ),
                    test_file_replace=ASSERT_FALSE_TRUE_REPLACE,
                    line_searches=(
                        LineSearch(
                            search=RERUN_PREVIOUS_MESSAGE,
                        ),
                    ),
                    prepend_args=["--lfnf", "none"],
                ),
                ExpectedResult(
                    Outcome(skipped=2),
                    line_searches=(
                        LineSearch(
                            search="run-last-failure: no previously failed tests, deselecting all items.",
                        ),
                    ),
                ),
            ],
        ),
    ],
    ids=("all", "all+skip"),
)
def test_lfnf_none(
    factory_test_plugin: Callable[..., None],
    run_args: list[str],
    expected_results: list[ExpectedResult],
) -> None:
    factory_test_plugin(
        run_args,
        expected_results,
    )


def test_package_version() -> None:
    assert all(
        __version__.startswith(initial_version) is False
        for initial_version in [
            "0.0.0",
            "0.0.1",
            "0.1.0",
        ]
    ), f"Version is {__version__} which indicates that git tags have not been cloned"


def test_no_lf_warning(
    pytester: pytest.Pytester,
) -> None:
    with pytest.warns(
        UserWarning,
        match="only works when running with `--lf`.",
    ):
        pytester.runpytest("--lf-skip")


def test_no_vscode_warning(
    pytester: pytest.Pytester,
) -> None:
    with pytest.warns(
        UserWarning,
        match="only works when running from vscode",
    ):
        pytester.runpytest("--auto-lf-skip-vscode")


def test_autoenable_vscode(
    pytester: pytest.Pytester,
) -> None:
    log_stream = StringIO()
    logger.addHandler(logging.StreamHandler(log_stream))

    # NOTE: this is a bit hacky because we're not passing the args in the same way as vscode (with the -p flag)
    # but it works for the test
    pytester.runpytest("--auto-lf-skip-vscode", "vscode_pytest")

    assert "Auto-added --lf and --lf-skip to args" in log_stream.getvalue()
