from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="VPN через наш сервер")],
        [KeyboardButton(text="Proxy для Telegram")],
        [KeyboardButton(text="VPN через WARP")]
    ],
    resize_keyboard=True
)