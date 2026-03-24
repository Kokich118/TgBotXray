from aiogram import Bot, Dispatcher

bot = Bot(token="TOKEN")
dp = Dispatcher()

# подключение роутеров/хендлеров

dp.run_polling(bot)