from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - Chalcogen 
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - Chalcogen 
│├─────────────────╯
├┼─────────────────⦿
├┤~ @urschalco
├┤~ @alfaz_e_lafz
├┤~ @nexiaupdates
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @c7gen
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Chalcogen", url=f"https://t.me/c7gen")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/c7gen"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/urschalco"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/nexiaupdates"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/nexiamusicbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/qu0hhu.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
