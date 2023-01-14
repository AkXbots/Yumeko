from NekoRobot import pgram, OWNER_ID
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button=InlineKeyboardMarkup([[InlineKeyboardButton(text="⚡Owner",url=f"https://t.me/JUMPMAN_BOY")],[InlineKeyboardButton(text="Join Here 💬", url="https://t.me/EXTINCTION_XD")]])  
       

@pgram.on_message(filters.command("owner"))
async def _owner(_, message):
    await message.reply_text("Here is my Owner and My Owners Group Link",reply_markup=button)
