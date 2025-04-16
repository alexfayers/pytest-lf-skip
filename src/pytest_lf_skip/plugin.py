from __future__ import annotations

from _pytest.cacheprovider import LFPlugin
import pytest

from pytest_lf_skip.constants import Constants
from pytest_lf_skip.lf_skip import LFSkipPlugin

from .hooks import argparse_parse_hook


def pytest_addoption(
    parser: pytest.Parser,
    pluginmanager: pytest.PytestPluginManager,  # noqa: ARG001
) -> None:
    """Add the lf-skip args to pytest."""
    parser.parse = argparse_parse_hook(parser.parse)  # type: ignore[method-assign, assignment]

    parser.addoption(
        *Constants.lf_skip_parser_options,
        action="store_true",
        default=False,
        help=(
            "If --last-failed is enabled, skip tests that have been passed in the last run instead of deselecting them"
        ),
    )

    parser.addoption(
        *Constants.lf_skip_vscode_options,
        action="store_true",
        default=False,
        help="Automatically enable --lf and --lf-skip when pytest is called from vscode.",
    )


@pytest.hookimpl
def pytest_plugin_registered(
    plugin: object,
    manager: pytest.PytestPluginManager,
) -> None:
    """Register the LFSkipPlugin if the LFPlugin is registered."""
    if isinstance(plugin, LFPlugin) and not isinstance(plugin, LFSkipPlugin):
        # add the override hook
        manager.register(LFSkipPlugin(plugin.config), Constants.lf_skip_plugin_name)
