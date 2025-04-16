from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Concatenate, ParamSpec, TypeVar, cast
import warnings

from .constants import Constants

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from os import PathLike

P = ParamSpec("P")
R = TypeVar("R")


def argparse_parse_hook(
    func: Callable[Concatenate[Sequence[str | PathLike[str]], P], R],
) -> Callable[Concatenate[Sequence[str | PathLike[str]], P], R]:
    """Add the `--lf` and `--lf-skip` options into the run if pytest has been called by vscode.

    Also warn if the `--lf-skip` options are used without `--lf` being enabled.
    """

    @functools.wraps(func)
    def wrapper(
        args_: list[str | PathLike[str]],
        /,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> R:
        for search_arg in Constants.lf_skip_vscode_options:
            if search_arg in args_:
                if "vscode_pytest" in args_:
                    # vscode_pytest plugin has been passed in, so add our args
                    args_.insert(0, "--lf")
                    args_.insert(0, "--lf-skip")
                else:
                    warnings.warn(
                        f"`{search_arg}` only works when running from vscode.",
                        stacklevel=1,
                    )

        for search_arg in Constants.lf_skip_parser_options:
            if search_arg in args_ and all(arg not in ("--lf", "--last-failed") for arg in args_):
                warnings.warn(
                    f"`{search_arg}` only works when running with `--lf`.",
                    stacklevel=1,
                )
                break

        return func(args_, *args, **kwargs)

    return cast("Callable[Concatenate[Sequence[str | PathLike[str]], P], R]", wrapper)
