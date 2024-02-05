import config

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message
from db import Database
from user import UserInfo
import instance
import uuid
import shutil
import os
import re
import time
from state import Form
from language import Language
import logging
from logger_config import logger

class BOT():
    def __init__(self):
        self.dp = Dispatcher()
        self.bot = instance.bot
        self.language = Language()
        self.image = instance.image_instance
        self.color = instance.color
        self.admin_id = config.admin_id
        self.blocked_users = instance.blocked_users

        #command
        self.dp.message(CommandStart())(self.command_start_handler)   
        self.dp.message(Form.set_bg_color, F.photo | F.document)(self.image.background_set)
        self.dp.message(Form.set_bg_color, F.web_app_data)(self.color.recive_web_color)
        self.dp.message(Form.set_bg_color)(self.cancel_operation)       
        self.dp.message(F.photo | F.document)(self.image.read_process)

    async def command_start_handler(self, message: Message):
        info = UserInfo(message)
        chat_id = info.chat_id
        user_id = info.user_id
        username = info.username
        language_code = info.language
        first_name = info.first_name
        try:
            if user_id in self.blocked_users:
                loading = self.language.loading(language_code)
                await message.reply(loading)
                return
            self.image.delate(user_id) #delate all
            Database().insert_user_data(user_id, username)
            start_text = self.language.start_lang(first_name, language_code)
            await message.answer(start_text)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{user_id}:{ex}")

    async def cancel_operation(self, message: Message, state: FSMContext):
        chat_id = message.chat.id
        user_id = message.from_user.id
        text = message.text
        language_code = message.from_user.language_code
        try:
            cancel = Language().cancel(language_code)
            operation_deleted = Language().operation_deleted(language_code)
            if text == cancel:           
                # active = False
                # self.user_instance.user_state(user_id, active)  
                
                await state.clear()
                # keyboard = instance.keyboard_instance.create_start_reply_keyboard(message)
                await message.answer(operation_deleted, reply_markup=types.ReplyKeyboardRemove()) 
                
                self.image.delate(user_id) #delate all

                # if user_id in blocked_users:
                #     del blocked_users[user_id]  # sblocca utente
                return True
            else :
                return False
            return
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{user_id}:{ex}")


