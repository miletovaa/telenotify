import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties

from bot.handlers import start, modes
from bot.utils.set_bot_commands import set_bot_commands
from bot.utils.setup_logging import setup_logging
from config import settings

bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode="HTML"))
logger = logging.getLogger(__name__)


async def run_bot():
    setup_logging()
    logger.info("Starting bot")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()

    # Register handlers
    dp.include_router(start.router)
    dp.include_router(modes.router)

    # Set bot commands in UI
    await set_bot_commands(bot)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        await bot.session.close()


asyncio.run(run_bot())
