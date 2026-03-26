from aiogram import Router, F
from aiogram.types import Message

from keyboards.proxy_tg_menu import proxy_tg_menu_kb

proxy_tg_menu_router = Router()

@proxy_tg_menu_router.message(F.text == "Proxy для Telegram")
async def handle_hello(message: Message):
    await message.answer(
        'Для работы телеграм в наше время без прокси не обойтись. В нашем случае прокси можно добавить в телеграм либо "доп. настройки" -> "тип соединения", либо "данные и память" -> "тип соединения". Затем нужно ввести данные по ссылке в таблице https://docs.google.com/spreadsheets/d/1INSlq3ld2TY2J7eBkeMn6mO2haLsu6mOWa3GUaVNS-Q/edit?usp=sharing. Сохраните себе ссылку, так как телеграм может перестать грузиться',
        reply_markup=proxy_tg_menu_kb
    )