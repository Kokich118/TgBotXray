from aiogram import Router, F
from aiogram.types import Message

from programs.CheckClient import checkclient

from keyboards.xui_absent import xui_absent_kb
from keyboards.xui_available import xui_available_kb

user_config_router = Router()

@user_config_router.message(F.text == "Посмотреть свой конфиг")
async def handle_hello(message: Message):
    username = message.from_user.username
    url = await checkclient(username)
    if url:
        await message.answer(
            url,
            reply_markup=xui_available_kb,
        )
    else:
        await message.answer(
            "Ваш конфиг отсутствует. Поэтому создайте его!",
            reply_markup=xui_absent_kb
        )