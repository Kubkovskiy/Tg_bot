from aiogram import Dispatcher
from aiogram.types import Message

from tg_bot.filters.admin import AdminFilter


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, AdminFilter, commands=["start"], state="*", is_admin=True)