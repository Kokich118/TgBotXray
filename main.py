from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers.start import start_router
from handlers.xui_server_main import xui_server_main_router
from handlers.vpn_warp import vpn_warp_router
from handlers.main_menu import main_menu_router
from handlers.user_config import user_config_router
from handlers.xui_add_client import xui_add_client_router
from handlers.xui_delete_client import xui_delete_client_router

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(xui_server_main_router)
dp.include_router(start_router)
dp.include_router(vpn_warp_router)
dp.include_router(main_menu_router)
dp.include_router(user_config_router)
dp.include_router(xui_add_client_router)
dp.include_router(xui_delete_client_router)

# подключение роутеров/хендлеров

if __name__ == "__main__":
    dp.run_polling(bot)