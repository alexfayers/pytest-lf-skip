from __future__ import annotations

from typing import TYPE_CHECKING

from _pytest.cacheprovider import LFPlugin
import pytest

from .constants import Config, Constants

if TYPE_CHECKING:
    from collections.abc import Generator

    import _pytest.nodes


class LFSkipPlugin(LFPlugin):
    _parent: LFPlugin | None = None

    def __init__(self, config: pytest.Config) -> None:
        should_be_active = True

        if not config.getoption(Constants.lf_skip_parser_options[0]):
            should_be_active = False

        # check if lfplugin is registered, if not, do nothing
        if should_be_active and (parent := config.pluginmanager.get_plugin(name=Constants.lf_plugin_name)):
            self._parent = parent
        else:
            should_be_active = False

        # save the current state of the lf options
        lf_attr = config._opt2dest.get("lf", "lf")  # noqa: SLF001
        existing_lf_value = config.getoption("lf")

        if not existing_lf_value:
            should_be_active = False

        if should_be_active:
            # allow re-setting of lfplugin-collwrapper, because it gets added in the init function
            # the wording of the function seems backwards to me, but it works.
            # this will allow us to reregister the `lfplugin-collwrapper` to this version when we run super's init

            config.pluginmanager.set_blocked(Constants.lf_collwrapper_plugin_name)
        else:
            # toggle the lf cli arg off temporarily so the lfplugin-collwrapper doesn't get reregistered
            setattr(config.option, lf_attr, False)

        super().__init__(config)

        if should_be_active:
            # disable the lfplugin-collwrapper plugin so it doesn't filter out known passes
            config.pluginmanager.unregister(name=Constants.lf_collwrapper_plugin_name)
        else:
            # set the lf arg pack to it's previous state
            setattr(config.option, lf_attr, existing_lf_value)
            self.active = False

    # wrap the existing pytest_collection_modifyitems on the parent
    @pytest.hookimpl(wrapper=True, tryfirst=True)
    def pytest_collection_modifyitems(
        self,
        config: pytest.Config,  # noqa: ARG002
        items: list[_pytest.nodes.Item],
    ) -> Generator[None]:
        """Mark deselected tests as skipped."""
        if not self._parent or not self._parent.active:
            return (yield)

        re_add_items = []

        # Temporarily disable the pytest_deselected hook so that stats aren't
        # messed up - very hacky, but it works
        # (If we could nicely check the calling plugin from within a hook, then
        # that would be better, but for now this is the solution)
        original_deselect_hook = self._parent.config.hook.pytest_deselected

        def pytest_deselected_override(items: list[pytest.Item]) -> None:
            for item in items:
                item.add_marker(pytest.mark.skip(reason=Config.skip_reason))
                re_add_items.append(item)

        self._parent.config.hook.pytest_deselected = pytest_deselected_override  # type: ignore[attr-defined]

        # Let the parent's pytest_collection_modifyitems execute
        res = yield

        # re-enable the pytest_deselected hook
        self._parent.config.hook.pytest_deselected = original_deselect_hook  # type: ignore[attr-defined]

        # add the previously removed tests back
        items.extend(re_add_items)

        # copy attrs from parent so that output is consistent with standard --lf
        for attr_name in dir(self._parent):
            if attr_name.startswith("__"):
                continue

            if callable(attr := getattr(self._parent, attr_name)):
                continue
            setattr(self, attr_name, attr)

        # deactivate parent LFPlugin to prevent doubled messages
        self._parent.active = False

        return res
