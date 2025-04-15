from __future__ import annotations

from dataclasses import asdict
import logging
from typing import TYPE_CHECKING

import pytest

from ._helper import replace_file_text

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from pathlib import Path

    from ._types import ExpectedResult

pytest_plugins = "pytester"

logger = logging.getLogger(__name__)


@pytest.fixture
def example_test_file(pytester: pytest.Pytester) -> Path:
    return pytester.makepyfile(
        """
        def test_will_pass():
            assert True

        def test_will_fail():
            assert False
    """,
    )


@pytest.fixture
def factory_test_plugin(
    pytester: pytest.Pytester,
    example_test_file: Path,
) -> Callable[..., None]:
    """Ensure that lf-skip works."""

    def _test_plugin(
        run_args: Iterable[str],
        expected_results: Iterable[ExpectedResult],
    ) -> None:
        runtime_args: Iterable[str | Path] = (*run_args, example_test_file)

        for index, expected_result in enumerate(expected_results):
            if expected_result.test_file_replace:
                logger.info(
                    "Replacing '%s' with '%s' in test file...",
                    expected_result.test_file_replace.old,
                    expected_result.test_file_replace.new,
                )
                replace_file_text(
                    example_test_file,
                    expected_result.test_file_replace.old,
                    expected_result.test_file_replace.new,
                )

            if expected_result.prepend_args:
                runtime_args = (*expected_result.prepend_args, *runtime_args)

            res = pytester.runpytest(*runtime_args)

            try:
                res.assert_outcomes(**asdict(expected_result.outcome))
            except AssertionError as e:
                msg = f"[{index}] Outcomes didn't match"
                raise AssertionError(msg) from e

            if expected_result.line_searches:
                for line_search in expected_result.line_searches:
                    match_count = 0
                    for line in res.outlines:
                        if line_search.search in line:
                            match_count += 1
                    assert match_count, f"[{index}] '{line_search.search}' didn't appear {line_search.count} times"

    return _test_plugin
