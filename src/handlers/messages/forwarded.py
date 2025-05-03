import logging

from aiogram import F, Router, types

# Create a router instance specific to forwarded message handlers
forwarded_router = Router(name="forwarded")


@forwarded_router.message(F.forward_origin)
async def handle_forwarded_message(message: types.Message):
    """Handles forwarded messages."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    text_preview = message.text[:50] + "..." if message.text else "[No text]"
    try:
        logging.info(f"Received forwarded message from user {user_id}: {text_preview}")
        # TODO: Add parsing/handling logic for forwarded messages here
        await message.answer(
            "Вижу пересланное сообщение, обрабатываю..."
        )  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_forwarded_message for user {user_id}: {e}",
            exc_info=True,
        )
        await message.answer("Произошла ошибка при обработке пересланного сообщения.")
