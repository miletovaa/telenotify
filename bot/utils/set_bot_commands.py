from aiogram import Bot
from aiogram.types import BotCommand


commands = [
    BotCommand(command="work", description="Work mode"),
    BotCommand(command="general", description="General mode"),
    BotCommand(command="personal", description="Personal mode"),
]


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(commands=commands)
