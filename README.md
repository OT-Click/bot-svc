# bot-svc

A Telegram bot that forwards messages via RabbitMQ for data extraction, displays job vacancy statuses, and can initiate contact with users mentioned in messages.

## Setup Instructions

### Prerequisites

*   Python >= 3.12
*   [uv](https://github.com/astral-sh/uv) (installation instructions on their page)
*   VSCode IDE
*   Recommended VSCode Extensions:
    *   `ms-python.python`
    *   `ms-python.debugpy` (Python Debugger)
    *   `charliermarsh.ruff`

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd bot-svc
    ```
2.  Create and activate a virtual environment (optional but recommended):
    ```bash
    # uv automatically creates and manages a .venv if one doesn't exist
    # You can activate it if needed:
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    uv sync
    ```

## Configuration

1.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
2.  Edit the `.env` file and add your actual Telegram Bot Token:
    ```dotenv
    BOT_TOKEN=your_actual_telegram_bot_token_here
    ```
    *Note: The `.env` file is ignored by git.* 

## Running the Bot

Make sure your virtual environment is active and the `.env` file is configured.

```bash
python src/main.py
```

The bot should start polling for messages.

## Development

*   **Project Structure:** 
    *   The main application code resides in the `src/` directory.
    *   `src/main.py`: Main entry point for the application.
    *   `src/config/`: Configuration loading (settings, logging).
    *   `src/handlers/`: Aiogram handlers for commands and messages.
    *   `src/middlewares/`, `src/services/`, `src/utils/`, `src/database/`: Placeholders for future modules (middleware, business logic, utilities, database interactions).
*   **Package Management:** Dependencies are managed using `uv` and defined in `pyproject.toml`.
*   **Linting/Formatting:** `ruff` is used for linting and formatting. It's configured in `pyproject.toml` and integrated with VSCode to format on save.
*   **Type Checking:** `pyright` is used for static type checking, configured in `pyproject.toml`.

## Debugging (VSCode)

1.  Ensure your `.env` file is correctly configured with the `BOT_TOKEN`.
2.  Open the project folder in VSCode.
3.  Go to the "Run and Debug" panel (usually accessible via a play button with a bug icon on the sidebar).
4.  Select the "Python: Bot Module" configuration from the dropdown menu at the top.
5.  Set breakpoints in your code (e.g., within `src/main.py`).
6.  Click the green play button to start debugging.

Execution should stop at your breakpoints, allowing you to inspect variables and step through the code.
