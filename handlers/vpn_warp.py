from aiogram import Router, F
from aiogram.types import Message

vpn_warp_router = Router()

@vpn_warp_router.message(F.text == "VPN через WARP")
async def handle_hello(message: Message):
    await message.answer("WARP")