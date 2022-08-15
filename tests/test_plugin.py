"""
    Plugin unit tests
"""
import time
import pytest
from unittest.mock import Mock

from nonebug import App


@pytest.mark.asyncio
async def test_random_waifu(app: App, load_waifulabs, monkeypatch):
    # Import the matcher to test
    from plugins.waifulabs import generate_random_waifu_matcher
    from plugins.waifulabs.site_navigator import SiteNavigator
    # Import the platform-specific Message and Event type.
    from nonebot.adapters.onebot.v11 import Message, MessageEvent
    from nonebot.adapters.onebot.v11.event import Sender

    async with app.test_matcher(generate_random_waifu_matcher) as ctx:
        bot = ctx.create_bot()

        # Test message content
        raw_msg = "随机老婆"
        msg = Message(raw_msg)
        # Test event
        event = MessageEvent(
            post_type="message",
            sub_type="normal",
            user_id=123456789,
            message_type="group",
            message_id=123456789,
            message=msg,
            original_message=msg,
            raw_message=raw_msg,
            font=1,
            sender=Sender(),
            to_me=True,
            time=time.time(),
            self_id=123456789,
        )

        # mock_navi = Mock(spec_set=SiteNavigator)

        async def test_mock_func():
            print("I'm here!!!")
        monkeypatch.setattr(SiteNavigator, "create_navi", test_mock_func)

        # Emulate receiving the event
        ctx.receive_event(bot, event)

        # Test expected response
        ctx.should_call_send(event, "正在生成随机老婆...", True)
        # ctx.should_finished()

        # mock_navi.assert_called()
