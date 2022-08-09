"""
    The zhenxun bot plugin for generating waifu images via querying waifulabs.com.
"""
from asyncio import sleep

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GROUP

#  === Zhenxun bot plugin standard specification ===
__zx_plugin_name__ = "老婆生成器"
# TODO: complete usage docs
__plugin_usage__ = """

"""
__plugin_des__ = "用AI生成独一无二超可爱的二次元老婆图片"
# TODO: complete plugin cmd list
__plugin_cmd__ = [
    "生成老婆/老婆",
    "随机老婆",
]
__plugin_type__ = ("来点好康的", 1)  # Use vertical cmd list cuz we have a lot of cmds
__plugin_version__ = 0.10
__plugin_author__ = "养猫的小天使喵"
__plugin_cd_limit__ = {
    "cd": 30,
    "rst": "刚刚才获得一只老婆，这么快就要变心了吗！",
}
__plugin_block_limit__ = {
    "rst": "其他群友正在生成老婆哦~请等Ta先完成吧~"
}
__plugin_count_limit__ = {
    "status": False,    # No daily usage limit
}
# TODO: complete (or discard) plugin resource specification
__plugin_resource__ = {}
# TODO: complete plugin user configs specification
__plugin_configs__ = {

}

# Matchers
generate_waifu_matcher = on_command("生成老婆", aliases={"老婆"}, rule=to_me(), permission=GROUP, priority=5, block=True)
generate_random_waifu_matcher = on_command("随机老婆", permission=GROUP, rule=to_me(), priority=5, block=True)


# Event responses
@generate_waifu_matcher.handle()
async def generate_waifu():
    await generate_waifu_matcher.send("正在生成老婆...")
    await sleep(3)
    await generate_waifu_matcher.finish("生成老婆成功！（测试）")
