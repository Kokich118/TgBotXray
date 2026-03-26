from aiogram import Router, F
from aiogram.types import Message

from keyboards.warp_main_menu import warp_main_kb

vpn_warp_router = Router()

@vpn_warp_router.message(F.text == "VPN через WARP")
async def handle_hello(message: Message):
    await message.answer(
        'Перейдите на сайт https://warp-generator.github.io/. У AmneziaWG справа есть настройки, где вы можете выбрать какие ресурсы вы хотите, чтобы работали через VPN (по умолчанию работают все). Затем скачайте любой из 3 вариантов и проверьте работоспособность (если 1 не работает, то пробуйте другой вариант. После скачивания конфига скачайте программу AmneziaWG (https://github.com/amnezia-vpn/amneziawg-windows-client/releases/tag/2.0.0). После установки и входа в приложение слева снизу будет кнопка "Добавить туннель". Выберите файл конфига, который вы скачали. Выберите слева ваш конфиг и справа появится кнопка подключиться. Приятного пользования!',
        reply_markup=warp_main_kb
    )