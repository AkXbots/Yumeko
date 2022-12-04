"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Awesome-Prince]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Awesome-Prince/NekoRobot-3 ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import random
import asyncio
import datetime
from datetime import datetime

from telegram import __version__ as ptb
from telethon import Button

from NekoRobot import BOT_NAME, BOT_USERNAME, SUPPORT_CHAT
from NekoRobot import tbot as neko
from NekoRobot.events import register

edit_time = 5
""" =======================Neko====================== """
file1 = "https://telegra.ph/file/da817befa131f7a5f533e.jpg"
file2 = "https://telegra.ph/file/a048c4fa0bdb2738fff69.jpg"
file3 = "https://telegra.ph/file/a62029574186f318c6529.jpg"
file4 = "https://telegra.ph/file/1368985b1a20870949673.jpg"
file5 = "https://telegra.ph/file/7dcde6edba760c620e91f.jpg"
""" =======================Neko====================== """

PHOTO = [
    "https://graph.org/file/8da1926f37ba046380333.jpg",
    "https://graph.org/file/c524b116572aeab85de10.jpg",
    "https://graph.org/file/0207ffe5c34d8def45246.jpg",
    "https://graph.org/file/575bb37708e2c571cb142.jpg",
    "https://graph.org/file/dbbeff71ace10c605b517.jpg",
]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    NekoX = f"**👋Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}) Senpai\n\n🌟I'm {BOT_NAME}\n🌹I'm Working Fine as Always **\n\n"
    NekoX += f"**⚡️My Uptime :** `{uptime}`\n\n"
    NekoX += f"**🐍PTB Version :** `{ptb}`\n\n"
    BUTTON = [
        [
            Button.url("🏥 Support", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await neko.send_file(yes.chat_id, ran, caption=NekoX, buttons=BUTTON)
