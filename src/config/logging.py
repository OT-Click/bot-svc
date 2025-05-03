import logging
import sys


def setup_logging(level: int | str = logging.INFO):
    """Configures basic logging for the application."""
    # Check if handlers are already configured
    # This prevents adding multiple handlers if the function is called again
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            stream=sys.stdout,  # Log to stdout
        )
        logging.info("Logging configured successfully.")
    else:
        logging.info("Logging already configured.")
