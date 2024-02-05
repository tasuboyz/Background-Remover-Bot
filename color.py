from mailbox import Message
import sqlite3
import json

from aiogram.types import ReplyKeyboardRemove

from aiogram.fsm.context import FSMContext
from state import Form
from user import UserInfo
from db import Database
import asyncio
import instance
import process
import logging
import config
from aiogram import types
import glob
import os
from logger_config import logger

class ColorManager: # crea una classe per gestire i colori e le impostazioni del QR
    def __init__(self, bot, keyboard_instance, language_instance):
        self.admin_id = config.admin_id
        self.bot = bot
        self.blocked_users = instance.blocked_users
        self.keyboard_instance = keyboard_instance
        self.language_instance = language_instance
        self.semaforo = asyncio.Semaphore(1)

    def get_color_from_web(self, message):
        user_id = message.from_user.id
        data = json.loads(message.web_app_data.data) ##get data responce
        color = tuple(data['rgb'].values())     
        color = ','.join(map(str, color))
        Database().save_color_in_settings(user_id, color)
        return color
    
    async def color_choose(self, message: Message, state: FSMContext):
        keyboard = self.keyboard_instance.color_chooser(message)
        info = UserInfo(message)
        user_id = info.user_id
        await state.set_state(Form.set_bg_color)
        language_code = info.language
        rembg_mode = self.language_instance.rembg_mode(language_code)
        await message.answer(rembg_mode, reply_markup=keyboard)
        
    async def recive_web_color(self, message: Message, state: FSMContext):
        info = UserInfo(message)
        user_id = info.user_id
        message_id = info.message_id 
        chat_id = info.chat_id
        language_code = info.language
        try:
            await state.clear()
            self.blocked_users[user_id] = True
            wait = self.language_instance.waiting(language_code) 
            wait_message = await message.answer(wait, reply_markup=ReplyKeyboardRemove())
            await self.bot.delete_message(user_id, message_id)
            color = self.get_color_from_web(message)
            file_name = Database().get_image(user_id)
            async with self.semaforo:   
                await process.process_bg_background(file_name, color)
                input_file = types.FSInputFile(file_name)
                await self.bot.send_photo(chat_id, input_file)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{user_id}:{ex}")
        finally:
            await self.bot.delete_message(chat_id, wait_message.message_id)
            instance.image_instance.delate(user_id)
            if user_id in self.blocked_users:
                del self.blocked_users[user_id]
            
