from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers import start

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start.router)

# подключение роутеров/хендлеров

if __name__ == "__main__":
    dp.run_polling(bot)