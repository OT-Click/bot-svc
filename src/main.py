import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from pydantic import ValidationError

# Import refactored components
from config import Settings, setup_logging  # Import from config package
from handlers import all_routers  # Import the aggregated list of routers

# --- Setup Logging ---
# Configure logging using the function from the config module
setup_logging()


# --- Load Settings ---
try:
    settings = Settings()  # type: ignore
    BOT_TOKEN_STR = settings.bot_token.get_secret_value()
except ValidationError as e:
    logging.error(f"Error loading settings: {e}")
    sys.exit("Could not load settings. Check your .env file or environment variables.")
except AttributeError:
    logging.error("Error: BOT_TOKEN is missing in settings.")
    sys.exit("BOT_TOKEN must be set in your .env file or environment variables.")


# --- Main Function ---
async def main():
    # Initialize bot
    bot = Bot(token=BOT_TOKEN_STR)
    # Initialize dispatcher
    dp = Dispatcher()

    # Include all routers from the handlers package
    # The order is defined in handlers/__init__.py
    for router in all_routers:
        dp.include_router(router)

    # Set up bot commands (optional, can be expanded)
    commands = [
        BotCommand(command="my_vacancies", description="Показать мои вакансии")
        # Add other commands here if needed
    ]
    try:
        await bot.set_my_commands(commands)
        logging.info("Bot commands set successfully.")
    except Exception as e:
        logging.error(f"Failed to set bot commands: {e}", exc_info=True)

    # Skip pending updates before starting polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        logging.info("Skipped pending updates.")
    except Exception as e:
        logging.error(f"Error deleting webhook: {e}", exc_info=True)

    # Start polling
    logging.info("Starting bot polling...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error during polling: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
