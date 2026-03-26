from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

proxy_tg_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)