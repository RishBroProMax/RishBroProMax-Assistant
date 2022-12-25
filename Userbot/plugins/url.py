from Userbot import bot as url
import pyshorteners
from pyrogram import filters, idle, Client, enums
from pyrogram.types import *
from config import Config

@url.on_message(filters.command('url'))
async def command1(_, message):
    a = await message.reply(text="`Processing...`")
    try:
        link = message.text.split(None, 1)[1]
        if not link:
            return await a.edit("🚧 Please Give me a Link to Shorten...")
        txt = pyshorteners.Shortener()
        if "http://tinyurl.com" in link.lower():
            ok = txt.tinyurl.expand(link)
            eu = "Expanded"
        else:
            ok = txt.tinyurl.short(link)
            eu = "Shortned"
        short = (
            f"**🛸 Url Shortned**\n \n**Given Link** ➠ `{link}`\n"
            f"**{eu} Link** ➠ `{ok}`\n \n"
            f"**[{Config.BOT_NAME} ✅](https://t.me/{Config.BOT_USERNAME})**"
        )
        await a.edit(text=short, disable_web_page_preview=True)
    except Exception as e:
        await a.edit("SomeThing Went Wrong. \n \n**🚫 ERROR**")
