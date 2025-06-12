from aiogram import types, filters, F, Dispatcher, Bot
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

bot = Bot(token='7289182096:AAFG2ZlqaKzeG3y7FGPhRMxCjljMDbtCgkM')
dp = Dispatcher(bot=bot)



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
