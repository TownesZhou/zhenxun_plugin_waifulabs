from pyppeteer import launch
from random import randint
from time import sleep


class SiteNavigator:

    def __init__(self):
        # Launch browser and open a new page
        self.browser = None
        self.page = None
        self.stage = None

    # Have to use a factory static method to initialize, because __init__() cannot be an async function
    @staticmethod
    async def create_navi():
        navi = SiteNavigator()
        navi.browser = await launch()
        navi.page = await navi.browser.newPage()
        await navi.page.setViewport({'width': 1200, 'height': 630})
        # Go to the waifulabs site
        await navi.page.goto('https://waifulabs.com/generate')

        # Current stage number. Starts at 1, and ends at 5. There are in total four selections to make.
        navi.stage = 1
        return navi

    # It will take a while for waifulabs to generate a batch of waifus. Wait for them to be fully loaded.
    async def wait_for_loading(self):
        # Before the final stage, when loading, there is a div with class "loading-callout".
        # It will be removed when the waifulabs is done loading.
        if self.stage < 5:
            while await self.page.querySelector(".loading-callout"):
                sleep(0.1)
        # In the final stage, the loading div is the one with class "cross-fade-enter-exit"
        else:
            # while await self.page.querySelector(".cross-fade-enter-exit"):
            #     sleep(0.1)
            await self.page.waitForSelector(".cross-fade-enter-done", {'visible': True})

    # Take a screenshot of the default waifu
    async def waifu_default_screenshot(self, img_path):
        # Sanity check: not in first stage. There is no default waifu if the first stage.
        assert self.stage > 1
        await self.wait_for_loading()
        # The default waifu is contained inside an img element of a div with class "waifu-preview"
        await (await self.page.querySelector(".waifu-preview > img")).screenshot({'path': img_path})

    # Take a screenshot of the waifu grid
    async def waifu_grid_screenshot(self, img_path):
        # Sanity check: not in final stage. There is no grid in the final stage
        assert self.stage < 5
        await self.wait_for_loading()
        # The grid is contained inside a div with class "waifu-grid"
        await (await self.page.querySelector(".waifu-grid")).screenshot({'path': img_path})

    # Continue to next stage with default waifu
    async def continue_default(self):
        # Sanity check: not in first and last stage. If in first stage, must select one from the waifu grid
        assert 1 < self.stage < 5
        await self.wait_for_loading()
        # The continue/back button is contained inside a button with class "sc-bdvvtL"
        await (await self.page.querySelectorAll(".sc-bdvvtL"))[1].click()
        # Increment stage counter
        self.stage += 1

    # Continue to next stage with a selection of an alternative from the waifu grid
    async def continue_grid(self, selection_id: int):
        # Sanity check: not in last stage
        assert self.stage < 5
        # Sanity check: selection_id must be in range [0, 15]. In addition, 15 is reserved for refresh.
        assert selection_id in range(0, 16)
        if selection_id == 15:
            await self.refresh()
            return

        await self.wait_for_loading()
        # Get the waifu grid
        grid = await self.page.querySelectorAll(".waifu-grid > div")
        # Click a button to progress to next
        await grid[selection_id].click()
        # Increment stage counter
        self.stage += 1

    # Refresh the current selection
    async def refresh(self):
        # Sanity check: not in last stage
        assert self.stage < 5
        await self.wait_for_loading()
        # Get the waifu grid
        grid = await self.page.querySelectorAll(".waifu-grid > div")
        # Click the last refresh button to refresh the current selection
        await grid[15].click()

    # Go back to previous stage
    async def back(self):
        # Sanity check: not in first stage.
        assert self.stage > 1
        await self.wait_for_loading()
        # The continue/back button is contained inside a button with class "sc-bdvvtL"
        await (await self.page.querySelectorAll(".sc-bdvvtL"))[0].click()
        # Decrement stage counter
        self.stage -= 1
