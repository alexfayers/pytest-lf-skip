from __future__ import annotations

from tests._types import ExpectedResult, FileReplace, LineSearch, Outcome

RERUN_PREVIOUS_MESSAGE = "run-last-failure: rerun previous 1 failure"
NO_PREVIOUSLY_FAILED_MESSAGE = "run-last-failure: no previously failed tests, not deselecting items."
FIRST_EXPECTED_RESULT = ExpectedResult(
    Outcome(passed=1, failed=1),
    line_searches=(
        LineSearch(
            search=NO_PREVIOUSLY_FAILED_MESSAGE,
        ),
    ),
)
LAST_EXPECTED_RESULT = ExpectedResult(
    Outcome(passed=2),
    line_searches=(
        LineSearch(
            search=NO_PREVIOUSLY_FAILED_MESSAGE,
        ),
    ),
)
ASSERT_FALSE_TRUE_REPLACE = FileReplace(
    old="assert False",
    new="assert True",
)
