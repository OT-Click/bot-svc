from .commands import commands_router
from .messages import forwarded_router, regular_router

# Define the order in which routers should be registered in the dispatcher
# Command handlers first, then specific message handlers, then general fallback
all_routers = [
    commands_router,
    forwarded_router,
    regular_router,  # This should generally be last for messages
]

__all__ = ["all_routers"]
