from aiogram import types, filters, F, Dispatcher, Bot
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

bot = Bot(token='7417222730:AAGkm54k3zqEnAhDnR5mWBH6IbJe9EY5dOI')
dp = Dispatcher(bot=bot)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
