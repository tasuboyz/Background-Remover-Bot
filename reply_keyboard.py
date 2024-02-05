from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import os

class Keyboard_Manager:
    def __init__(self, language_instance):
        self.color_url = 'https://python-telegram-bot.org/static/webappbot'
        self.lang = language_instance

    def color_chooser(self, message):
        language_code = message.from_user.language_code
        cancel = self.lang.cancel(language_code)
        choose_color = self.lang.choose_color(language_code)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
            [
                KeyboardButton(text=choose_color, web_app=WebAppInfo(url=self.color_url))
            ],
            [
                KeyboardButton(text=cancel) 
            ]                                    
        ])
        return keyboard
    
    def create_user_keyboard(self):
        keyboard = []               
        keyboard.append([InlineKeyboardButton(text="📦 Invia Messaggio agli Utenti", callback_data="send_message")])       
        # keyboard.append([InlineKeyboardButton(text="🔍 Dettagli utenze attive", callback_data="details")])
        keyboard.append([InlineKeyboardButton(text="🧹 Pulizia Utenti", callback_data="clean"),
                                InlineKeyboardButton(text="🔍 Elenco Utenti", callback_data="users")])
        keyboard.append([InlineKeyboardButton(text="Send Ads", callback_data="ads")])
        keyboard.append([InlineKeyboardButton(text="Annulla ❌", callback_data="cancel")])

        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard


