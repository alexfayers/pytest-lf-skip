from __future__ import annotations


class Constants:
    lf_plugin_name = "lfplugin"
    lf_collwrapper_plugin_name = "lfplugin-collwrapper"

    lf_skip_plugin_name = "lfskipplugin"
    lf_skip_parser_options = (
        "--last-failed-skip",
        "--lf-skip",
    )

    lf_skip_vscode_options = (
        "--auto-last-failed-skip-vscode",
        "--auto-lf-skip-vscode",
    )


class Config:
    skip_reason = "previously passed"
