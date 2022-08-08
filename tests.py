import os
import asyncio

from site_navigator import SiteNavigator


test_screenshot_dir = "test_screenshot"


async def default_to_end():
    # Use default waifu till the end
    navi = await SiteNavigator.create_navi()
    # stage 1
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_1_grid.png"))
    # stage 2
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_2_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_2_default.png"))
    # stage 3
    await navi.continue_default()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_3_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_3_default.png"))
    # stage 4
    await navi.continue_default()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_4_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_4_default.png"))
    # stage 5
    await navi.continue_default()
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_5_default.png"))


async def first_to_end():
    # Use first alternative waifu in the grid till end
    navi = await SiteNavigator.create_navi()
    # stage 1
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_1_grid.png"))
    # stage 2
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_2_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_2_default.png"))
    # stage 3
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_3_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_3_default.png"))
    # stage 4
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_4_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_4_default.png"))
    # stage 5
    await navi.continue_grid(0)
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_5_default.png"))


if __name__ == '__main__':
    if not os.path.exists(test_screenshot_dir):
        os.mkdir(test_screenshot_dir)

    asyncio.get_event_loop().run_until_complete(first_to_end())
