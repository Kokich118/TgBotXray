from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

xui_absent_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать свой конфиг")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)