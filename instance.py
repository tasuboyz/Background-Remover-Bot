import config
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import F, Bot
import logging
from aiogram.enums import ParseMode
from color import ColorManager
from reply_keyboard import Keyboard_Manager
from language import Language
from image import FileManager

bot_token=config.TOKEN
admin_id = config.admin_id

if config.use_local_api:
    session = AiohttpSession(
            api=TelegramAPIServer.from_base(config.api_base_url)
    )
    bot = Bot(bot_token, session=session, parse_mode=ParseMode.HTML)
else:
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)

blocked_users = {}

language_instance = Language()
keyboard_instance = Keyboard_Manager(language_instance)
color = ColorManager(bot, keyboard_instance, language_instance)
image_instance = FileManager(bot, admin_id, language_instance, color)
