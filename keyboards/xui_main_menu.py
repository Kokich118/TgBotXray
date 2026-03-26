from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

xui_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Посмотреть свой конфиг")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)