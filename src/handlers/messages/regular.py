import logging

from aiogram import Router, types

# Create a router instance specific to regular message handlers
regular_router = Router(name="regular")


@regular_router.message()
async def handle_regular_message(message: types.Message):
    """Handles any regular message not caught by previous handlers in this router."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    text_preview = message.text[:50] + "..." if message.text else "[No text]"
    try:
        logging.info(f"Received regular message from user {user_id}: {text_preview}")
        # TODO: Add default response or logic here
        await message.answer("Получил ваше сообщение.")  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_regular_message for user {user_id}: {e}", exc_info=True
        )
        await message.answer("Произошла ошибка при обработке сообщения.")
