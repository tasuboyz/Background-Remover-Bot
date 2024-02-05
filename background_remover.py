from aiogram.dispatcher.dispatcher import loggers
from bot import BOT
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession
import logging
from db import Database
import asyncio
import logger_config

async def on_start():
    Database().create_table()
    print("Bot avviato")

async def on_stop():
    
    print("Bot fermato")

async def main():
    try:       
        my_bot = BOT()
        await on_start()
        await my_bot.dp.start_polling(my_bot.bot)
    except Exception as ex:
        logger_config.logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
    except KeyboardInterrupt:
        print("Interrotto dall'utente")
    finally:
        # await my_bot.dp.stop_polling()
        await on_stop()
        
if __name__ == '__main__':   
    asyncio.run(main())
