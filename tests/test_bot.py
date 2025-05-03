from unittest.mock import AsyncMock

import pytest

# Assuming echo_message is importable from src.main or a handlers module
from src.main import echo_message


@pytest.mark.asyncio
async def test_echo_message():
    # Create a mock message object
    message = AsyncMock()

    # Call the handler
    await echo_message(message)

    # Assert the message.answer was called with the expected response
    message.answer.assert_called_once_with("Приветствием")
