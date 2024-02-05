from PIL import Image, ImageColor, ImageOps ,ImageDraw, ImageFont, ImageFilter
from rembg import remove
import numpy as np
import io
import os
import time
import random
import uuid
import logging
import glob
import process
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from user import UserInfo
from db import Database
from logger_config import logger
import instance

class FileManager: # crea una classe per gestire i colori e le impostazioni del QR
    def __init__(self, bot, admin_id, language_instance, color):
        self.bot = bot
        self.admin_id = admin_id
        self.lang = language_instance
        self.color = color
        self.blocked_users = instance.blocked_users

    def resize(self, file_path, fill_color):
        color = tuple(map(int, fill_color.split(',')))
        if file_path.endswith(('.png', '.jpg', '.jpeg')):  # aggiungi qui altri formati di immagine se necessario
            im = Image.open(file_path)            
            if im.size[0] != im.size[1]: #Controlla se l'immagine è quadrata
                im_square = self.make_square(im, color)
                im_square.save(file_path)
                    
    def make_square(self, im, fill_color):
        try:
            min_size=256
            x, y = im.size
            size = max(min_size, x, y)
            new_im = Image.new('RGB', (size, size), fill_color)
            new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
            return new_im
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            
    async def background_set(self, message: Message, state: FSMContext):
        info = UserInfo(message)
        user_id = info.user_id
        chat_id = info.chat_id
        language_code = info.language
        await state.clear()
        try:           
            wait = self.lang.waiting(language_code) 
            wait_message = await message.answer(wait, reply_markup=ReplyKeyboardRemove())
            file_saved = Database().get_image(user_id)
            file_path, file_name = await self.recive_image(message)
            self.blocked_users[user_id] = True
            #self.background_remover(file_saved, None, file_name)
            await process.process_bg_background(file_saved, None, file_path)
            input_file = FSInputFile(file_saved)
            await self.bot.send_photo(chat_id, input_file)
            self.delate(user_id)
            file_info = FileInfo(file_path)
            name = file_info.file
            self.remove_file_if_exists(name)
            
            await self.bot.delete_message(chat_id, wait_message.message_id)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
        finally:
            if user_id in self.blocked_users:
                del self.blocked_users[user_id]

    def background_remover(self, file_name, color, background_image_path=None):
        try:
            base_name = os.path.splitext(file_name)[0]  # Ottieni il nome del file senza estensione
            output_path = f'{base_name}.png'  # Aggiungi '.png'

            with open(file_name, 'rb') as img_file:
                img = img_file.read()

            result = remove(img)

            img = Image.open(io.BytesIO(result)).convert("RGBA")

            # Se è fornito un percorso di immagine di sfondo, utilizzalo. Altrimenti, utilizza il colore.
            if background_image_path:
                background = Image.open(background_image_path).convert("RGBA")
                background = background.resize(img.size, Image.LANCZOS)  # Ridimensiona l'immagine di sfondo per adattarla all'immagine originale
            else:
                background_color = tuple(map(int, color.split(',')))
                background = Image.new('RGBA', img.size, background_color)

            img_with_background = Image.alpha_composite(background, img)  # Combina l'immagine e lo sfondo

            img_with_background.save(output_path)  # Salva l'immagine come PNG

            jpeg_path = f'{base_name}.jpg'  # Usa lo stesso nome base, ma con estensione '.jpg'
            img_jpeg = img_with_background.convert('RGB')  # Rimuovi il canale alfa
            img_jpeg.save(jpeg_path, 'JPEG')  # Salva l'immagine come JPEG
            # os.remove(output_path)   
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)

    def generate_random_filename(self, file_path):
        file_name, file_extension = os.path.splitext(file_path)
        random_suffix = random.randint(1000, 9999)
        return f"{file_name}_{random_suffix}{file_extension}"

    def check_file_exists(self, file_path):
        while os.path.exists(file_path):
            file_path = self.generate_random_filename(file_path)
        return file_path

    async def recive_image(self, message):
        chat_id = message.chat.id
        try:
            if message.document or message.photo or message.animation:
                file = message.document or message.photo[-1] or message.animation
                file_info = await self.bot.get_file(file.file_id)
                file_path = file_info.file_path                

                uid = uuid.uuid4()   # Genera un identificatore univoco                
                file_extension = file_path.split(".")[-1]# Ottieni l'estensione del file originale                
                file_name = f"{uid}.{file_extension}"  # Crea il nuovo nome del file con l'identificatore e l'estensione    

                # Specifica il percorso della directory in cui desideri salvare l'immagine
                directory_path = f"UserImage"
                if not os.path.exists(directory_path):
                    os.makedirs(directory_path)

                # Combina il percorso della directory con il nome del file
                download_path = os.path.join(directory_path, file_name)
                file_path = self.check_file_exists(file_path) # Aggiungi questa riga

                await self.bot.download_file(file_path, download_path)
                #await self.bot.download_file(file_path, download_path)

                return download_path, file_name
            return None
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{chat_id}:{ex}")           
    
    async def check_image(self, file_name, message):
        language_code = message.from_user.language_code
        file_not_valid = self.lang.file_not_valid(language_code)
        try:
            Image.open(file_name)
            return True
        except IOError:
            await message.reply(file_not_valid, reply_markup=ReplyKeyboardRemove())                
            # os.remove(file_name)
            return False
            
    def remove_file_if_exists(self, file):    
        for file in glob.glob(file + ".*"):
                if os.path.exists(file):
                    os.remove(file)
                    
    def get_file_details(self, file_name):
        # Ottieni i dettagli del file
        nome_completo = os.path.basename(file_name).split(".")[0]
        percorso = os.path.dirname(os.path.abspath(file_name)) #visualizza percorso file
        file = file_name.split(".")[0]
        extention = file_name.split(".")[-1]
        file_jpg = f'{percorso}//{file}.jpg'
        return nome_completo, file_name, extention, file_jpg
    
    async def read_process(self, message: Message, state:FSMContext):
        info = UserInfo(message)
        user_id = info.user_id
        language_code = info.language
        try:
            if user_id in self.blocked_users:
                loading = self.lang.loading(language_code)
                await message.reply(loading)
                return
            file_Path, file_name = await self.recive_image(message)
            check = await self.check_image(file_Path, message)
            if check == True:
                Database().save_image(user_id, file_Path)
                await self.color.color_choose(message, state)
            else:
                os.remove(file_name)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{user_id}:{ex}")
            
    def delate(self, user_id):
        file_path = Database().get_image(user_id)    
        if file_path != None:
            # file, extention, file_jpg = self.get_file_details(file_name)
            file_info = FileInfo(file_path)
            nome = file_info.nome_completo
            percorso = file_info.percorso
            file = f"{percorso}/{nome}"
            self.remove_file_if_exists(file) #elimina file
            Database().delate_image(user_id)
            
class FileInfo: # crea una classe per gestire i colori e le impostazioni del QR
    def __init__(self, file_name):
        self.nome_completo = os.path.basename(file_name).split(".")[0]
        self.percorso = os.path.dirname(os.path.abspath(file_name)) #visualizza percorso file
        self.file = file_name.split(".")[0]
        self.extention = file_name.split(".")[-1]
            
