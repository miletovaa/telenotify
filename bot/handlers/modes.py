from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from bot.utils.set_bot_commands import commands

router = Router()


@router.message(Command(commands=commands))
async def mode_handler(message: types.Message, command: CommandObject):
    selected_mode = command.text[1:]
    await message.answer("Changing the mode to %s" % selected_mode)
