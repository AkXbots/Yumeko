from pyrogram import Client, enums, filters
from pyrogram.types import Message
from NekoRobot import DRAGONS 

@Client.on_message(
    filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], ".") & (filters.me | filters.user(DRAGONS))
)
async def spam_stick(client: Client, message: Message):
    if message.chat.id in BLACKLIST_CHAT:
        return await message.reply_text(
            "This command is not allowed to be used in this group"
        )
    if not message.reply_to_message:
        await message.reply_text(
            "reply to a sticker with amount you want to spam"
        )
        return
    if not message.reply_to_message.sticker:
        await message.reply_text(
            "repjly to a sticker with amount you want to spam"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)
