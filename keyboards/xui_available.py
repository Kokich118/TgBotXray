from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

xui_available_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Удалить свой конфиг")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)