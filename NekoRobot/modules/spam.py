from NekoRobot import pgram, DRAGONS
from pyrogram import filters,enums
from pyrogram.errors import FloodWait 

@pgram.on_message(filters.command("spam") & filters.user(DRAGONS) & ~filters.private)
async def _spam(_, message):
    if len(message.command) < 2 or message.reply_to_message:
        return await message.reply_text("ᴜsᴀɢᴇ :- /spam [ᴀᴍᴏᴜɴᴛ ᴏғ ɴᴜᴍʙᴇʀ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴘᴀᴍ] [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ.]")
    try:
        if len(message.command) == 2:
            amt = message.text.split(None,1)[1]

        if len(message.command) > 2:
            amt = message.text.split(None,2)[1]
            text = message.text.split(None,2)[2]
    except Exception:
        pass
    if amt.isdigit():
        amt = int(amt)
    else:
        return await message.reply_text("ʙʀᴜʜ ᴛᴇʟʟ ᴍᴇ ʜᴏᴡ ᴍᴀɴʏ ᴛɪᴍᴇs ᴅᴏ ɪ sᴘᴀᴍ ᴍᴇssᴀɢᴇ. ᴛʜᴇ ᴀʀɢᴜᴍᴇɴᴛ ʏᴏᴜ ᴀʀᴇ ᴘʀᴏᴠɪɴɢ ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀ.")
    
    if amt > 100:
        return await message.reply_text("ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʟɪᴍɪᴛᴀᴛɪᴏɴs ɪ ᴄᴀɴ ᴏɴʟʏ sᴘᴀᴍ ᴜᴘᴛᴏ 𝟷𝟶𝟶.")

    for steve in range(amt):
        await pgram.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        try:
            if message.reply_to_message:
                await message.reply_to_message.reply_text(text)
            else:
                await pgram.send_message(message.chat.id,text) 
        except FloodWait as e:
            await asyncio.sleep(e.value)
