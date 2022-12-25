import os
import pyrogram
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

HELP_TEXT = f"""
Hey there... 😇

**🛸 I have some fun and useful tools. 👻
So you can get a help about them. 🚀**

  Click " /help "

||💖 Thank you for use my bot
Stay with me forever... ❤️‍🔥||

**[DɪʟᴜᴍBBᴀɴᴅᴀʀᴀ](https://t.me/{Config.C_CHANNEL})**

"""

HELP_TEXT2 = f"""
Hey there... ☄️

**🛸 I have some fun and useful tools. 👻
So you can get a help about them. 🚀**

||💖 Thank you for use my bot
Stay with me forever... ❤️‍🔥||

**[DɪʟᴜᴍBBᴀɴᴅᴀʀᴀ](https://t.me/{Config.C_CHANNEL})**

"""
CLOSE_BUTTONS = [
	[
	InlineKeyboardButton('匚ㄥㄖ丂|几ᘜ ...', callback_data='stats_callback'),
	],
]

CLOSE_TEXT = """🏖️️ Closing... 🔫"""

SONG_TEXT = """

**🎧 Help For Song Download 🎧**

**Available Commands**

❥ `/song {song name}` - Download a song simply.
❥ `/song {youtube link}` - Download song using youtube link.

"""
LOGO_TEXT = """

**🏙 Help For Logo Make 🌄**

**Available Commands**

❥ `/logo {text}`  - Create Simple Random Logos
❥ `/mlogo {text}` - Write Something
❥ `/xlogo {text}` - Create SriLankan Mask Logo

"""
QUOTE_TEXT = """
**💬 Help for Quote 💬**

**Available Commands**

❥ `/q` - Reply to a message to make it quote.

"""
URL_TEXT = """

**🚧 Help for Link Shorten. 🚧**

**Available Commands**

❥ `/url {Link}` - Link Shorten

"""
COVID_TEXT = """
**🧰 Help for Covid 🧰**

**Available Commands**

❥ `/covid` - Get the Covid status of Sri Lanka 🇱🇰


"""
HACK_TEXT = """

**🛸 Help for Hack 🛸**

**Available Commands**

❥ `/hack`

"""

HELP_BUTTONS = [
	[
	InlineKeyboardButton("Url", callback_data='url'),
	],
	[
	InlineKeyboardButton("Logo", callback_data='logo'),
	],
	[
	InlineKeyboardButton("Song", callback_data='song'),
	],
	[
	InlineKeyboardButton("Covid", callback_data='covid'),
	],
	[
	InlineKeyboardButton("Quote", callback_data='quote'),
	],
	[
	InlineKeyboardButton("SMS-Bomber", callback_data='otpbomber'),
	],
	[
	InlineKeyboardButton("Hack", callback_data='hack'),
	],
	[
	InlineKeyboardButton(text='Close 🗑', callback_data='close'),
	],
]

SMS_TEXT = """

**🚫 Help for SMS-Bomber 🚫**

**Available Commands**

❥ `/otpbomber {phone number}` - **[SMS-Bomber](https://t.me/Mars11Lkbot)**

"""

START_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('☃︎━━━━━━━━━━━━━━☃︎', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('☘️ CHANNEL ☘️', url=f'https://t.me/{Config.CHANNEL}'),
	InlineKeyboardButton('🍁 Discussion 🍁', url=f'https://t.me/{Config.GROUP}'),
	],
	[
	InlineKeyboardButton(text='🌺 Help 🌺', callback_data='helpmenu'),
	],
	[
	InlineKeyboardButton(text='Close 🗑', callback_data='close'),
	],
	[
	InlineKeyboardButton(text='➕ Add Me to Your Group ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true'),
	],
]

BACK_BUTTONS = [
	[
	InlineKeyboardButton('🔙 Back', callback_data="Back"),
	],
]

HELP_BACK_BUTTONS = [
	[
	InlineKeyboardButton('🔙 Back', callback_data="helpback"),
	],
]

FTEXT = f" **🚫Access Denied🚫** \n \nYou Must Join Our Channel To Use Me. So, Please Join it & Try Again. ☘️"

CAPTION_TEXT = [
	[
	InlineKeyboardButton("🙋Join Channel", url=f"https://t.me/{Config.CHANNEL}"),
	],
]

VISIT_PM = [
	[
	InlineKeyboardButton('━━━━━━━━━━━━━━', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('☘️ Visit PM ☘️', url=f'https://t.me/{Config.BOT_USERNAME}?start'),
	],
]

LOGO = """

BOT STARTING IN PROGRESS... ✅

"""
