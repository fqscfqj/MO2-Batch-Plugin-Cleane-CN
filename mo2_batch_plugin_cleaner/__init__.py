# Created by GoriRed
# Version: 1.0
# License: CC-BY-NC
# https://github.com/tkoopman/

import mobase  # type: ignore

from mo2_batch_plugin_cleaner import plugin


def createPlugin() -> mobase.IPluginTool:
    return plugin.CleanerPlugin()