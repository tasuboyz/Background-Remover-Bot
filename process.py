from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

import os
import uuid
import shutil
# from db import Database
import instance
import logging
import asyncio 
import config

from multiprocessing import Process, process
# from language import Language
from user import UserInfo

from PIL import Image, ImageColor, ImageOps ,ImageDraw, ImageFont, ImageFilter
from user import UserInfo
from aiogram import types
        
async def process_bg_background(file_name, color, bg_file=None):
    background_process = Process(target=process_background_remover, args=(file_name, color, bg_file))
    background_process.start()
    while background_process.is_alive():
        await asyncio.sleep(1)
        
def process_background_remover(file_name, color, bg_file):
    instance.image_instance.background_remover(file_name, color, bg_file) 
    
async def process_convert_mp4(file_name):
    convert_process = Process(target=process_convertion, args=(file_name,))
    convert_process.start()
    while convert_process.is_alive():
        await asyncio.sleep(1)
    
def process_convertion(file_name):
    instance.image_instance.convert_mp4(file_name)
    
# async def custom_light(message, color, image, wait_message):
#     info = UserInfo(message)
#     user_id = info.user_id
#     process_bg_background(image, color)                        