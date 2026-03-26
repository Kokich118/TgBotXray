from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

warp_main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)