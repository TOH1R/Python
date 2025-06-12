import asyncio
from aiogram import Dispatcher, Bot
from app.handlers import dp

bot = Bot(token='7417222730:AAGkm54k3zqEnAhDnR5mWBH6IbJe9EY5dOI')
router = Dispatcher(bot=bot)


async def main():
    router.include_router(dp)
    await router.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
