"""
    Pytest fixture for loading the plugin to test
"""
from typing import TYPE_CHECKING, Set
import pytest


if TYPE_CHECKING:
    from nonebot.plugin import Plugin


@pytest.fixture
def load_waifulabs(nonebug_init: None) -> Set["Plugin"]:
    import nonebot  # 这里的导入必须在函数内
    # 加载插件
    # return nonebot.load_plugins("../")
    return nonebot.load_plugins("../plugins")

