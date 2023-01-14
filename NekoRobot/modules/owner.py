from NekoRobot import pgram, OWNER_ID
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button=InlineKeyboardMarkup([[InlineKeyboardButton(text="owner",url=f"https://t.me/JUMPMAN_BOY")],[InlineKeyboardButton(text="join here", url="https://t.me/EXTINCTION_XD")]])  
       

@pgram.on_message(filters.command("owner"))
async def _owner(_, message):
    await message.reply_text("here is my owner and join link",reply_markup=button)
