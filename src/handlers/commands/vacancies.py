import logging

from aiogram import Router, types
from aiogram.filters import Command

# Create a router instance specific to command handlers
commands_router = Router(name="commands")


@commands_router.message(Command("my_vacancies"))
async def handle_my_vacancies(message: types.Message):
    """Handles the /my_vacancies command."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    try:
        logging.info(f"Received /my_vacancies from user {user_id}")
        # TODO: Replace with actual logic to fetch and display user vacancies
        await message.answer("Вот ваши вакансии:")  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_my_vacancies for user {user_id}: {e}", exc_info=True
        )
        await message.answer("Произошла ошибка при показе вакансий.")
