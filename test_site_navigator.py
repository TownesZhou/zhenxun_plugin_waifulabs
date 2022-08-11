import os
import asyncio
import random
import time

from site_navigator import SiteNavigator


test_screenshot_dir = "test_screenshot"


async def default_to_end(navi):
    # Use default waifu till the end
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


async def first_to_end(navi):
    # Use first alternative waifu in the grid till end
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


async def random_to_end(navi):
    # Use random waifu in the grid till end
    # stage 1
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_1_grid.png"))
    # stage 2
    await navi.continue_grid(random.randrange(0, 15))
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_2_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_2_default.png"))
    # stage 3
    await navi.continue_grid(random.randrange(0, 15))
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_3_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_3_default.png"))
    # stage 4
    await navi.continue_grid(random.randrange(0, 15))
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_4_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_4_default.png"))
    # stage 5
    await navi.continue_grid(random.randrange(0, 15))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_5_default.png"))


async def refresh_to_end(navi):
    # Refresh the grid at each stage, then use first selection of the grid to proceed till end
    # stage 1
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_1_grid.png"))
    await navi.refresh()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_1_grid_refresh.png"))
    # stage 2
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_2_grid.png"))
    await navi.refresh()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_2_grid_refresh.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_2_default.png"))
    # stage 3
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_3_grid.png"))
    await navi.refresh()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_3_grid_refresh.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_3_default.png"))
    # stage 4
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_4_grid.png"))
    await navi.refresh()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "stage_4_grid_refresh.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_4_default.png"))
    # stage 5
    await navi.continue_grid(0)
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "stage_5_grid.png"))


async def first_to_end_and_back(navi):
    # Use first alternative waifu in the grid till end,
    # then go back to stage 1
    # stage 1
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "1_grid.png"))
    # stage 2
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "2_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "2_default.png"))
    # stage 3
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "3_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "3_default.png"))
    # stage 4
    await navi.continue_grid(0)
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "4_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "4_default.png"))
    # stage 5
    await navi.continue_grid(0)
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "5_default.png"))
    # stage 6 (4)
    await navi.back()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "6_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "6_default.png"))
    # stage 7 (3)
    await navi.back()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "7_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "7_default.png"))
    # stage 8 (2)
    await navi.back()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "8_grid.png"))
    await navi.waifu_default_screenshot(os.path.join(test_screenshot_dir, "8_default.png"))
    # stage 9 (1)
    await navi.back()
    await navi.waifu_grid_screenshot(os.path.join(test_screenshot_dir, "9_grid.png"))


async def test_process(test_func):
    start_time = time.time()
    navi = await SiteNavigator.create_navi()
    await test_func(navi)
    print("Time taken: {}".format(time.time() - start_time))


if __name__ == '__main__':

    if not os.path.exists(test_screenshot_dir):
        os.mkdir(test_screenshot_dir)
    # Clear all .png files under the test_screenshot_dir
    for filename in os.listdir(test_screenshot_dir):
        if filename.endswith(".png"):
            os.remove(os.path.join(test_screenshot_dir, filename))

    # Select one of the above functions to test
    test_func = random_to_end
    asyncio.get_event_loop().run_until_complete(test_process(test_func))
