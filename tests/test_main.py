import logging
from unittest.async_case import IsolatedAsyncioTestCase

import pytest
import asyncio
from unittest.mock import AsyncMock

from main import plus, start


@pytest.mark.asyncio
async def test_plus():
    text_mock = "test123"
    message_mock = AsyncMock(text=text_mock)
    await plus(message=message_mock)
    message_mock.answer.assert_called_with(text_mock * 2)


@pytest.mark.asyncio
async def test_start():
    text_mock = "/start"
    expected_result = "старт команда!"
    message_mock = AsyncMock(text=text_mock)
    await start(message=message_mock)
    message_mock.answer.assert_called_with(expected_result)
