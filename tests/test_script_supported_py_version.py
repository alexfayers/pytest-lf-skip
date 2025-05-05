from __future__ import annotations

from importlib.util import find_spec

import pytest

if not find_spec("scripts.get_supported_py_versions"):
    pytest.skip("get_supported_py_versions script does not exist.", allow_module_level=True)

try:
    from scripts import get_supported_py_versions as _get_supported_py_versions  # noqa: F401
except ImportError as e:
    pytest.skip(f"couldn't import get_supported_py_versions script ({e}).", allow_module_level=True)

from packaging.version import (
    Version,
    parse,
)

from scripts.get_supported_py_versions import (
    MetaVersionInfo,
    calculate_min_max_versions,
    next_version,
    parse_specs,
    previous_version,
)


@pytest.fixture(autouse=True)
def mocked_version_info() -> MetaVersionInfo:
    info = MetaVersionInfo()
    info._latest_2_version = parse("2.7.18")  # noqa: SLF001
    info._latest_3_version = parse("3.13.3")  # noqa: SLF001
    info._latest_eol_version = parse("3.8.20")  # noqa: SLF001
    info._oldest_supported_version = parse("3.9")  # noqa: SLF001
    info._subversion_min_maxes = {  # noqa: SLF001
        (2, 7): (parse("2.7"), parse("2.7.18")),
        (3, 0): (parse("3.0"), parse("3.0.1")),
        (3, 1): (parse("3.1"), parse("3.1.5")),
        (3, 2): (parse("3.2"), parse("3.2.6")),
        (3, 3): (parse("3.3"), parse("3.3.7")),
        (3, 4): (parse("3.4"), parse("3.4.10")),
        (3, 5): (parse("3.5"), parse("3.5.10")),
        (3, 6): (parse("3.6"), parse("3.6.15")),
        (3, 7): (parse("3.7"), parse("3.7.17")),
        (3, 8): (parse("3.8"), parse("3.8.20")),
        (3, 9): (parse("3.9"), parse("3.9.22")),
        (3, 10): (parse("3.10"), parse("3.10.17")),
        (3, 11): (parse("3.11"), parse("3.11.12")),
        (3, 12): (parse("3.12"), parse("3.12.10")),
        (3, 13): (parse("3.13"), parse("3.13.3")),
    }
    return info


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("2.7.18", "3.0"),
        ("3.10", "3.10.1"),
        ("3.10.16", "3.10.17"),
        ("3.10.17", "3.11"),
        ("3.13.3", "3.13.4"),
    ],
)
def test_next_version(version: str, expected: str, mocked_version_info: MetaVersionInfo) -> None:
    """Test the next_version function."""
    assert next_version(parse(version), mocked_version_info) == parse(expected)


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("2.7.18", "2.7.17"),
        ("3.10", "3.9.22"),
        ("3.10.16", "3.10.15"),
        ("3.10.17", "3.10.16"),
        ("3.13.3", "3.13.2"),
    ],
)
def test_previous_version(version: str, expected: str, mocked_version_info: MetaVersionInfo) -> None:
    """Test the previous_version function."""
    assert previous_version(parse(version), mocked_version_info) == parse(expected)


@pytest.mark.parametrize(
    ("spec", "expected"),
    [
        (">=3.9, <4.0.0", (parse("3.9"), parse("3.13.3"))),
        (">=3.8, <3.9", (parse("3.8"), parse("3.8.20"))),
        (">=2.7, <3", (parse("2.7"), parse("2.7.18"))),
        (">=3.10, <=3.11", (parse("3.10"), parse("3.11"))),
    ],
)
def test_calculate_min_max_versions(
    spec: str, expected: tuple[Version, Version], mocked_version_info: MetaVersionInfo
) -> None:
    """Test the parse_specs function."""
    min_version, max_version = calculate_min_max_versions(parse_specs(spec), mocked_version_info)
    assert min_version == expected[0]
    assert max_version == expected[1]
