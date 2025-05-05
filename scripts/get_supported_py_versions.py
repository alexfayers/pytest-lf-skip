# ruff: noqa: T201, PLR2004
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "packaging",
#     "requests",
#     "tomli",
# ]
#
# [dependency-groups]
# typechecking = [
#     "types-requests",
# ]
# ///
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from typing import TYPE_CHECKING, ClassVar, NoReturn, TypeVar

from packaging.specifiers import InvalidSpecifier, Specifier, SpecifierSet
from packaging.version import (
    parse,
)
import requests
import tomli

if TYPE_CHECKING:
    from packaging.version import Version

    VERSION_TUPLE_TYPE = TypeVar("VERSION_TUPLE_TYPE", bound=tuple[int, ...])


def error(message: str) -> NoReturn:
    """Print an error message to stderr and exit."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


class MetaVersionInfo:
    EOL_PYTHON_VERSIONS_URL: ClassVar[str] = "https://endoflife.date/api/python.json"

    _latest_2_version: Version | None = None
    _latest_3_version: Version | None = None

    _latest_eol_version: Version | None = None
    _oldest_supported_version: Version | None = None

    _subversion_min_maxes: dict[tuple[int, int], tuple[Version, Version]] | None = None

    @property
    def latest_2_version(self) -> Version:
        """The latest Python 2 version."""
        if self._latest_2_version is None:
            self._fetch_data()

        if self._latest_2_version is None:
            error("Failed to get the latest Python 2 version.")

        return self._latest_2_version

    @property
    def latest_3_version(self) -> Version:
        """The latest Python 3 version."""
        if self._latest_3_version is None:
            self._fetch_data()

        if self._latest_3_version is None:
            error("Failed to get the latest Python 3 version.")

        return self._latest_3_version

    @property
    def latest_eol_version(self) -> Version:
        """The latest EOL Python version."""
        if self._latest_eol_version is None:
            self._fetch_data()

        if self._latest_eol_version is None:
            error("Failed to get the latest EOL Python version.")

        return self._latest_eol_version

    @property
    def oldest_supported_version(self) -> Version:
        """The oldest supported Python version."""
        if self._oldest_supported_version is None:
            self._fetch_data()

        if self._oldest_supported_version is None:
            error("Failed to get the oldest supported Python version.")

        return self._oldest_supported_version

    @property
    def subversion_min_maxes(self) -> dict[tuple[int, int], tuple[Version, Version]]:
        """Get the latest and earliest releases for each subversion."""
        if self._subversion_min_maxes is None:
            self._fetch_data()

        if self._subversion_min_maxes is None:
            error("Failed to get the subversion min maxes.")

        return self._subversion_min_maxes

    def _fetch_data(self) -> None:
        current_time = datetime.now(timezone.utc)

        response = requests.get(self.EOL_PYTHON_VERSIONS_URL, timeout=5)
        response.raise_for_status()

        data: list[dict[str, str]] = response.json()

        self._subversion_min_maxes = {}

        for item in data:
            version = parse(item["latest"])

            self._subversion_min_maxes[(version.major, version.minor)] = (
                parse(f"{version.major}.{version.minor}"),
                version,
            )

            if version.major == 2:
                self._latest_2_version = (
                    version if self._latest_2_version is None else max(self._latest_2_version, version)
                )
            else:
                self._latest_3_version = (
                    version if self._latest_3_version is None else max(self._latest_3_version, version)
                )

            eol_dt = datetime.fromisoformat(item["eol"]).replace(tzinfo=timezone.utc)
            if eol_dt <= current_time:
                self._latest_eol_version = (
                    version if self._latest_eol_version is None else max(self._latest_eol_version, version)
                )
            else:
                self._oldest_supported_version = (
                    version if self._oldest_supported_version is None else min(self._oldest_supported_version, version)
                )

        if self._oldest_supported_version is not None:
            self._oldest_supported_version = parse(
                f"{self._oldest_supported_version.major}.{self._oldest_supported_version.minor}"
            )


def next_version(version: Version, meta_version_info: MetaVersionInfo) -> Version:
    """Get the next version in the sequence."""
    this_version_release_bounds = meta_version_info.subversion_min_maxes.get((version.major, version.minor), None)
    if this_version_release_bounds is None:
        error(f"Version {version} doesn't exist.")

    min_version, max_version = this_version_release_bounds

    if (next_value := parse(f"{version.major}.{version.minor}.{version.micro + 1}")) > max_version:
        get_next_version = False
        for (subversion_major, subversion_minor), (
            min_version,
            _,
        ) in meta_version_info.subversion_min_maxes.items():
            if get_next_version:
                return min_version
            if version.major == subversion_major and version.minor == subversion_minor:
                get_next_version = True
                continue

    # can't find the actual next version, so just use the guessed next version
    return next_value


def previous_version(version: Version, meta_version_info: MetaVersionInfo) -> Version:
    """Get the previous version in the sequence."""
    this_version_release_bounds = meta_version_info.subversion_min_maxes.get((version.major, version.minor), None)
    if this_version_release_bounds is None:
        if version.major == 4 and version.minor == 0:
            return meta_version_info.latest_3_version
        error(f"Version {version} is not supported for calculation yet.")
    min_version, max_version = this_version_release_bounds

    if version.micro == 0:
        get_previous_version = False
        for (subversion_major, subversion_minor), (
            _,
            max_version,
        ) in reversed(meta_version_info.subversion_min_maxes.items()):
            if get_previous_version:
                return max_version
            if version.major == subversion_major and version.minor == subversion_minor:
                get_previous_version = True
                continue

    return parse(f"{version.major}.{version.minor}.{version.micro - 1}")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Get the minimum and maximum supported Python versions from a given pyproject.toml"
    )
    parser.add_argument(
        "pyproject",
        type=Path,
        help="Path to the pyproject.toml file",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["json", "gh-action"],
        default="json",
        help=(
            "The way that the output should be formatted "
            "(gh-action appends to the file in the GITHUB_OUTPUT environment variable)"
        ),
    )

    return parser.parse_args()


def get_requires_python(pyproject_path: Path, meta_version_info: MetaVersionInfo) -> str:
    """Get the requires-python field from the pyproject.toml file."""
    if not pyproject_path.is_file():
        error("The specified path is not a file.")

    with pyproject_path.open("rb") as f:
        data: dict[str, dict[str, str]] = tomli.load(f)
        return data.get("project", {}).get(
            "requires-python",
            f">={next_version(meta_version_info.latest_eol_version, meta_version_info)}",
        )


def parse_specs(specs: str) -> SpecifierSet:
    """Parse the specs string into a SpecifierSet."""
    try:
        return SpecifierSet(specs)
    except InvalidSpecifier as e:
        error(str(e))
        sys.exit(1)


def handle_eq_operator(
    min_version: Version | None, max_version: Version | None, parsed: Version
) -> tuple[Version | None, Version | None]:
    """Handle the == and === operators."""
    return (
        parsed if min_version is None else min(min_version, parsed),
        parsed if max_version is None else max(max_version, parsed),
    )


def handle_gte_operator(min_version: Version | None, parsed: Version) -> Version | None:
    """Handle the >= operator."""
    return parsed if min_version is None else min(min_version, parsed)


def handle_lte_operator(max_version: Version | None, parsed: Version) -> Version | None:
    """Handle the <= operator."""
    return parsed if max_version is None else max(max_version, parsed)


def handle_gt_operator(
    min_version: Version | None, parsed: Version, meta_version_info: MetaVersionInfo
) -> Version | None:
    """Handle the > operator."""
    parsed = next_version(parsed, meta_version_info)
    return parsed if min_version is None else min(min_version, parsed)


def handle_lt_operator(
    max_version: Version | None, parsed: Version, meta_version_info: MetaVersionInfo
) -> Version | None:
    """Handle the < operator."""
    parsed = previous_version(parsed, meta_version_info)
    return parsed if max_version is None else max(max_version, parsed)


def handle_compatible_release_operator(
    min_version: Version | None, max_version: Version | None, parsed: Version, meta_version_info: MetaVersionInfo
) -> tuple[Version | None, Version | None]:
    """Handle the compatible release operator."""
    if len(parsed.release) >= 3:
        min_version = parsed if min_version is None else min(min_version, parsed)
        max_version = (
            next_version(parsed, meta_version_info)
            if max_version is None
            else max(max_version, next_version(parsed, meta_version_info))
        )
    elif len(parsed.release) >= 2:
        min_version = parsed if min_version is None else min(min_version, parsed)
        max_version = (
            parse(f"{parsed.major}.{parsed.minor + 1}")
            if max_version is None
            else max(max_version, parse(f"{parsed.major}.{parsed.minor + 1}"))
        )
    elif len(parsed.release) >= 1:
        min_version = parsed if min_version is None else min(min_version, parsed)
        max_version = (
            parse(f"{parsed.major + 1}") if max_version is None else max(max_version, parse(f"{parsed.major + 1}"))
        )

    return min_version, max_version


def handle_specifier(
    min_version: Version | None, max_version: Version | None, specifier: Specifier, meta_version_info: MetaVersionInfo
) -> tuple[Version | None, Version | None]:
    """Handle a single specifier."""
    version = parse(specifier.version)

    if specifier.operator == ">=":
        min_version = handle_gte_operator(min_version, version)
    elif specifier.operator == "<=":
        max_version = handle_lte_operator(max_version, version)
    elif specifier.operator == ">":
        min_version = handle_gt_operator(min_version, version, meta_version_info)
    elif specifier.operator == "<":
        max_version = handle_lt_operator(max_version, version, meta_version_info)
    elif specifier.operator in {"==", "==="}:
        min_version, max_version = handle_eq_operator(min_version, max_version, version)
    elif specifier.operator == "~=":
        min_version, max_version = handle_compatible_release_operator(
            min_version, max_version, version, meta_version_info
        )

    return min_version, max_version


def calculate_min_max_versions(specifiers: SpecifierSet, meta_version_info: MetaVersionInfo) -> tuple[Version, Version]:
    """Calculate the minimum and maximum supported Python versions."""
    max_version: Version | None = None
    min_version: Version | None = None

    for specifier in specifiers:
        min_version, max_version = handle_specifier(min_version, max_version, specifier, meta_version_info)

    if min_version is None:
        min_version = meta_version_info.oldest_supported_version
    if max_version is None:
        max_version = meta_version_info.latest_3_version

    if min_version > max_version:
        error("The minimum version is greater than the maximum version.")

    return min_version, max_version


def main(args: argparse.Namespace) -> None:
    """Main body of the script."""
    meta_version_info = MetaVersionInfo()

    raw_spec = get_requires_python(args.pyproject, meta_version_info)

    specs = parse_specs(raw_spec)

    min_version, max_version = calculate_min_max_versions(specs, meta_version_info)

    min_version_str, max_version_str = str(min_version), str(max_version)

    if args.mode == "gh-action":
        # GitHub Actions requires the output to be in a specific format
        if not (gh_output_file := os.environ.get("GITHUB_OUTPUT")):
            error("GITHUB_OUTPUT environment variable is not set.")

        gh_output_path = Path(gh_output_file)

        with gh_output_path.open("a") as f:
            f.write(f"min-version={min_version_str}\n")
            f.write(f"max-version={max_version_str}\n")
    else:
        print(
            json.dumps(
                {
                    "min-version": min_version_str,
                    "max-version": max_version_str,
                }
            )
        )


if __name__ == "__main__":
    main(parse_args())
