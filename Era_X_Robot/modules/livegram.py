from pyrogram import Client, filters
from pyrogram.types import Message

from Era_X_Robot import OWNER_ID
from Era_X_Robot import pbot as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
