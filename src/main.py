import asyncio
import logging  # Import logging module
import sys  # Import sys for exiting

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command  # Import Command filter
from aiogram.types import BotCommand  # Import BotCommand
from pydantic import SecretStr, ValidationError
from pydantic_settings import BaseSettings

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# --- Pydantic Settings ---
class Settings(BaseSettings):
    # Define your settings here
    bot_token: SecretStr  # Use SecretStr for sensitive values

    class Config:
        # Load from a .env file (default)
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Ignore extra fields from .env


# --- Bot Setup ---
try:
    # Load settings
    settings = Settings()  # type: ignore
    BOT_TOKEN_STR = settings.bot_token.get_secret_value()  # Get the actual string
except ValidationError as e:
    print(f"Error loading settings: {e}")
    # Optionally provide more details from e.errors()
    sys.exit("Could not load settings. Check your .env file or environment variables.")
except AttributeError:
    # Handle case where bot_token might not be set at all
    print("Error: BOT_TOKEN is missing in settings.")
    sys.exit("BOT_TOKEN must be set in your .env file or environment variables.")


# --- Routers --- # Renamed and new router created
commands_router = Router(name="commands")  # Router for command handlers
messages_router = Router(name="messages")  # Router for message handlers

# Initialize dispatcher
dp = Dispatcher()


# --- Command Handlers (in commands_router) ---
@commands_router.message(Command("my_vacancies"))
async def handle_my_vacancies(message: types.Message):
    """Handles the /my_vacancies command."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    try:
        logging.info(f"Received /my_vacancies from user {user_id}")
        await message.answer("Вот ваши вакансии:")  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_my_vacancies for user {user_id}: {e}", exc_info=True
        )
        await message.answer("Произошла ошибка при показе вакансий.")


# --- Message Handlers (in messages_router) ---


# Handler for forwarded messages
@messages_router.message(F.forward_origin)
async def handle_forwarded_message(message: types.Message):
    """Handles forwarded messages."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    text_preview = message.text[:50] + "..." if message.text else "[No text]"
    try:
        logging.info(f"Received forwarded message from user {user_id}: {text_preview}")
        # Add parsing/handling logic for forwarded messages here
        await message.answer(
            "Вижу пересланное сообщение, обрабатываю..."
        )  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_forwarded_message for user {user_id}: {e}",
            exc_info=True,
        )
        await message.answer("Произошла ошибка при обработке пересланного сообщения.")


# Fallback handler for regular messages (must be last in this router)
@messages_router.message()
async def handle_regular_message(message: types.Message):
    """Handles any regular message not caught by previous handlers in this router."""
    user_id = message.from_user.id if message.from_user else "Unknown"
    text_preview = message.text[:50] + "..." if message.text else "[No text]"
    try:
        logging.info(f"Received regular message from user {user_id}: {text_preview}")
        # Add default response or logic here
        await message.answer("Получил ваше сообщение.")  # Mock response
    except Exception as e:
        logging.error(
            f"Error in handle_regular_message for user {user_id}: {e}", exc_info=True
        )
        await message.answer("Произошла ошибка при обработке сообщения.")


# --- Main Function ---
async def main():
    # Initialize bot inside main
    bot = Bot(token=BOT_TOKEN_STR)

    # Set up bot commands
    commands = [
        BotCommand(command="my_vacancies", description="Показать мои вакансии")
        # Add other commands here
    ]
    await bot.set_my_commands(commands)

    # Include routers in the dispatcher
    # Order matters: commands first, then general messages
    dp.include_router(commands_router)
    dp.include_router(messages_router)

    # Skip pending updates
    await bot.delete_webhook(drop_pending_updates=True)
    # Start polling
    logging.info("Starting bot polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
