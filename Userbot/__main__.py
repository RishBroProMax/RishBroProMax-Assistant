import os,time
from time import sleep
from Userbot import bot
from config import Config
from Userbot.plugins import*
from pyrogram import filters, idle, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, CallbackQuery, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from requests import get,post
import asyncio
import logging
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
import requests
from Userbot import LOG
from Userbot.inline import START_MESSAGE_BUTTONS, LOGO, VISIT_PM, BACK_BUTTONS, HELP_TEXT, HELP_BUTTONS, HELP_TEXT2, LOGO_TEXT, HELP_BACK_BUTTONS, SONG_TEXT, QUOTE_TEXT, URL_TEXT, COVID_TEXT, SMS_TEXT, HACK_TEXT, CLOSE_BUTTONS, CLOSE_TEXT
from Userbot.helpers.addusers import AddUserToDatabase, AddChatToDatabase
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


@bot.on_message(filters.command('start') & filters.private)
async def command1(bot, message):
	await AddUserToDatabase(bot, message)
	m = await bot.send_sticker(message.from_user.id, Config.START_STICKER)
	time.sleep (0.7)
	reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
	await bot.send_photo(
		message.chat.id,
		photo=Config.START_PIC,
		caption=f"""**💠 | Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id}) ...\n \nI am The Assistant Bot Of [Rishmika Sandanu](https://t.me/ImRishmika)**.\n\n💬 You Can Contract Him Using This Bot.\n📨 Send Your Messages Normally And I Will Forward Them To Him. ☘️  """,
		reply_markup=reply_markup
		)
	await m.delete()

@bot.on_message(filters.command('help'))
async def command2(bot, message):
	text=HELP_TEXT2
	reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
	await message.reply_text(
		text=text,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command(['start', 'otpbomber']) & filters.group)
async def command3(bot, message):
	await AddUserToDatabase(bot, message)
	text="""|    """
	reply_markup = InlineKeyboardMarkup(VISIT_PM)
	await bot.send_photo(
		message.chat.id,
		photo=Config.START_PIC,
		caption="| ",
		reply_markup=reply_markup,
		)

@bot.on_message(filters.command("rp") & filters.user(Config.OWNER))
async def send_requ(bot, message):
	query = message.text.split(None, 1)[1]
	x=post("https://api.telegram.org/bot"+Config.BOT_TOKEN+"/sendMessage?chat_id="+query+"").text
	print (" \n \n SEND_MSG { \n \n "+x+" \n \n } \n")


@bot.on_callback_query()
def callback_query(Client, Callback_Query):
	if Callback_Query.data == "helpmenu":
		Callback_Query.edit_message_text(
			HELP_TEXT,
			reply_markup=InlineKeyboardMarkup(BACK_BUTTONS),
		)
	elif Callback_Query.data == "Back":
		CALLBACK = f"""**💠 | Hello... \n \nI am The Assistant Bot Of [Rishmika Sandanu](https://t.me/ImRishmika)** .\n\n💬 You Can Contract Him Using This Bot.\n📨 Send Your Messages Normally And I Will Forward Them To Him. ☘️  """
		Callback_Query.edit_message_text(
			CALLBACK,
			reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS),
		)
	elif Callback_Query.data == "helpback":
		reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
		Callback_Query.edit_message_text(
			HELP_TEXT2,
			reply_markup = reply_markup,
		)
	elif Callback_Query.data == "url":
		Callback_Query.edit_message_text(
			URL_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "logo":
		Callback_Query.edit_message_text(
			LOGO_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "quote":
		Callback_Query.edit_message_text(
			QUOTE_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "song":
		Callback_Query.edit_message_text(
			SONG_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "covid":
		Callback_Query.edit_message_text(
			COVID_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "otpbomber":
		Callback_Query.edit_message_text(
			SMS_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "hack":
		Callback_Query.edit_message_text(
			HACK_TEXT,
			reply_markup = InlineKeyboardMarkup(HELP_BACK_BUTTONS),
		)
	elif Callback_Query.data == "close":
		c = Callback_Query.edit_message_text(
			CLOSE_TEXT,
			reply_markup = InlineKeyboardMarkup(CLOSE_BUTTONS)
		)
		time.sleep(1.2)
		c.delete()

stats = """
💖 Thank you for use my bot
Stay with me forever. ❤️‍🔥
"""

@bot.on_callback_query(filters.regex("stats_callback"))
async def stats_callbacc(_, CallbackQuery):
	text = stats
	await bot.answer_callback_query(CallbackQuery.id, text, show_alert=True)

IF_TEXT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

@bot.on_message(filters.private & filters.text)
async def pm_text(bot, message):
	if message.from_user.id == Config.OWNER:
		await bot.send_message(chat_id=Config.OWNER, text=f"**You are Owner 🌝🏖️️**")
		return
	info = await bot.get_users(user_ids=message.from_user.id)
	reference_id = int(message.chat.id)
	await bot.send_message(
		chat_id=Config.OWNER,
		text=IF_TEXT.format(reference_id, info.first_name, message.text),
	)

@bot.on_message(filters.private & filters.media)
async def pm_media(bot, message):
	await message.reply_text(f"**Media is Not Supported... 🏖️️ \n \nSend it to @ImRishmika_Bot ✅**")

async def main_startup():
    print (LOGO)
    await bot.start()
    logging.info("Bot Is Fucking Now...")
    try:
        await bot.send_message(chat_id=Config.LOG_GRP, text=f"**[{Config.BOT_NAME} ✅](https://t.me/{Config.BOT_USERNAME}) is Online.**.", disable_web_page_preview=True)
    except:
        logging.warn("error")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
